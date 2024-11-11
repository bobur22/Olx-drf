from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'color', ColorViewSet)
router.register(r'job', JobsViewset)
router.register(r'size', SizeViewSet)
router.register(r'variants', VariantsViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls