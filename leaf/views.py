from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Leaf
from .serializers import LeafSerializer
from ll_api.permissions import IsOwnerOrReadOnly


class LeafList(generics.ListCreateAPIView):
  """

  """
  queryset = Leaf.objects.annotate(
    remember_count=Count('remembered', distinct=True),
  ).order_by('-created_at')
  serializer_class = LeafSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]
  filter_backends = [filters.OrderingFilter, filters.SearchFilter]
  ordering_fields = ['created_at', 'remember_count']
  search_fields = ['name', 'memory', 'user', 'due_date']
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)



class LeafDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update, or delete a leaf instance
  """
  queryset = Leaf.objects.annotate(
    remember_count=Count('remembered', distinct=True),
  ).order_by('-created_at')
  serializer_class = LeafSerializer
  permission_classes = [
    IsOwnerOrReadOnly
  ]