from users.models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# class ProfileViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#        queryset = Profile.objects.all()
#        serializer = ProfileSerializer(queryset, many=True)
#        return Response(serializer.data)
#


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('id').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)




