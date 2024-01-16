import webbrowser

from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from amour_link.models import Form
from amour_link.paginators import FormPaginator
from amour_link.permissions import IsOwner
from amour_link.serializers import FormSerializer
from rest_framework.response import Response


class FormCreateAPIView(generics.CreateAPIView):
    serializer_class = FormSerializer

    def perform_create(self, serializer):
        new_form = serializer.save()
        new_form.save()


class FormListAPIView(generics.ListAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    pagination_class = FormPaginator


class FormRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()


class FormUpdateAPIView(generics.UpdateAPIView):

    serializer_class = FormSerializer
    queryset = Form.objects.all()
    permission_classes = [IsOwner]


class FormDestroyAPIView(generics.DestroyAPIView):
    """ Destroy Lesson """
    queryset = Form.objects.all()
    permission_classes = [IsOwner]