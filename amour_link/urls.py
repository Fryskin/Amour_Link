from rest_framework import routers
from django.urls import path
from amour_link.apps import AmourLinkConfig

from amour_link.views import FormListAPIView, FormDestroyAPIView, FormUpdateAPIView, FormRetrieveAPIView,\
    FormCreateAPIView

app_name = AmourLinkConfig.name
router = routers.DefaultRouter()


urlpatterns = [
    path('form/', FormListAPIView.as_view(), name='form_list'),
    path('form/create/', FormCreateAPIView.as_view(), name='form_create'),
    path('form/<int:pk>', FormRetrieveAPIView.as_view(), name='form_view'),
    path('form/update/<int:pk>', FormUpdateAPIView.as_view(), name='form_update'),
    path('form/delete/<int:pk>', FormDestroyAPIView.as_view(), name='form_list')


]