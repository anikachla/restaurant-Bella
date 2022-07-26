from django.db import models


class Contact(models.Model):
    #sno = models.AutoField(primary_key=True,blank=True)
    name = models.CharField(max_length =255)
    phone = models.CharField(max_length= 13)
    email = models.EmailField(max_length=100)
    issue = models.TextField(max_length=2000)
    #timestamp = models.DateTimeField(auto_now_add = True ,blank=True)

    def __str__(self):
        return self.email
    
    """this Contact model class maps to a single table in our project’s database, 
    with each of its attributes corresponding to a specific column in that table.
    The email attribute is an instance of Django’s models.EmailField() class which
    only allows valid email addresses to be saved, a feature that will come in handy 
    when we need it for validating our contact form data. 
    Django has many other built-in model fields 
    to provide useful constraints and additional features for various kinds of data, 
    such as the CharFieldand TextField classes that we use here for our subject and message fields."""
# Create your models here.

class Dish(models.Model):
    id:int
    name = models.CharField(max_length =100)
    img = models.ImageField(upload_to= 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    time = models.CharField(max_length= 50)
    category = models.ForeignKey('Category', null=True, blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
class Category(models.Model):
    name= models.CharField(max_length =100)
    id:int
    
    def __str__(self):
        return self.name
    

class OrderModel(models.Model):
    created_on= models.DateTimeField(auto_now_add= True)
    price = models.IntegerField()
    #items = models.ManyToManyField('Dish',related_name='order',blank=True )
    item =models.TextField(max_length=100)
    #order_id =models.IntegerField(null=False, blank=True,unique=True,primary_key=True)
    #item_id= models.OneToOneField(Dish, on_delete=models.CASCADE)
    item_id= models.IntegerField(null=True, blank=True)
    item_uniq = models.IntegerField(null=True, blank=True)
    
    
    # def __str__(self):
    #     return "f'Order: {self.created_on.strftime("%b %d %I: %M %p")}"
    
class Orderee(models.Model):
    serve_on = models.TextField(max_length=50,null=True, blank=True)
    total =models.IntegerField(null=True, blank=True)
    serve_fn =models.TextField(max_length=100,null=True, blank=True)
    serve_ln = models.TextField(max_length=100,null=True, blank=True)
    #billitem =  models.ForeignKey('OrderModel', null=True, blank=True,on_delete=models.CASCADE)
    bill_uniq =models.IntegerField(null=True, blank=True)
    
    
    
    
    



   
    
    
    
    
    
    
    
    
    
# class Cart(models.Model):
#     user= models.ForeignKey(Dish,on_delete=models.CASCADE)
#     ordered = models.BooleanField(default =False)
#     total_price = models.IntegerField(default=0)
    
# class CartItem(models.Model):
#     cart= models.ForeignKey(Cart, on_delete= models.CASCADE) 
#     product = models.ForeignKey(Product, on_delete =models.CASCADE)
#     price = models.IntegerField(default=0)
#     total_items = models
     
