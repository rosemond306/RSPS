from django.db import models

# # Create your models here.
# class Rate (models.Model):
#   date = models.DateField()
#   price = models.IntegerField()
#   def __str__(self):
#    return str(self.price)

# class Store(models.Model):
#   storename= models.CharField(max_length=100)
#   def __str__(self):
#     return self.storename


# class LocalDelivery(models.Model):
#   options=(
#     ('standarddelivery','standarddelivery'),
#     ('expressdelivery','expressdelivery'),
#   )
#   name = models.CharField(max_length=250 ,choices=options)
#   storename = models.ForeignKey(Store,on_delete=models.DO_NOTHING)
 
#   def __str__(self):
#     return self.nam


class ShoppingType(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
    return self.title



class Storename(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
     return self.title


class DeliveryType(models.Model):
  storename=models.ForeignKey(Storename,on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=5, decimal_places=2)


  def __str__(self):
     return self.title




  