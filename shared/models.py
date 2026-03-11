from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True


class Staff(BaseModel):
    full_name = models.CharField(max_length=128, verbose_name=_('Full name'))
    profession = models.CharField(max_length=128, verbose_name=_('Profession'))
    image = models.ImageField(upload_to='staff/', null=True, blank=True, verbose_name=_('Image'))
    info = models.CharField(max_length=255, verbose_name=_('Information'))

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'staff'
        verbose_name = _('Staff member')
        verbose_name_plural = _('Staff members')


class Contact(BaseModel):
    full_name = models.CharField(max_length=128, verbose_name=_('Full name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=13, blank=True, verbose_name=_('Phone'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))

    is_read = models.BooleanField(default=False, verbose_name=_('Is read'))

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contacts'
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')