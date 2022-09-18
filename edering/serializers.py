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
    fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer 
    fields = '__all__'

class FoodCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodCategory
    fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = '__all__'
    depth = 2 

class OrderSerializer(serializers.ModelSerializer):
  # customer_id = CustomerSerializer(many = True, read_only = True)
  # hotel_id = HotelSerializer(many = True, read_only = True)
  # menu_id = MenuSerializer(many = True, read_only = True)
  
  class Meta:
    model = Order
    fields = '__all__'

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