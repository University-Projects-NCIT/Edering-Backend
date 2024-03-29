from ast import Delete
from tabnanny import verbose
from django.db import models


class Provider(models.Model):
  id = models.CharField(
    verbose_name = ("Provider id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 255,
    primary_key = True,
  )

  name = models.CharField(
    verbose_name=("Provider name"),
    help_text=(" Required "),
    max_length= 255,
    unique= False 
  )

  location = models.CharField(
    verbose_name=("Provider location"),
    help_text=(" Required , (lat, lng) "),
    max_length= 100,
    unique= False 
  )

  image_id = models.CharField(
      verbose_name = ("Provider Profile Image Url"),
      help_text=("https://my_image.png"),
      max_length= 255
  )

  known_for = models.CharField(
    verbose_name=("famous food "),
    help_text=(" Not Required"),
    max_length= 100,
    unique= False 
  )

  open_time = models.CharField(
    verbose_name=("Provider open time "),
    help_text=("10:00 AM"),
    max_length= 100,
    unique= False 
  )

  close_time = models.CharField(
    verbose_name=("Provider close time "),
    help_text=("10:00 PM"),
    max_length= 100,
    unique= False 
  )

  created_at = models.CharField(
    verbose_name=("Account created timestamp"),
    help_text= ("Timesamp take default timestamp"),
    max_length= 255 
  )

class Customer(models.Model):
  id = models.CharField(
    verbose_name = ("Customer id"),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 255,
    primary_key = True,
  )

  name = models.CharField(
    verbose_name = ("Customer name"),
    help_text = ("String name"),
    max_length = 255,
  )

  email = models.CharField(
    verbose_name = ("Customer email"),
    help_text = ("String email"),
    max_length = 255,
  )

  profile_image = models.CharField(
    verbose_name = ("Customer profile Image"),
    help_text = ("String url of image"),
    max_length = 255,
  )

  # orders -> Foreign 
  # user_scan -> Foreign 

class Rating(models.Model):
  id = models.AutoField(
    verbose_name = ('rating id'),
    help_text = ('auto increment, int id'),
    unique = True,
    primary_key = True,
  )

  rating = models.DecimalField(
    verbose_name =('rating_value'),
    help_text = ('decimal valued rating'),
    max_digits = 10,
    decimal_places = 3  
  )

  created_at = models.DateTimeField(
    verbose_name =('date created_at'),
    help_text = ('time stamp value'),
    auto_now_add=True, 
  )

  rating_from = models.ForeignKey(
    Customer,
    related_name="rating_from",
    on_delete=models.CASCADE,
    verbose_name=("Customer")
  )

  rating_to = models.ForeignKey(
    Provider,
    related_name = "ratings",
    on_delete = models.CASCADE,
    verbose_name=('Provider')
  )

class FoodCategory(models.Model):
  id = models.AutoField(
    verbose_name = ('FoodCategory id'),
    help_text = ('auto increment, int id'),
    unique = True,
    primary_key = True,
  )
  
  c_name = models.CharField(
    verbose_name = ("Category Name"),
    help_text = ("Required"),
    max_length = 300,
  )

  image_id = models.URLField(
    verbose_name = ("Food Image Url"),
    help_text=("https://my_image.png"),
    max_length=500
  )
  
  provider = models.ForeignKey(
    Provider,
    related_name="food_categories",
    on_delete=models.CASCADE,
    verbose_name=("provider"),
  )

class Menu(models.Model):
  id = models.AutoField(
    verbose_name = ('Menu id'),
    help_text = ('auto increment, int id'),
    unique = True,
    primary_key = True,
  )

  name = models.CharField(
    verbose_name = ("Menu item name"),
    help_text = ("Required"),
    max_length = 100,
  )

  price = models.DecimalField(
    verbose_name = ("Menu Item price"),
    help_text = ("Decimal Digit"),
    max_digits = 10,
    decimal_places = 3 
  )

  image_url = models.CharField(
    verbose_name = ("Menu Image"),
    help_text = ("String url of image"),
    max_length = 255,
  )

  foodCategory = models.ForeignKey(
    FoodCategory,
    related_name = "menus",
    on_delete = models.CASCADE,
    verbose_name = ('Food Category')
  )

class Comment(models.Model):
  id = models.AutoField(
    verbose_name = ('Comment id'),
    help_text = ('auto increment, int id'),
    unique = True,
    primary_key = True,
  )

  comment_from = models.ForeignKey( 
      Customer,
      related_name="comment_comment_from",
      on_delete= models.CASCADE,
      verbose_name=("Comment customer"), 
  )

  comment_to = models.ForeignKey( 
      Provider,
      related_name="comments",
      on_delete=models.CASCADE,
      verbose_name=("Comment Hotel"), 
  )
  
  content = models.TextField(
    verbose_name= "Comment conent",
  )

  created_at = models.DateTimeField(
    verbose_name=("Commented at"),
    auto_now_add=True,
    editable = False
  )

class Order(models.Model):
  id = models.AutoField(
    verbose_name = ('Order id'),
    help_text = ('auto increment, int id'),
    unique = True,
    primary_key = True,
  )

  food_name = models.CharField(
    verbose_name = ("food name "),
    help_text = ("Not Required"),
    unique = False,
    max_length = 255,
  )

  food_count = models.IntegerField(
    verbose_name = ("food count "),
    help_text = ("Not Required"),
  )

  order_from = models.ForeignKey( 
      Customer,
      related_name="customer_order",
      on_delete=models.CASCADE,
      verbose_name=("Order from"), 
  )

  order_to = models.ForeignKey( 
      Provider,
      related_name= "provider_order",
      on_delete=models.CASCADE,
      verbose_name=("Order to"), 
  )

  order_date_time  = models.DateTimeField(
    verbose_name=("Ordered at"),
    auto_now_add=True,
    editable = False
  )

  order_status = models.CharField(
    verbose_name = ('Order Status'),
    help_text = ('Canceled, approved ... '),
    max_length = 255 
  )

  order_cost = models.DecimalField(
    verbose_name = ('Order cost'),
    help_text = ('Total cost of order'),
    max_digits = 10,
    decimal_places = 3 
  )

class UserScan(models.Model):
  id = models.AutoField(
    verbose_name = ("UserScan id "),
    help_text = ("Auto increment int"),
    unique = True,
    primary_key = True,
  )

  scan_url = models.CharField(
    verbose_name = ("Scanned Url"),
    help_text=("https://myhotel.com/tara_hotel/account"),
    max_length=255
  )

  date_time = models.DateTimeField(
    verbose_name=("Scanned at"),
    auto_now_add=True,
    editable = False
  )

  customer_id = models.ForeignKey( 
      Customer,
      related_name="user_scan",
      on_delete=models.CASCADE,
      verbose_name=("Scanned customer"), 
  )
