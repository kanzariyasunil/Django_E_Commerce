from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default='')
    subcategory = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=100)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = 'shop/images',default='')
    
    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=50,default='')
    desc = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip_code =models.CharField(max_length=120)
    phone = models.CharField(max_length=10,default=None)
    
    
class OrdersUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7] + "..."
    