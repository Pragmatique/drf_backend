from django.conf.urls import url, include
from rest_framework import routers
from .views import ShopViewSet, ShopItemViewSet, ShopClientViewSet

# from allauth.account.views import confirm_email

router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'shop-items', ShopItemViewSet)
router.register(r'shop-clients', ShopClientViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]