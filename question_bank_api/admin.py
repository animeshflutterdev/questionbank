from django.contrib import admin

from question_bank_api.models.level_model import QuestionLevel
from question_bank_api.models.question_options_model import QuestionOption
from question_bank_api.models.questionbank_model import QuestionBank


admin.site.register(QuestionBank)
admin.site.register(QuestionOption)
admin.site.register(QuestionLevel)
