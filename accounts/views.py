from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from ll_api.permissions import IsOwnerOrReadOnly

class AccountList(generics.ListAPIView):
    """
    Lists all accounts belonging to registered users
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    

class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update account details
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()