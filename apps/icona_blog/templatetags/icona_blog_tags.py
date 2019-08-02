from django import template
register = template.Library()

from mezzanine.blog.models import BlogPost


@register.inclusion_tag("icona_shop/includes/popular_post.html")
def popular_post():
    """
    Muestra los ultimos post mas populares
    El criterio de mas popular es primero por rating y segundo
    por fecha de publicacion
    """

    post_popular = BlogPost.objects.all().order_by('-rating_sum', '-created')[:2]

    return {'post_popular': post_popular}


@register.inclusion_tag("blog/custom_rating_form.html")
def custom_rating_fields(rating_fields):
    """
    Personalizacion de las opciones de rating del blog. Especificamente
    los radios para votar
    """

    return {'rating_fields': rating_fields}



#Refactorizar no va aqui en blog
@register.inclusion_tag("icona_shop/includes/categories_home.html")
def categories_home():
    from cartridge.shop.models import Category
    return {'page_branch': Category.objects.all()}