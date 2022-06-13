from django.urls import path
from user.views import CreateUserView, CreateTokenView, ManageUserView, \
    SystemUsersViewSet

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
    # Superuser route
    path('list/', SystemUsersViewSet.as_view({'get': 'list'}), name='list')
]
