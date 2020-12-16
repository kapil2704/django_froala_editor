from django.db import models
from froala_editor.fields import FroalaField


class Page(models.Model):
    content = FroalaField()
