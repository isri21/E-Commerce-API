from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'products', ViewSet)
urlpatterns = [
	path("", include(router.urls)),
	path("login/", obtain_auth_token),
]