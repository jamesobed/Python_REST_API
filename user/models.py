from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.email + " (" + self.phone + ")" #+ " " + self.address + " " + str(self.age)
    
