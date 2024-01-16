from rest_framework import serializers

from amour_link.models import Form

from amour_link.validators import CountryValidator, NameValidator


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = "__all__"
        validators = [CountryValidator(field='country'), NameValidator(field='name')]