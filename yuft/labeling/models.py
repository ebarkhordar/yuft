from django.db import models
from django.db.models import DateTimeField
from django.utils.translation import gettext_lazy as _


class DateAwareModel(models.Model):
    created_at = DateTimeField(
        verbose_name=_("created at"),
        help_text=_("creation datetime of the object"),
        auto_now_add=True,
    )

    updated_at = DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("modification datetime of the object"),
        auto_now=True,
    )

    class Meta:
        abstract = True


class Label(DateAwareModel):
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("the `name` of the property."),
        max_length=128,
    )
    brand = models.CharField(
        verbose_name=_("brand"),
        help_text=_("the `brand` of the property."),
        max_length=128,
    )
    owner = models.CharField(
        verbose_name=_("owner"),
        help_text=_("the `owner` of the property."),
        max_length=128,
    )
    serial_number = models.BigIntegerField(
        verbose_name=_("serial number"),
        help_text=_("the `serial number` of the property."),
    )
    signature = models.TextField(
        verbose_name=_("signature"),
        help_text=_("the `signature` of the information."),
    )
