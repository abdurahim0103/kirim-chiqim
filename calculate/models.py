from django.db import models

# Create your models here.
 

class User(models.Model):
    firs_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    phone_number=models.CharField(max_length=100)
    adress=models.TextField()

    def __str__(self):
        return self.firs_name


class Income(models.Model):
    amount=models.FloatField()
    desc=models.TextField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True)



class Expanse(models.Model):
    amount=models.FloatField()
    desc=models.TextField(null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True)

    


