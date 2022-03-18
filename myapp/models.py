from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Signature(models.Model):
    name = models.CharField(max_length=50)
    value = models.FloatField()
    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length = 55)
    idUser = models.BigIntegerField()
    email = models.CharField(max_length = 80)
    phone = models.CharField(max_length = 15,null=True,blank=True)
    active = models.BooleanField(default = False)

    signatureFK = models.ForeignKey(Signature, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=100)
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Favorite(models.Model):
    movie_id = models.ForeignKey(Movies,on_delete=models.CASCADE)
    user_is = models.ForeignKey(Users, on_delete=models.CASCADE)


