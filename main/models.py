from django.db import models

class News1(models.Model):
    image = models.ImageField(upload_to='new_images/')
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.description

class News2(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='new2_images/')
    date = models.DateField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

class News3(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='new3_images/')
    date = models.DateField()
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title