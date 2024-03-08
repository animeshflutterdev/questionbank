from typing import List, Optional

from django.db import models


from question_bank_api.models.base_model.base_model import QuestionBankBaseModel
from question_bank_api.models.options import Options
from django.utils import timezone


# class QuestionBank(QuestionBankBaseModel):
#     question: str
#     level: Optional[str] = None
#     point: Optional[float] = None
#     image: Optional[str] = None
#     options: List[Options]
#     answer: str
#     isActive: bool
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def __str__(self):
#         return self.question
#
#     def save(self, *args, **kwargs):
#         self.expiration_time = timezone.now() + timezone.timedelta(minutes=15)
#         super().save(*args, **kwargs)

class QuestionBank(QuestionBankBaseModel):
    question: models.CharField(max_length=1000,null=False, blank=False)
    level: models.CharField(max_length=10)
    point: models.FloatField(default=0.0)
    image: models.ImageField(
        upload_to="images/questionImage/"
    )
    # options: models.Li
    answer: models.CharField(max_length=100)
    isActive: models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

