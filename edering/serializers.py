from asyncore import read
from pyexpat import model
from rest_framework import serializers 
from .models import(
  Provider,
  Customer,
  FoodCategory,
  Menu,
  Order,
  Comment,
  UserScan
)

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer 
    fields = '__all__'
    depth = 2 

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = '__all__'
    depth = 2 

class FoodCategorySerializer(serializers.ModelSerializer):
  menus = MenuSerializer(many = True, read_only = True)
  class Meta:
    model = FoodCategory
    fields = ['id','c_name','image_id','menus']
    depth = 3

class OrderSerializer(serializers.ModelSerializer):
  # customer_id = CustomerSerializer(many = True, read_only = True)
  # hotel_id = HotelSerializer(many = True, read_only = True)
  # menu_id = MenuSerializer(many = True, read_only = True)
  
  class Meta:
    model = Order
    fields = '__all__'
    depth = 2 

class CommentSerializer(serializers.ModelSerializer):
  # comment_from = CustomerSerializer(many = True, read_only = True)
  # comment_to = HotelSerializer(many = True, read_only = True)
  class Meta:
    model = Comment
    # fields =["id","comment_from","comment_to","content","date_time"]
    fields = '__all__' 
    depth = 2 

class UserScanSerializer(serializers.ModelSerializer):
  user_id = CustomerSerializer(many = True, read_only = True)
  class Meta:
    model = UserScan
    fields =["id","scan_url","date_time","user_id"]
    depth = 2 

class ProviderSerializer(serializers.ModelSerializer):
  food_categories = FoodCategorySerializer(many = True,read_only=True)
  
  class Meta:
    model = Provider
    fields = ['id','name','location','image_id','known_for','rating','open_time','close_time','created_at','food_categories']
    depth = 2 