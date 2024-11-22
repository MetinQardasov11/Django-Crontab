from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    expiration_date = models.DateField()
    expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name