from django.contrib import admin

from .models import(
  Hotel,
  Customer,
  FoodCategory,
  Menu,
  Order,
  Comment,
  UserScan
)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "name",
      "location",
      "image_uri_id",
      "known_for",
      "rating",
      "open_time",
      "close_time"
    ]
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "auth_id"
    ]

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "c_name",
      "image_uri_id"
    ]
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "category",
      "name",
      "price"
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "order_from",
      "order_to",
      "order_date_time",
      "food",
      "delivered_status"
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "comment_from",
      "comment_to",
      "content",
      "date_time"
    ]

@admin.register(UserScan)
class UserScanAdmin(admin.ModelAdmin):
    list_display = [
      "id",
      "scan_url",
      "date_time",
      "user_id"
    ]