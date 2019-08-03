from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _


# register_setting(
#     name="INSTAGRAM_URL",
#     label=_("Instagram url"),
#     editable=True,
#     default=""
# )
#
# register_setting(
#     name="FACEBOOK_URL",
#     label=_("Facebook url"),
#     editable=True,
#     default=""
# )


# The next settings declaration is an override, the original declaration is in
# site-packages/mezzanine/core/defaults.py
# THIS OVERRIDE IS NECESSARY IF, AND ONLY IF, RSTATUS_FOR_SURVEY_USERS AND
# PRIZE_FOR_SURVEY_USERS WILL BE USED IN A TEMPLATE,
# otherwise you don't need to make this declaration.

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    append=True,
    default=(
        "ACCOUNTS_APPROVAL_REQUIRED", "ACCOUNTS_VERIFICATION_REQUIRED",
        "ADMIN_MENU_COLLAPSED",
        "BITLY_ACCESS_TOKEN", "BLOG_USE_FEATURED_IMAGE",
        "COMMENTS_DISQUS_SHORTNAME", "COMMENTS_NUM_LATEST",
        "COMMENTS_DISQUS_API_PUBLIC_KEY", "COMMENTS_DISQUS_API_SECRET_KEY",
        "COMMENTS_USE_RATINGS", "DEV_SERVER", "FORMS_USE_HTML5",
        "GRAPPELLI_INSTALLED", "GOOGLE_ANALYTICS_ID", "JQUERY_FILENAME",
        "JQUERY_UI_FILENAME", "LOGIN_URL", "LOGOUT_URL", "SITE_TITLE",
        "SITE_TAGLINE", "USE_L10N", "USE_MODELTRANSLATION",
        ## NEW ##
        "INSTAGRAM_URL", "FACEBOOK_URL",
    ),
)
