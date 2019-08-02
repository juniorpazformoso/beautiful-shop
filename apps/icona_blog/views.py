from django.shortcuts import render
from apps.icona_blog.models import BlogSubscriptor
from django.http import JsonResponse
from apps.icona_shop.shop_util import send_email
from django.contrib.messages import info, error
from django.utils.translation import ugettext_lazy as _


def subscriptor_email(request):
    """
        Registra a un nuevo subscriptor
    """
    email = request.POST.get('email')
    blog_subscriptor = BlogSubscriptor()
    blog_subscriptor.email = email
    blog_subscriptor.save()

    info(request, _("The subscription was created successfully."))

    return JsonResponse({'success': 'true'}, safe=False)



