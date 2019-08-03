from django.conf.urls import url
from apps.icona_shop.views import IconaPage

urlpatterns = [
    url(r'icona$', IconaPage.as_view(), name="icona_page"),
]