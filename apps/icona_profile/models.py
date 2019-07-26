from django.db import models
from mezzanine.utils.models import AdminThumbMixin, upload_to
from mezzanine.core.fields import FileField
from django.utils.translation import ugettext_lazy as _
from cartridge.shop.models import ProductImage
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from cartridge.shop.models import Product

class Profile(models.Model, AdminThumbMixin):
    """
    A profile.
    """
    partner = models.BooleanField(_("Partner"), default=False)
    consumer = models.BooleanField(_("Consumer"), default=False)

    user = models.OneToOneField("auth.User", related_name="Profile")
    via_numero = models.CharField(_("Via numero"), max_length=200, null=True, blank=True)
    cell_phone = models.CharField(_("Cell phone"), max_length=30, null=True, blank=True)

    city = models.ForeignKey("icona_geo.City", null=True, blank=True, verbose_name=_("City"))
    cap = models.ForeignKey("icona_geo.Cap", null=True, blank=True, verbose_name=_("Cap"))


    #Business fields
    is_public = models.BooleanField(_("Published on shop locator"), default=False)
    business_name = models.CharField(_("Business name"), max_length=200, null=True, blank=True)
    business_postal_address = models.CharField(_("Business postal address"), max_length=200, null=True, blank=True)
    business_city = models.ForeignKey("icona_geo.City", null=True, blank=True, verbose_name=_("Business City"), related_name='BusinessCity')
    business_cap = models.ForeignKey("icona_geo.Cap", null=True, blank=True, verbose_name=_("Business Cap"), related_name='BusinessCap')
    business_phone = models.CharField(_("Business phone"), max_length=30, null=True, blank=True)
    social_reason = models.CharField(_("Social reason"), max_length=30, null=True, blank=True)





class ProductPreference(models.Model, AdminThumbMixin):
    """
    User product preference
    """
    user = models.ForeignKey("auth.User", related_name='ProductPreference')
    product_image = models.ForeignKey(ProductImage)
    file = FileField(_("Image"), max_length=255, format="Image",
        upload_to=upload_to("shop.ProductImagePreference.file", "product"))



@receiver(pre_save, sender=Profile, dispatch_uid="profile_save")
def profile_save(sender, instance, **kwargs):
    if instance.business_postal_address and instance.business_cap and instance.business_city and instance.business_name:
        instance.is_public = True
    else:
        instance.is_public = False



@receiver(pre_save, sender=Product, dispatch_uid="populate_short_description_listing")
def populate_short_description_listing(sender, instance, **kwargs):
    if not instance.short_description_listing:
        instance.short_description_listing = instance.short_description