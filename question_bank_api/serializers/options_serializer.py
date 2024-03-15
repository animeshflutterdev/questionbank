from rest_framework import serializers

from question_bank_api.models.question_options_model import QuestionOption


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = "__all__"
