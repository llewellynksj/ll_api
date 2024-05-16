from rest_framework import generics, permissions
from .models import Leaf
from .serializers import LeafSerializer
from ll_api.permissions import IsOwnerOrReadOnly


class LeafList(generics.ListCreateAPIView):
  """

  """
  queryset = Leaf.objects.all()
  serializer_class = LeafSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)



class LeafDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update, or delete a leaf instance
  """
  queryset = Leaf.objects.all()
  serializer_class = LeafSerializer
  permission_classes = [
    IsOwnerOrReadOnly
  ]