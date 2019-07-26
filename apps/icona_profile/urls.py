from django.conf.urls import url
from apps.icona_profile.views import create_profile, user_product_preference, create_profile_consumer

urlpatterns = [
    url(r'created$', create_profile, name="create_profile"),
    url(r'created/consumer$', create_profile_consumer, name="create_profile_consumer"),

    url(r'product/save/yeapcasa$', user_product_preference, name="save_product"),
]