from django.db import models

from question_bank_api.models.base_model.base_model import QuestionBankBaseModel


#
# from question_bank_api.models.base_model.base_model import QuestionBankBaseModel
# from question_bank_api.models.level_model import QuestionLevel
# from question_bank_api.models.question_options_model import QuestionOption
#
#
# class QuestionBank(QuestionBankBaseModel):
#     question = models.TextField()
#     image = models.CharField(max_length=1000, blank=True, null=True)
#     level = models.ForeignKey(QuestionLevel, on_delete=models.CASCADE, null=True)
#     options = models.ForeignKey(QuestionOption, on_delete=models.CASCADE, null=True)
#     isActive = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.question


class QuestionBank(QuestionBankBaseModel):
    from question_bank_api.models.level_model import QuestionLevel

    question = models.TextField()
    image = models.CharField(max_length=1000, blank=True, null=True)
    level = models.ForeignKey(QuestionLevel, on_delete=models.CASCADE, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.question