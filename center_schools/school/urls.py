from django.urls import path, include
from rest_framework import routers

from school import views

router = routers.DefaultRouter()
# Routes for logged in user
router.register('members', views.MembersViewSet, basename='person')

app_name = 'school'

urlpatterns = [
    path('', include(router.urls)),
]
