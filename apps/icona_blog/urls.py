from django.conf.urls import url
from apps.icona_blog.views import subscriptor_email

urlpatterns = [
    url(r'subscriptor_email', subscriptor_email, name="subscriptor_email"),
]