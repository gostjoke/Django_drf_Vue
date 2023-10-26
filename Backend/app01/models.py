from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    sex = models.BooleanField(default=1, verbose_name="Gender")
    age = models.IntegerField(verbose_name="Age")
    class_null = models.CharField(max_length=5, verbose_name="Class")
    description = models.TextField(verbose_name = "Description", max_length =1000)

    class Meta:
        db_table = "tb_student"
        verbose_name = "student"
        verbose_name_plural = verbose_name