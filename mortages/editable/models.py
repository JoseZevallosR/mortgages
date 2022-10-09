from django.db import models
from django.conf import settings
from django.urls.base import reverse
from django.shortcuts import redirect
from django.template.defaultfilters import slugify

from django.dispatch import receiver
import os, shutil
# Create your models here.
class tables(models.Model):
    file_path = models.FileField(upload_to='files/')