from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TypeChoices(TextChoices):
    BLOG = "B", _("Blog")
    NEWS = "N", _("News")
    ARTICLES = "A", _("Best Articles")
