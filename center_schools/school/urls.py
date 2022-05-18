from django.urls import path, include
from rest_framework.routers import DefaultRouter

from school import views

router = DefaultRouter()
router.register('person-list', views.PersonViewSet)
# router.register('person-detail', views.PersonViewSet)

app_name = 'school'

urlpatterns = [
    path('', include(router.urls))
]
