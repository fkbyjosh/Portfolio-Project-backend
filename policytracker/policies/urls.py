from django.urls import path
from . import views
from .views import PolicyList

urlpatterns = [
    path('', views.policy_list, name='policy_list'),
    path('api/policies/', PolicyList.as_view(), name='policy_list_api'),
]
