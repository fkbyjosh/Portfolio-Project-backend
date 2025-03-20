from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics  # Add this for DRF
from .models import Policy
from .serializers import PolicySerializer

# Function-based view for /policies/
@login_required
def policy_list(request):
    policies = Policy.objects.all()
    return render(request, 'policies/policy_list.html', {'policies': policies})

# DRF class-based view for /policies/api/policies/
class PolicyList(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
