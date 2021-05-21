from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


# Create your models here.
class calculate(models.Model):

    age1 = models.IntegerField(null=True, blank=True, default=0)



    def save(self, *args, **kwargs):

        self.age1 = date.today().year - self.dob.year
        super(calculate, self).save(*args, **kwargs)

    Displayfields = ['dob', 'age1']

    def no_future(value):
        today = date.today()
        if value > today:
            raise ValidationError('Purchase_Date cannot be in the future.')

    dob = models.DateField(null=True, validators=[no_future])









