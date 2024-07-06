from rest_framework.serializers import ModelSerializer
from .models import Profile

class ProfileInputSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_internal_value(self, data):
        if self.context and self.context['request'].method == "POST":
            data['user'] = self.context['request'].user.id
        return super().to_internal_value(data)


class ProfileOutputSerilaizer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"