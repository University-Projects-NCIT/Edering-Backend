from asyncore import read
from pyexpat import model
from rest_framework import serializers 
from .models import(
  Provider,
  Customer,
  Rating,
  FoodCategory,
  Menu,
  Order,
  Comment,
  UserScan
)

class UserScanSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserScan
    fields ='__all__'
    depth = 2 

class OrderSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Order
    fields = '__all__'
    depth = 2 
    
class CustomerSerializer(serializers.ModelSerializer):
  customer_order = OrderSerializer(many = True, read_only = True)
  user_scan = UserScanSerializer(many = True, read_only = True)

  class Meta:
    model = Customer 
    fields = ['id','customer_order','user_scan']
    depth = 2 

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ['id','name','price']
    depth = 2 

class FoodCategorySerializer(serializers.ModelSerializer):
  menus = MenuSerializer(many = True, read_only = True)
  class Meta:
    model = FoodCategory
    fields = ['id','c_name','image_id','provider','menus']

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__' 
    depth = 2 

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = '__all__'
    depth = 2 

class ProviderSerializer(serializers.ModelSerializer):
  food_categories = FoodCategorySerializer(many = True,read_only=True)
  ratings = RatingSerializer(many = True, read_only = True)
  comments = CommentSerializer(many = True, read_only = True)
  provider_order = OrderSerializer(many = True, read_only = True)
  
  class Meta:
    model = Provider
    fields = ['id','name','location','image_id','known_for','open_time','close_time','created_at','food_categories','comments','ratings','provider_order']
    depth = 2 