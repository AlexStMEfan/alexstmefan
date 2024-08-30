from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class lessonmodel(models.Model):
    name_Lesson = models.TextField()
    date_lesson = models.DateField()
    email_student = models.EmailField()
    fio_student = models.TextField()
    phone_teacher_regex = RegexValidator(regex=r'^\+?7?\d{9,11}$', message="Phone number must be entered in the format: '+799999999999'. Up to 11 digits allowed.")
    phone_teacher = models.CharField(validators=[phone_teacher_regex], max_length=17, blank=True)
    number_classroom = models.TextField()
    email_teach_teach_organization = models.EmailField()
    FIO_director_organization = models.TextField()
    index_adress = models.IntegerField()
    rayon = models.TextField()
    city = models.TextField()
    street = models.TextField()
    otzyv = models.TextField()
    