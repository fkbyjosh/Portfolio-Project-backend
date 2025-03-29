from rest_framework import status 
from .models import Policy
from .serializers import PolicySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

# List of all policies
 
class PolicyList(APIView):
    def post(self, request):
        try:
            data = request.data
            policy = Policy(
                policy_num=data.get('policy_num'),
                policy_holder=data.get('policy_holder'),
                policy_type=data.get('policy_type'),
                payment_mode=data.get('payment_mode'),
                status=data.get('status', 'Pending'),
                branch=data.get('branch'),
                premium=data.get('premium', 0.00)
            )
            policy.save()

            return Response({
                'policy_num': policy.policy_num,
                'policy_holder': policy.policy_holder,
                'policy_type': policy.policy_type,
                'payment_mode': policy.payment_mode,
                'status': policy.status,
                'branch': policy.branch,
                'premium': policy.premium
            }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    def get(self, request):
        policy = [policy.policy_num for policy in Policy.objects.all()]
        return Response(policy)

# Update policies
class PolicyDetails(APIView):
    def put(self, request, policy_num):
        try:
            policy = Policy.objects.get(policy_num=policy_num)

            data = request.data
            policy.policy_num = data.get('policy_num', policy.policy_num)
            policy.policy_holder = data.get('policy_holder', policy.policy_holder)
            policy.policy_type = data.get('policy_type', policy.policy_type)
            policy.payment_mode = data.get('payment_mode', policy.payment_mode)
            policy.status = data.get('status', policy.status)
            policy.branch = data.get('branch', policy.branch)
            policy.premium = data.get('premium', policy.premium)

            policy.save()

            return Response({
                'policy_num': policy.policy_num,
                'policy_holder': policy.policy_holder,
                'policy_type': policy.policy_type,
                'payment_mode': policy.payment_mode,
                'status': policy.status,
                'branch': policy.branch,
                'premium': policy.premium
                }, status=status.HTTP_200_OK)

        except Policy.DoesNotExist:
            return Response(
            {'error': 'Policy not found'},
            status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
            )
   
    def delete(self, request, policy_num): 
        try:
            policy = Policy.objects.get(policy_num=policy_num)
            policy.delete()

            return Response(
                {'message': f'Policy {policy_num} deleted successfully'},
                status=status.HTTP_204_NO_CONTENT)
        except Policy.DoesNotExist:
            return Response(
                {'error': 'Policy not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    def patch(self, request, policy_num):
        try:
            policy = Policy.objects.get(policy_num=policy_num)
            data = request.data
            
            if 'policy_holder' in data:
                policy.policy_holder = data['policy_holder']
            if 'policy_type' in data:
                policy.policy_type = data['policy_type']
            if 'payment_mode' in data:
                policy.payment_mode = data['payment_mode']
            if 'status' in data:
                policy.status = data['status']
            if 'branch' in data:
                policy.branch = data['branch']
            if 'premium' in data:
                policy.premium = data['premium']
                
            policy.save()
            
            return Response({
                'policy_num': policy.policy_num,
                'policy_holder': policy.policy_holder,
                'policy_type': policy.policy_type,
                'payment_mode': policy.payment_mode,
                'status': policy.status,
                'branch': policy.branch,
                'premium': policy.premium
            }, status=status.HTTP_200_OK)
            
        except Policy.DoesNotExist:
            return Response(
                {'error': 'Policy not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
#Sign Up View
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not username or not email or not password:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)