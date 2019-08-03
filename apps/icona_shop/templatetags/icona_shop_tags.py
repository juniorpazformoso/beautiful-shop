from django import template
register = template.Library()

from apps.icona_geo.models import City, Country, Cap
from apps.icona_profile.models import Profile
from mezzanine.utils.importing import import_dotted_path
from mezzanine.pages.models import  RichTextPage

@register.inclusion_tag("pages/home.html")
def home_content(page):
    r = RichTextPage.objects.get(page_ptr_id=page.id)
    return {'home_content': r.content}


def build_link(image, cell):

    link = "<a data-pk='%s' " \
           "class='product-version product-version-%s'>%s</a><span class='description-version'>%s</span>" % (image.id, image.id, cell, "")

    return link


def build_cell_color(image):
    var_class=""
    if image.number and len(image.number) >= 5:
        var_class = "text-content"

    color = "wbite"
    if image.color[1] == 'f' and (image.color[3] == 'f' or image.color[3] == 'e'):
        color = "black"

    return "<div data-pk='%s' class='size change-img %s' " \
           "style='height: 60px; width: 60px; border: 1px solid gray; " \
           "background-color: %s; " \
           "margin-bottom: 22px;'>" \
           "<span class='content' style='color: %s'> %s </span> " \
           "</div>" % (image.pk, var_class, image.color, color, image.number)


def build_cell_texture(image):
    var_class = ""
    if image.number and len(image.number) >= 5:
        var_class = "text-content"

    return "<div data-pk='%s' class='size change-img %s' " \
           "style='height: 60px; width: 60px; border: 1px solid gray; " \
           "background-image: url(%s); background-size: cover; " \
           "margin-bottom: 22px;'>" \
           "<span class='content'> %s </span> " \
           "</div>" % (image.pk, var_class, image.texture.url, image.number)


@register.inclusion_tag("shop/product_version.html")
def product_version_desktop(images):
    count_objects = images.count()

    html_result = "<table cellpadding='8' cellspacing='3' style='position:relative; left: -11px;'><body>"


    for column in range(count_objects, 0, -1):

        if column - (count_objects // column) <= 2 or count_objects <= 5:
            count_rows = count_objects // column
            list_images = list(images)
            index = 0 #Determina el indice en el arreglo de imagenes
            #donde estamos interando para construir las celdas de la tabla

            objects_in_table = 0 #Cuenta la cantidad de objetos actualmente colocados
            for rows_table in range(0, count_rows):
                html_result += "<tr>"
                for column_table in range(0, column):
                    current_image = list_images[index]

                    if current_image.texture:
                        objects_in_table += 1
                        html_result += "<td>%s</td>" % (build_link(current_image,
                                                               build_cell_texture(current_image)),)
                    else:
                        objects_in_table += 1
                        html_result += "<td>%s</td>" % (build_link(current_image,
                                                               build_cell_color(current_image)),)
                    index +=1

                html_result += "</tr>"

            if objects_in_table < count_objects:
                for column_table in range(0, count_objects - objects_in_table):
                    current_image = list_images[index]

                    if current_image.texture:
                        objects_in_table += 1
                        html_result += "<td>%s</td>" % (build_link(current_image,
                                                               build_cell_texture(current_image)),)
                    else:
                        objects_in_table += 1
                        html_result += "<td>%s</td>" % (build_link(current_image,
                                                               build_cell_color(current_image)),)
                    index +=1

                html_result += "</tr>"



            html_result += "</body></table>"


            return {'table': html_result}

