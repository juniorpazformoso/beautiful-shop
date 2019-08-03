from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy
from cartridge.shop.admin import ProductAdmin, CategoryAdmin, ProductVariationAdmin, ProductImageAdmin
from cartridge.shop.models import Product, Category
from mezzanine.core.admin import TabularDynamicInlineAdmin

product_fieldsets = deepcopy(ProductAdmin.fieldsets)


product_fieldsets = deepcopy(ProductAdmin.fieldsets)

product_fieldsets[0][1]["fields"].insert(2, "featured_image")
product_fieldsets[0][1]["fields"].insert(6, "new_product")
product_fieldsets[0][1]["fields"].insert(6, "limited_edition")
product_fieldsets[0][1]["fields"].insert(7, "artext")
product_fieldsets[0][1]["fields"].insert(6, "short_description_listing")
product_fieldsets[0][1]["fields"].insert(7, "short_description")
product_fieldsets[0][1]["fields"].insert(2, "plus_content")
product_fieldsets[0][1]["fields"].insert(2, "ingredients")

category_fieldsets = deepcopy(CategoryAdmin.fieldsets)
#category_fieldsets[0][1]["fields"].insert(1, "short_description_listing")
category_fieldsets[0][1]["fields"].insert(2, "short_text")



class ProductAdmin(ProductAdmin):
    fieldsets = product_fieldsets
    inlines = (ProductImageAdmin, ProductVariationAdmin)


class CategoryAdmin(CategoryAdmin):
    fieldsets = category_fieldsets


admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)

admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)

