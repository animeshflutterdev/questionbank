from rest_framework import serializers

from question_bank_api.models.level_model import QuestionLevel


class QuestionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionLevel
        fields = "__all__"
