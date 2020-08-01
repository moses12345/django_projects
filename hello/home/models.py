from django.db import models

class Contact(models.Model):
    email=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    discription=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
class About(models.Model):
    name=models.CharField(max_length=30)
    about_you=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.name
    

    
