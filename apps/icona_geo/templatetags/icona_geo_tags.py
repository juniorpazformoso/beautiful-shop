from django import template
register = template.Library()

from apps.icona_geo.models import City, Country, Cap
from apps.icona_profile.models import Profile
from mezzanine.utils.importing import import_dotted_path

@register.inclusion_tag("icona_geo/city_select.html")
def city_select(id_city):
    """
    Construye un select usando las ciudades disponibles
    """

    return {'cities': City.objects.all(), 'id_city': id_city}


@register.inclusion_tag("icona_geo/country_select.html")
def country_select():
    """
    Construye un select usando los paises disponibles
    """

    return {'countries': Country.objects.all()}


@register.inclusion_tag("icona_geo/cap_select.html")
def country_cap(id_cap):
    """
    Construye un select usando los cap disponibles
    """

    return {'caps': Cap.objects.all(), 'id_cap': id_cap}

@register.inclusion_tag("icona_geo/shop_locator_list.html")
def shop_locator_list():
    """
    Devuelve la lista de peluquerias y centros de esteticas que se pondran
    en el mapa de Shop locator
    """

    return {'profiles': Profile.objects.all()}


@register.inclusion_tag("icona_geo/shop_locator_map.html")
def shop_locator_map():
    """
    Devuelve el mapa con todos los marcadores de peluquerias y centros esteticos ubicados
    """

    return {'profiles': Profile.objects.all()}



@register.inclusion_tag("generic/includes/comments.html", takes_context=True)
def comments_for_mio(context, obj):
    """
    Provides a generic context variable name for the object that
    comments are being rendered for.
    """
    from apps.icona_comments.forms import CommentFormWithTitle
    form_class = CommentFormWithTitle
    form = form_class(context["request"], obj)
    context_form = context.get("posted_comment_form", form)
    context.update({
        'posted_comment_form':
            context_form if context_form.target_object == obj else form,
        'unposted_comment_form': form,
        'comment_url': reverse("comment"),
        'object_for_comments': obj,
    })
    return context.flatten()