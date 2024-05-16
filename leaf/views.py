from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Leaf
from .serializers import LeafSerializer


class LeafList(APIView):
  serializer_class = LeafSerializer
  permission_classes = [
    permissions.IsAuthenticatedOrReadOnly
  ]

  def get(self, request):
    leaves = Leaf.objects.all()
    serializer = LeafSerializer(leaves, many=True, context={'request': request})
    return Response(serializer.data)

  def post(self, request):
    serializer = LeafSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)