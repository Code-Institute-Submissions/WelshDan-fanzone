from django.db import IntegrityError
from rest_framework import generics, serializers
from drf_fanzone.permissions import IsOwnerOrReadOnly
from .models import TeamsList


class TeamsListSerializer(serializers.ModelSerializer):
    team_choices = serializers.SerializerMethodField()

    class Meta:
        model = TeamsList
        fields = [
            'id', 'team'
        ]
    
    def get_team_choices(self, obj):
        return TeamsList.objects.all()
