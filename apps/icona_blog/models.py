from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.blog.models import BlogPost
from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.icona_shop.shop_util import send_email
from django.contrib.sites.models import Site
from django.template.loader import render_to_string

class BlogSubscriptor(models.Model):
    """
    Representa los email a los cuales enviar correo cuando se crea
    un nuevo blog
    """
    email = models.CharField(_("Email"), max_length=30, unique=True)


class BlogPostSubscriptor(models.Model):
    """
    Indica para un sbuscriptor los post creados para los cuales recibe
    notificacion
    """
    subscriptor = models.ForeignKey(BlogSubscriptor)
    blog_post = models.ForeignKey(BlogPost)


@receiver(post_save, sender=BlogPost, dispatch_uid="notify_blog")
def blog_post_new(sender, instance, **kwargs):
    """
    Este signal es usado para determinar cuando un blog se crea/modifica
    y enviar correo a todos los subscriptores que aun no han recibido notificacion
    de este post
    """

    domain = Site.objects.get_current().domain
    link = '%s/blog/%s' % (domain, instance.slug)

    for subscriptor in BlogSubscriptor.objects.all():
        if BlogPostSubscriptor.objects.filter(subscriptor=subscriptor,
                                            blog_post=instance).count() == 0:


            ctx = {
                'link': link,
            }

            msg_mail = render_to_string('icona_blog/email/new-tutorial', ctx)
            send_email(subscriptor.email, "New Blog Post", msg_mail)

            notify_post_subscriptor = BlogPostSubscriptor()
            notify_post_subscriptor.blog_post = instance
            notify_post_subscriptor.subscriptor = subscriptor
            notify_post_subscriptor.save()