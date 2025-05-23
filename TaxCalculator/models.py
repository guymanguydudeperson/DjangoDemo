from django.db import models

class EmployerInfo(models.Model):
    company_name = models.CharField(max_length=255)
    ein = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    ssn = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name
