from django.db import models

# Create your models here.
from private_storage.fields import PrivateFileField


class Alert(models.Model):
    title = models.CharField(max_length=255)
    autor=models.CharField(max_length=255)
    phone=models.CharField(max_length=20)
    due_date = models.DateField()
    Resolue = models.BooleanField()
    Encours = models.BooleanField()
    attachment = models.FileField(upload_to='public', null=True)
    private_file = PrivateFileField(upload_to='private', null=True)

    list = models.ForeignKey('AlertList', null=False, on_delete=models.CASCADE)


class AlertList(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Alert List'
        verbose_name_plural = 'Alert Lists'