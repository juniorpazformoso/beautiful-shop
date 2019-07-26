from django.contrib import admin
from django.contrib.auth import get_user_model
from mezzanine.accounts.admin import UserProfileAdmin
from apps.icona_profile.models import Profile
from django.utils.translation import ugettext_lazy as _
from copy import deepcopy
from mezzanine.core.admin import StackedDynamicInlineAdmin
from apps.icona_profile.models import ProductPreference


User = get_user_model()


class UserProductPreferenceAdmin(StackedDynamicInlineAdmin):
    model = ProductPreference
    fields = ('file',)


class ProfileInline(admin.StackedInline):
    model = Profile


class ProfileAdmin(UserProfileAdmin):
    inlines = (ProfileInline, UserProductPreferenceAdmin)

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.allow_tags = True
    group.short_description = _('Groups')

    list_display = deepcopy(UserProfileAdmin.list_display) + ('group',)


if User in admin.site._registry:
    admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)

