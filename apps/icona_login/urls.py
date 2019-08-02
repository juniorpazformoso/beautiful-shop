from django.conf.urls import url
from apps.icona_login.views import register_user, login_user

urlpatterns = [
    url(r'new$', register_user, name="register_user"),
    url(r'login$', login_user, name="login_user"),
]