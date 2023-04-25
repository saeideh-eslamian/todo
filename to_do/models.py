from django.db import models


BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    complete =models.BooleanField(choices=BOOL_CHOICES, default=False)
    expiry_date = models.DateField()
