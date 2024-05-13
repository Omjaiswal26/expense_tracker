from django.db import models

# Create your models here.
class Tracker(models.Model):
    expense_id = models.IntegerField()
    expense_type = models.CharField(max_length=255 , null= True, blank=True)
    expense_name = models.CharField(max_length=255, null=True, blank=True)
    expense_desc = models.TextField(null=True, blank=True)
    expense_amount = models.IntegerField()
    expense_date = models.DateField()