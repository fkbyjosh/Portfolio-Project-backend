from django.urls import path
from . import views
from .views import PolicyList

urlpatterns = [
    path('policies/', views.PolicyList.as_view(), name='policy_list'),
    path('policies/<int:policy_num>/', views.PolicyUpdate.as_view(), name='policy_update'),
    path('policies/', views.NewPolicy.as_view(), name='new_policy'),
    path('policies/<int:policy_num>/', views.PolicyDelete.as_view(), name='policy_delete'),
    path('policies/<int:policy_num>/', views.PolicyList.as_view(), name='retrieve_policy')
]
