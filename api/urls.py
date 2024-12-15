from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSet

router = DefaultRouter()
router.register(r'products', ViewSet)
urlpatterns = [
	path("", include(router.urls))
]