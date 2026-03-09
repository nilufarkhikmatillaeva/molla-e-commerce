from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class Staff(models.Model):
#     full_name = models.CharField(max_length=128)
#     profession = models.CharField(max_length=128)
#     image = models.ImageField(upload_to='staff/', null=True, blank=True)
#     info = models.CharField(max_length=255)
#     social_links = models.JSONField(blank=True, null=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.full_name

    class Meta:
        db_table = 'staff'
        verbose_name = 'staff'
        verbose_name_plural = 'staff'

class Contact(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contacts'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
