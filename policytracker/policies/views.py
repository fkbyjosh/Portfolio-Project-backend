from rest_framework import generics  # Add this for DRF
from .models import Policy
from .serializers import PolicySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PolicySerializer

# List of all policies
class PolicyList(APIView):
    def get(self, request):
        policy = [policy.policy_num for policy in Policy.objects.all()]
        return Response(policy)

#Update policies
class PolicyUpdate(APIView):
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
            )            data = request.data                                                  
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

#Create a policy
class NewPolicy(APIView):
    def post(self, request):
        try:
            policy = Policy(
                policy_num=data.get('policy_num'),
                policy_holder=data.get('policy_holder'),
                policy_type=data.get('policy_type'),
                payment_mode=data.get('payment_mode'),
                status=data.get('status', 'Pending'),  # Default value example
                branch=data.get('branch'),
                premium=data.get('premium', 0.0)  # Default value example
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

#Delete a policy
class PolicyDelete(APIView):
    def delete(self, request, policy_num):
        try:
            # Get the policy to delete
            policy = Policy.objects.get(policy_num=policy_num)
            policy.delete()

            return Response(
                {'message': f'Policy {policy_num} deleted successfully'},
                status=status.HTTP_204_NO_CONTENT)
