from django.urls import path, include
from rest_framework import routers

from school import views

router = routers.DefaultRouter()
# NO FUNCA
# router.register(r'members', views.PersonViewSet)
# router.register(r'profile', views.UserProfileViewSet, basename='User')

# # Routes for superusers
# router.register('members', views.PersonViewSet, basename='person')
# # Routes for logged in user
# router.register('user/profiles', views.UserProfileViewSet,
#                 basename='person')

# Routes for logged in user
router.register('members', views.MembersViewSet,
                basename='person')

app_name = 'school'

urlpatterns = [
    path('', include(router.urls)),
    path('user/profile', views.ManageUserProfileView.as_view(), name='profile')
    # NO FUNCA
    # path(r'^members/$', views.members, name='members'),
    # path(r'^profile/(?P<pk>[0-9]+)$', views.profile, name='profile'),
]
