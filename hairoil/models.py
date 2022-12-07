from django.db import models

# Create your models here.
class register_form(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  hashpass = models.TextField()

class contact_form(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	message = models.CharField(max_length=255)

class productup(models.Model):
  catagory = models.CharField(max_length=255)
  product_name = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  img = models.ImageField(upload_to='uploads/')
  details = models.TextField()

class cart_tb(models.Model):
  pid=models.ForeignKey(productup, on_delete=models.CASCADE)
  uid=models.ForeignKey(register_form, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  totalprice=models.CharField(max_length=255)
  status=models.CharField(max_length=255)

class shipping(models.Model):
  uid=models.ForeignKey(register_form, on_delete=models.CASCADE)
  fullname = models.CharField(max_length=255)
  number = models.CharField(max_length=255)
  landmark = models.CharField(max_length=255)
  city = models.CharField(max_length=255)




