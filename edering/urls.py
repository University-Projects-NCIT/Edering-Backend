from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls import path, include
from .views import(
  HomePageView,
  ProviderViewSet,
  CustomerViewSet,
  FoodCategoryViewSet,
  MenuViewSet,
  OrderViewSet,
  CommentViewSet,
  UserScanViewSet,
  RatingViewSet
)

router = DefaultRouter()

router.register(f'providers',ProviderViewSet, 'Hotel')
router.register(f'customers',CustomerViewSet, 'Customer')
router.register(f'food_categories',FoodCategoryViewSet, 'FoodCategory')
router.register(f'menus',MenuViewSet, 'Menu')
router.register(f'orders',OrderViewSet, 'Order')
router.register(f'comments',CommentViewSet, 'Comment')
router.register(f'user_scans',UserScanViewSet, 'UserScan')
router.register(f'ratings',RatingViewSet, 'Rating')

urlpatterns = [
    path('', HomePageView.as_view()),
    path('', include(router.urls)),
]