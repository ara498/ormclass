from django.db import models

# Create your models here.
class Countries(models.Model):
    Countries_id=models.IntegerField(primary_key=True)
    Countries_name=models.CharField(max_length=50)
    def __str__(self):
        return self.Countries_name
class Capital(models.Model):
    Capital_id=models.IntegerField(primary_key=True)
    Capital_name=models.CharField(max_length=50)
    Capital_code=models.IntegerField()
    Countries_id=models.OneToOneField( Countries,on_delete=models.CASCADE)
    def __str__(self):
        return self.Capital_name  