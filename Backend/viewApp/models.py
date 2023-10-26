from django.db import models

# Create your models here.
class Book(models.Model):
    
    title = models.CharField(verbose_name="Book Name",max_length=32)
    price = models.IntegerField(verbose_name="Price")
    pub_date = models.DateField(verbose_name="Publish Date")

    bread = models.IntegerField(verbose_name="Read")
    bcomments = models.IntegerField(verbose_name="Comment")

    publish = models.ForeignKey("Publish", on_delete=models.CASCADE, verbose_name="Publisher")
    authors = models.ManyToManyField("Author", verbose_name="Author")

    def __str__(self):
        return self.title

class Publish(models.Model):
    name = models.CharField(verbose_name="Publisher", max_length=32)
    email = models.EmailField(verbose_name="Publisher Email")

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(verbose_name="Author", max_length=32)
    age = models.IntegerField(verbose_name="Age")

    def __str__(self):
        return self.name
    

