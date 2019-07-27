def get_form():
    return ThreadedCommentWithPhoneForm


def get_model():
    from mezzanine.generic.models import ThreadedComment
    return ThreadedComment

