from django.db import models

# Create your models here.
class Items(models.Model):
    def __str__(self):
       return self.item_name

    #def __str__(self):
    #    return str((self.item_name,self.item_desc,self.item_price))

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://th.bing.com/th/id/OIP.nLDShz9SB5YleA3GH5fJJAHaHa?pid=ImgDet&rs=1')

