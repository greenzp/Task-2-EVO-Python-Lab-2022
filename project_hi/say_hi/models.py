from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
