from rest_framework import serializers

from question_bank_api.models.questionbank_model import QuestionBank


class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = "__all__"
