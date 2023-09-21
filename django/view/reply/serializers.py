from rest_framework import serializers

from reply.models import Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
