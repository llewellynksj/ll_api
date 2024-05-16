from rest_framework import generics, permissions
from ll_api.permissions import IsOwnerOrReadOnly
from .models import Remember
from .serializers import RememberSerializer


class RememberList(generics.ListCreateAPIView):
    """
    List all Remember instances or create a new Remember instance
    """
    queryset = Remember.objects.all()
    serializer_class = RememberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RememberDetail(generics.RetrieveDestroyAPIView):
    """
    Detail view allows all users to see Remember instances
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RememberSerializer
    queryset = Remember.objects.all()