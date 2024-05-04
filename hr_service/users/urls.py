from django.urls import path

from .views import UserDeleteView, UserListView, UserDetailView, UserCreateView, UserUpdateView, export_excel, import_excel

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:id>/edit/', UserUpdateView.as_view(), name='user-update'),
    path("user/delete/<int:id>", UserDeleteView.as_view(), name="user-delete"),
    path('export/', export_excel, name='export_users'),
    path('import/', import_excel, name='import_users')
]