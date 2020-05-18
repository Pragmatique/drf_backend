from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductViewSet

# from allauth.account.views import confirm_email

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]