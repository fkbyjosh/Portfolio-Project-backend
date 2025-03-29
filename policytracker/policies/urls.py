from django.urls import path
from . import views

urlpatterns = [
    # Update policy(PUT)
    path('policies/<str:policy_num>/', views.PolicyDetails.as_view(), name='policy_update'),
    
    # Create new policy(POST)
    path('policies/', views.PolicyList.as_view(), name='new_policy')
]