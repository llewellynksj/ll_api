from django.db.models import Count
from rest_framework import generics, filters
from .models import Account
from .serializers import AccountSerializer
from ll_api.permissions import IsOwnerOrReadOnly

class AccountList(generics.ListAPIView):
    """
    Lists all accounts belonging to registered users
    """
    queryset = Account.objects.annotate(
        leaf_count=Count('user__leaf', distinct=True),
    ).order_by('-created_at')
    serializer_class = AccountSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'leaf_count']
    

class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update account details
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AccountSerializer
    queryset = Account.objects.annotate(
        leaf_count=Count('user__leaf', distinct=True),
    ).order_by('-created_at')