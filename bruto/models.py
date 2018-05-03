# -*- coding: utf-8 -*-
from django.db import models

def unique_upload(instance, filename):
    instance.my_file.open()
    # Only hash chunk size of file for avoiding DOS
    contents = instance.my_file.read(instance.my_file.DEFAULT_CHUNK_SIZE)

    return None

class Document(models.Model):
    docfile = models.FileField(upload_to=unique_upload)
