from asyncore import read
from pyexpat import model
from rest_framework import serializers 
from .models import(
  Hotel,
  Customer,
  FoodCategory,
  Menu,
  Order,
  Comment,
  UserScan
)

class HotelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hotel
    fields = ["id","name","location","image_uri_id", "known_for","rating","open_time","close_time"]

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    modal = Customer 
    fiels = ["id","auth_id"]

class FoodCategorySerializer(serializers.ModelSerializer):
  class Meta:
    modal = FoodCategory
    fields =["id","c_name","image_uri_id"]

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    modal = Menu
    fields =["id","category","name", "price"]

class OrderSerializer(serializers.ModelSerializer):
  order_from = CustomerSerializer(many = True, read_only = True)
  order_to = HotelSerializer(many = True, read_only = True)
  food = MenuSerializer(many = True, read_only = True)
  class Meta:
    modal = Order
    fields =["id","order_from","order_to","order_date_time","food","delivered_status"]

class CommentSerializer(serializers.ModelSerializer):
  comment_from = CustomerSerializer(many = True, read_only = True)
  comment_to = HotelSerializer(many = True, read_only = True)
  class Meta:
    modal = Comment
    fields =["id","comment_from","comment_to","content","date_time"]

class UserScanSerializer(serializers.ModelSerializer):
  user_id = CustomerSerializer(many = True, read_only = True)
  class Meta:
    modal = UserScan
    fields =["id","scan_url","date_time","user_id"]