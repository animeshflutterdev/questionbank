from django.db import models
from question_bank_api.models.questionbank_model import QuestionBank

#
# from .base_model.base_model import QuestionBankBaseModel
# from question_bank_api.models.questionbank_model import QuestionBank
#
#
# class QuestionOption(QuestionBankBaseModel):
#     question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
#     option = models.CharField(max_length=255, default='')
#     isCorrect = models.BooleanField(default=False, null=False, blank=False)
#
#     def __str__(self):
#         return self.option


class QuestionOption(models.Model):
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    option = models.CharField(max_length=255, default='')
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.option
