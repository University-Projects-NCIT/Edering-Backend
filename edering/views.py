from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.generics import ListAPIView 
from django.views.generic import TemplateView
from datetime import date
from datetime import datetime
from django.db.models import Q

from .serializers import(
  ProviderSerializer,
  CustomerSerializer,
  FoodCategorySerializer,
  MenuSerializer,
  OrderSerializer,
  CommentSerializer,
  UserScanSerializer,
  RatingSerializer
)

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

class HomePageView(TemplateView):
  template_name = "index.html"

class ProviderViewSet(viewsets.ModelViewSet):
  serializer_class = ProviderSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point providers
    providers/?id=jskdfhjkdsg
    """
    query_set = Provider.objects.all()
    hotel_id = self.request.query_params.get('id')
    # search_fields = ['$name','$location','$known_for']
    search_key = self.request.query_params.get('search')

    if(search_key is not None):
      query_set = query_set.filter(
        Q(name__icontains= search_key) or
        Q(location__icontains= search_key)
      )

    if(hotel_id is not None):
      query_set = query_set.filter(id = hotel_id)
    return query_set
  

class CustomerViewSet(viewsets.ModelViewSet):
  serializer_class = CustomerSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point customer/id=skjdhgsd454
    """
    query_set = Customer.objects.all()
    customer_id = self.request.query_params.get('id')
    
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
    provider_id = self.request.query_params.get('provider_id')
    search_key = self.request.query_params.get('search')

    if(search_key is not None):
      query_set = query_set.filter(
        Q(c_name__icontains= search_key) 
      )

    if(provider_id is not None):
      query_set = query_set.filter(provider = provider_id)

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
    search_key = self.request.query_params.get('search')

    if(search_key is not None):
      query_set = query_set.filter(
        Q(name__icontains= search_key) 
      )
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
    provider_id = self.request.query_params.get('provider_id')
    customer_id = self.request.query_params.get('customer_id')
    
    if( provider_id is not None):
      query_set = query_set.filter(order_to = provider_id)

    if( customer_id is not None):
      query_set = query_set.filter(order_from = customer_id)  

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
    provider_id = self.request.query_params.get('provider_id')

    if(provider_id is not None):
      query_set = query_set.filter(comment_to = provider_id)

    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set 


class RatingViewSet(viewsets.ModelViewSet):
  serializer_class = RatingSerializer
  permission_classes = [permissions.AllowAny]

  def get_queryset(self):
    """
    end point rating/id=skjdhgsd454
    """
    query_set = Rating.objects.all()
    id = self.request.query_params.get('id')
    provider_id = self.request.query_params.get('provider_id')

    if(provider_id is not None):
      query_set = query_set.filter(to_id = provider_id)

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
    customer_id = self.request.query_params.get('customer_id')

    if(customer_id is not None):
      query_set = query_set.filter(customer_id = customer_id)

    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set 
