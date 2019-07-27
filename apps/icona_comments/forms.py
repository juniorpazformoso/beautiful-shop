from django import forms
from django_comments.forms import CommentForm
from django.utils.translation import ugettext_lazy as _
from mezzanine.generic.forms import ThreadedCommentForm
from mezzanine.core.forms import Html5Mixin
from mezzanine.utils.deprecation import is_authenticated
from mezzanine.utils.email import split_addresses, send_mail_template
from mezzanine.utils.static import static_lazy as static
from mezzanine.utils.views import ip_for_request
from mezzanine.generic.models import ThreadedComment
from django_comments.signals import comment_was_posted
from django.utils import six
from mezzanine.conf import settings
from django.utils.safestring import mark_safe

class ThreadedCommentWithPhoneForm(ThreadedCommentForm):
    phone = forms.CharField(label=_("Cellulare (non si pubblica)"), required=False)
    name = forms.CharField(label=_("Nome *"), required=False)
    email = forms.EmailField(label=_("Email *"), required=False)
    comment = forms.CharField(label=_('Commento *'), widget=forms.Textarea, required=False)


    # These are used to get/set prepopulated fields via cookies.
    cookie_fields = ("name", "email", "url")
    cookie_prefix = "mezzanine-comment-"
    field_order = ['name', 'email', 'phone', 'comment']

    def save(self, request):
        """
        Saves a new comment and sends any notification emails.
        """
        comment = self.get_comment_object()
        obj = comment.content_object
        if is_authenticated(request.user):
            comment.user = request.user
        comment.by_author = request.user == getattr(obj, "user", None)
        comment.ip_address = ip_for_request(request)
        comment.replied_to_id = self.data.get("replied_to")
        comment.phone = self.data.get("phone")

        # Mezzanine's duplicate check that also checks `replied_to_id`.
        lookup = {
            "content_type": comment.content_type,
            "object_pk": comment.object_pk,
            "user_name": comment.user_name,
            "user_email": comment.user_email,
            "user_url": comment.user_url,
            "replied_to_id": comment.replied_to_id,
        }
        for duplicate in self.get_comment_model().objects.filter(**lookup):
            if (duplicate.submit_date.date() == comment.submit_date.date() and
                    duplicate.comment == comment.comment):
                return duplicate

        comment.save()
        comment_was_posted.send(sender=comment.__class__, comment=comment,
                                request=request)
        notify_emails = split_addresses(settings.COMMENTS_NOTIFICATION_EMAILS)
        if notify_emails:
            subject = ugettext("New comment for: ") + str(obj)
            context = {
                "comment": comment,
                "comment_url": add_cache_bypass(comment.get_absolute_url()),
                "request": request,
                "obj": obj,
            }
            send_mail_template(subject, "email/comment_notification",
                               settings.DEFAULT_FROM_EMAIL, notify_emails,
                               context)
        return comment
