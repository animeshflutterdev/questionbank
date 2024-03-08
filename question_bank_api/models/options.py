from question_bank_api.models.base_model.base_model import QuestionBankBaseModel


class Options(QuestionBankBaseModel):
    option: str

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def __str__(self):
        return self.option
