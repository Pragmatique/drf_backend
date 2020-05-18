from django.conf.urls import url, include
from rest_framework import routers
from .views import UserPartialUpdateView, UserViewSet, UserCreateView, activate_account

# from allauth.account.views import confirm_email

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^users/register/', UserCreateView.as_view(), name='user_register'),
    url(r'^users/update-partial/(?P<pk>\d+)/', UserPartialUpdateView.as_view(), name='user_partial_update'),
    url(r'^users/mail-verification/(?P<pk>\d+)/', activate_account, name='mail_verification'),
]