import uuid

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from question_bank_api.log_file.logger import Logger
from question_bank_api.models.level_model import QuestionLevel
from question_bank_api.models.questionbank_model import QuestionBank
from question_bank_api.serializers.level_serializer import QuestionLevelSerializer
from question_bank_api.serializers.options_serializer import QuestionOptionSerializer
from question_bank_api.serializers.question_bank_serializer import QuestionBankSerializer


class CreateQuestion(APIView):
    renderer_classes = [JSONRenderer]

    @staticmethod
    def post(request: Request):
        try:
            request_data = request.data
            question = request_data.get("question")
            image = request_data.get("image")
            level = request_data.get("level")
            options = request_data.get("options")

            levelDBData = QuestionLevelSerializer(QuestionLevel.objects.all(), many=True).data
            for levelData in levelDBData:
                if levelData['level'] == level:
                    request_data['level'] = uuid.UUID(levelData['id'])

            # Logger().writeLogFile(log_message=str(level), err_file_name="Level-UUID", )

            questionSerializer = QuestionBankSerializer(data=request_data)
            if question is not None and level is not None and options is not None or image is not None:

                # for option in options:
                #     optionsSerializer = QuestionOptionSerializer(data=request_data)
                #     if optionsSerializer.is_valid():
                #         optionsSerializer.save()

                if questionSerializer.is_valid():
                    questionSerializer.save()

                    questionDBData = QuestionBankSerializer(QuestionBank.objects.all(), many=True).data
                    if questionDBData[-1]['question'] == question:
                        questionID: str = str(questionDBData[-1]['id'])

                return Response(
                    data={
                        "successMessage": "Data added",
                        "data": {"question_id": questionID},
                        "errorMessage": None,
                    },
                    status=status.HTTP_201_CREATED,
                    content_type="application/json",
                )
            else:
                Logger().writeLogFile(log_error_message="Something went wrong !", err_file_name="ValueError", )
                raise ValueError("Something went wrong !")

        except Exception as e:
            Logger().writeLogFile(log_error_message=str(e), err_file_name="Exception", )

            return Response(
                data={
                    "successMessage": None,
                    "errorMessage": f"InternalServerError: {e}",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )
