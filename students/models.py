from django.db import models

class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    identity_no = models.CharField("IdentityNo", max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    photo = models.ImageField(upload_to='pics', blank=True, null=True)
    def __str__(self):
        return self.name