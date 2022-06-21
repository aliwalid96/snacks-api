from django.urls import path
from snacks.api.viewsets import SnackListAPIView,SnackDetailAPIView

urlpatterns = [
    path('api/v1/snacks-list',SnackListAPIView.as_view(),name='snacks_list'),
    path('api/v1/<int:pk>',SnackDetailAPIView.as_view(),name='snack_detail'),

]