from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.generics import ListAPIView 
from django.views.generic import TemplateView
from datetime import date
from datetime import datetime
from django.db.models import Q

from .serializers import(
  HotelSerializer,
  CustomerSerializer,
  FoodCategorySerializer,
  MenuSerializer,
  OrderSerializer,
  CommentSerializer,
  UserScanSerializer
)

from .models import(
  Hotel,
  Customer,
  FoodCategory,
  Menu,
  Order,
  Comment,
  UserScan
)

class HomePageView(TemplateView):
  template_name = "index.html"

class HotelViewSet(viewsets.ModelViewSet):
  serializer_class = HotelSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point hotel/hotel_id=skjdhgsd454
    """
    query_set = Hotel.objects.all()
    hotel_id = self.request.query_params.get('hotel_id')
    if(hotel_id is not None):
      query_set = query_set.filter(id = hotel_id)
    return query_set
  

class CustomerViewSet(viewsets.ModelViewSet):
  serializer_class = CustomerSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point customer/customer_id=skjdhgsd454
    """
    query_set = Customer.objects.all()
    customer_id = self.request.query_params.get('customer_id')
    
    if(customer_id is not None):
      query_set = query_set.filter(id = customer_id)
    return query_set

class FoodCategoryViewSet(viewsets.ModelViewSet):
  serializer_class = FoodCategorySerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point food_categories/id=skjdhgsd454
    """
    query_set = FoodCategory.objects.all()
    id = self.request.query_params.get('id')
    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set

class MenuViewSet(viewsets.ModelViewSet):
  serializer_class = MenuSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point menus/id=skjdhgsd454
    """
    query_set = Menu.objects.all()
    id = self.request.query_params.get('id')
    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set  

class OrderViewSet(viewsets.ModelViewSet):
  serializer_class = OrderSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point orders/id=skjdhgsd454
    """
    query_set = Order.objects.all()
    id = self.request.query_params.get('id')
    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set 

class CommentViewSet(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point comments/id=skjdhgsd454
    """
    query_set = Comment.objects.all()
    id = self.request.query_params.get('id')
    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set 

class UserScanViewSet(viewsets.ModelViewSet):
  serializer_class = UserScanSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point user_scans/id=skjdhgsd454
    """
    query_set = UserScan.objects.all()
    id = self.request.query_params.get('id')
    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set 
