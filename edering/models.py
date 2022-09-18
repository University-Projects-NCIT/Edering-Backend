from django.db import models

class Hotel(models.Model):
  id = models.CharField(
    verbose_name = ("hotel id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )

  name = models.CharField(
    verbose_name=("hotel name"),
    help_text=(" Required "),
    max_length= 300,
    unique= False 
  )

  location = models.CharField(
    verbose_name=("hotel location"),
    help_text=(" Required , (lat, lng) "),
    max_length= 100,
    unique= False 
  )

  image_uri_id = models.URLField(
      verbose_name = ("Hotel Profile Image Url"),
      help_text=("https://my_image.png"),
      max_length=500
  )

  known_for = models.CharField(
    verbose_name=("famous food "),
    help_text=(" Not Required"),
    max_length= 100,
    unique= False 
  )

  rating = models.FloatField(
    verbose_name=("Hotel Rating"),
    help_text=("4.5"),
  )

  open_time = models.CharField(
    verbose_name=("Hotel open time "),
    help_text=("10:00 AM"),
    max_length= 100,
    unique= False 
  )

  close_time = models.CharField(
    verbose_name=("Hotel close time "),
    help_text=("10:00 PM"),
    max_length= 100,
    unique= False 
  )

  account_create = models.CharField(
    verbose_name=("Account created timestamp"),
    help_text= ("Timesamp take default timestamp"),
    max_length= 300 
  )

class Customer(models.Model):
  id = models.CharField(
    verbose_name = ("Customer id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )

  auth_id = models.CharField(
    verbose_name = ("Firebase auth id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
  )

class FoodCategory(models.Model):
  id = models.CharField(
    verbose_name = ("FoodCategory id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )
  c_name = models.CharField(
    verbose_name = ("Category Name"),
    help_text = ("Required"),
    max_length = 300,
  )

  image_uri_id = models.URLField(
    verbose_name = ("Food Image Url"),
    help_text=("https://my_image.png"),
    max_length=500
  )

class Menu(models.Model):
  id = models.CharField(
    verbose_name = ("Menu id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )

  category = models.ForeignKey( 
      FoodCategory,
      related_name="menu",
      on_delete=models.CASCADE,
      verbose_name=("Food Category id"), 
  )

  name = models.CharField(
    verbose_name = ("Menu item name"),
    help_text = ("Required"),
    max_length = 100,
  )

  price = models.CharField(
    verbose_name = ("Menu Item price"),
    help_text = ("Required and Unique"),
    max_length = 100,
  )

class Comment(models.Model):
  id = models.CharField(
    verbose_name = ("Comment Id"),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )
  comment_from = models.ForeignKey( 
      Customer,
      related_name="comment_comment_from",
      on_delete=models.CASCADE,
      verbose_name=("Comment customer"), 
  )

  comment_to = models.ForeignKey( 
      Hotel,
      related_name="comment_comment_to",
      on_delete=models.CASCADE,
      verbose_name=("Comment Hotel"), 
  )
  
  content = models.TextField(
    verbose_name= "Comment conent",
  )

  date_time = models.DateTimeField(
    verbose_name=("Commented at"),
    auto_now_add=True,
    editable = False
  )

class Order(models.Model):
  id = models.CharField(
    verbose_name = ("order id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )

  order_from = models.ForeignKey( 
      Customer,
      related_name="customer_id",
      on_delete=models.CASCADE,
      verbose_name=("Ordered customer"), 
  )

  order_to = models.ForeignKey( 
      Hotel,
      related_name= "hotel_id",
      on_delete=models.CASCADE,
      verbose_name=("Ordered Hotel"), 
  )

  order_date_time  = models.DateTimeField(
    verbose_name=("Ordered at"),
    auto_now_add=True,
    editable = False
  )

  # food = models.ForeignKey( 
  #     Menu,
  #     related_name="menu_id",
  #     on_delete=models.CASCADE,
  #     verbose_name=("Ordered food item"), 
  # )

  delivered_status = models.BooleanField(
    verbose_name=("Served status"),
    help_text=("True"),
    default= False,
  )

class UserScan(models.Model):
  id = models.CharField(
    verbose_name = ("UserScan id "),
    help_text = ("Required and Unique"),
    unique = True,
    max_length = 100,
    primary_key = True,
  )
  scan_url = models.URLField(
    verbose_name = ("Scanned Url"),
    help_text=("https://myhotel.com/tara_hotel/account"),
    max_length=500
  )

  date_time = models.DateTimeField(
    verbose_name=("Scanned at"),
    auto_now_add=True,
    editable = False
  )
  user_id = models.ForeignKey( 
      Customer,
      related_name="userscan_user_id",
      on_delete=models.CASCADE,
      verbose_name=("Scanned customer"), 
  )
