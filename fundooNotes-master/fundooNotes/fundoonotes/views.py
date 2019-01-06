from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from fundoonotes.models import Notes
from fundoonotes.permissions import UserIsOwnerFundooNotes
from fundoonotes.serializers import FundooNotesSerializer


class FundooNotesListCreateAPIView(ListCreateAPIView):
    serializer_class = FundooNotesSerializer

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FundooNotesDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FundooNotesSerializer
    queryset = Notes.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerFundooNotes)
