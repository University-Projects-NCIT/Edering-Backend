from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.generics import ListAPIView 
from django.views.generic import TemplateView
from datetime import date
from datetime import datetime
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response

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

  def create(self, request, *args, **kwargs):
    prvId = request.data.get('provider')
    provider = Provider.objects.filter(id = prvId)[0]

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(provider = provider)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
  
  def create(self, request, *args, **kwargs):
    foodCategoryId = request.data.get('foodCategory')
    provider = FoodCategory.objects.filter(id = foodCategoryId)[0]

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(foodCategory = provider)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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

  def create(self, request, *args, **kwargs):
    order_from_id = request.data.get('order_from')
    order_to_id = request.data.get('order_to')
    customer = Customer.objects.filter(id = order_from_id)[0]
    provider = Provider.objects.filter(id = order_to_id)[0]

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(order_from= customer, order_to= provider)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
  
  def create(self, request, *args, **kwargs):
    comment_from = request.data.get('comment_from')
    comment_to = request.data.get('comment_to')
    customer = Customer.objects.filter(id = comment_from)[0]
    provider = Provider.objects.filter(id = comment_to)[0]

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(comment_from = customer, comment_to = provider)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
      query_set = query_set.filter(rating_to = provider_id)

    if(id is not None):
      query_set = query_set.filter(id = id)
    return query_set 

  def create(self, request, *args, **kwargs):
    # import pdb;
    # pdb.set_trace()
    rating_from = request.data.get('rating_from')
    rating_to = request.data.get('rating_to')
    customer = Customer.objects.filter(id = rating_from)[0]
    provider = Provider.objects.filter(id = rating_to)[0]

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # self.perform_create(serializer)
    serializer.save(rating_from = customer, rating_to = provider)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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

  def create(self, request, *args, **kwargs):
    customerId = request.data.get('customer_id')
    customer = Customer.objects.filter(id = customerId)[0]

    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(customer_id = customer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
