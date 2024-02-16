from rest_framework import generics, permissions
from drf_fanzone.permissions import IsOwnerOrReadOnly
from .models import TeamsList
from .serializers import TeamsListSerializer


class TeamsListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TeamsList.objects.all()
    serializer_class = TeamsListSerializer

    def perform_create(self, serializer):
        serializer.save(team=self.request.user)
