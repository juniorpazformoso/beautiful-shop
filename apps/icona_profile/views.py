from django.shortcuts import render
from django.http import HttpResponse
from apps.icona_geo.models import City, Country, Cap
from apps.icona_profile.models import Profile
from django.contrib.auth.models import User
from django.http import JsonResponse
from apps.icona_shop.shop_util import send_email
from mezzanine.conf import settings
from django.template.loader import render_to_string
from cartridge.shop.models import ProductImage
from apps.icona_profile.models import ProductPreference
from django.contrib.messages import info, error
from django.utils.translation import ugettext_lazy as _

def user_product_preference(request):
    prod_img = ProductImage.objects.get(pk=request.POST.get('product_img_pk'))
    product_preference = ProductPreference()
    product_preference.user = request.user
    product_preference.product_image = prod_img
    product_preference.file = prod_img.file
    product_preference.save()

    return JsonResponse({'success': 'true'}, safe=False)


def generate_username(useremail):
    users = User.objects.filter(username=useremail)

    if users:
        for i in range(1, users.count() + 100):
            if not User.objects.filter(username=useremail + str(i)):
                return useremail + str(i)

    return useremail


def create_profile_consumer(request):
    """
    Create a profile consumer from page icona
    """
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    cell_phone = request.POST.get('phone')
    via_numero = request.POST.get('via_numero')
    city = request.POST.get('city')
    cap = request.POST.get('cap')

    user = User()
    user.email = email
    user.username = generate_username(email.split("@")[0])
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = False

    user.save()

    profile = Profile()
    profile.user = user
    profile.cell_phone = cell_phone
    profile.via_numero = via_numero

    profile.city = City.objects.get_or_create(name=city)[0]
    profile.cap = Cap.objects.get_or_create(cap=cap)[0]
    profile.consumer = True
    profile.save()

    subject = request.POST.get('subject')
    message = request.POST.get('message')

    ctx = {
        'message': message,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'cell_phone': cell_phone,
        'via_numero': via_numero,
        'city': city,
        'cap': cap,
    }



    msg_mail = render_to_string('icona_profile/email/profile_notify', ctx)

    send_email(settings.DEFAULT_FROM_EMAIL, subject, msg_mail)

    return JsonResponse({'success': 'true'}, safe=False)


def create_profile(request):
    """
    Register a profile from page icona
    """
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    cell_phone = request.POST.get('phone')
    via_numero = request.POST.get('via_numero')
    city = request.POST.get('city')
    cap = request.POST.get('cap')
    social_reason = request.POST.get('social_reason')

    user = User()
    user.email = email
    user.username = generate_username(email.split("@")[0])
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = False

    user.save()

    profile = Profile()
    profile.user = user
    profile.cell_phone = cell_phone
    profile.via_numero = via_numero

    profile.city = City.objects.get_or_create(name=city)[0]
    profile.cap = Cap.objects.get_or_create(cap=cap)[0]
    profile.partner = True
    profile.social_reason = social_reason
    profile.save()

    subject = request.POST.get('subject')
    message = request.POST.get('message')

    ctx = {
        'message': message,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'cell_phone': cell_phone,
        'via_numero': via_numero,
        'city': city,
        'cap': cap,
        'social_reason': social_reason
    }



    msg_mail = render_to_string('icona_profile/email/profile_notify', ctx)

    send_email(settings.DEFAULT_FROM_EMAIL, subject, msg_mail)

    return JsonResponse({'success': 'true'}, safe=False)