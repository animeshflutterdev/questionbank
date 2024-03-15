from django.db import models

from question_bank_api.models.base_model.base_model import QuestionBankBaseModel


# from .questionbank_model import QuestionBank


# class QuestionLevel(QuestionBankBaseModel):
#     question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
#     level = models.CharField(max_length=10, null=False, blank=False)
#
#     def __str__(self):
#         return self.level


class QuestionLevel(QuestionBankBaseModel):
    LEVEL_CHOICES = (
        ('1', 'Easy'),
        ('2', 'Medium'),
        ('3', 'Hard'),
    )
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)

    # question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_level_display()
