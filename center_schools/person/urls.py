from django.urls import path, include
from rest_framework.routers import DefaultRouter

from person import views

router = DefaultRouter()
router.register('person-list', views.PersonViewSet)
# router.register('person-detail', views.PersonViewSet)

app_name = 'person'

urlpatterns = [
    path('', include(router.urls))
]
