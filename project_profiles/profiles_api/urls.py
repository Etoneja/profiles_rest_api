from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register(
    "hello_viewset",
    viewset=views.HelloViewSet,
    basename="hello_viewset"
)
router.register(
    "user_profile",
    viewset=views.UserProfileViewSet
)


urlpatterns = [
    path("hello/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
