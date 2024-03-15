from django.http import JsonResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


from question_bank_api.models.question_options_model import QuestionOption
from question_bank_api.models.questionbank_model import QuestionBank
from question_bank_api.serializers.level_serializer import QuestionLevelSerializer
from question_bank_api.serializers.options_serializer import QuestionOptionSerializer
from question_bank_api.serializers.question_bank_serializer import QuestionBankSerializer
from ..log_file.logger import Logger
from ..models.level_model import QuestionLevel


class AllQuestions(APIView):
    renderer_classes = [JSONRenderer]

    @staticmethod
    def get(_):
        try:
            all_question = QuestionBank.objects.all()
            all_level = QuestionLevel.objects.all()
            all_option = QuestionOption.objects.all()

            questionDBData = QuestionBankSerializer(all_question, many=True).data
            Logger().warning(questionDBData)

            levelDBData = QuestionLevelSerializer(all_level, many=True).data
            Logger().warning(levelDBData)

            optionDBData = QuestionOptionSerializer(all_option, many=True).data
            Logger().warning(optionDBData)

            merged_data = []
            for question in questionDBData:
                is_active_question: bool = question['isActive']
                if is_active_question:
                    question_id = question['id']
                    question['id'] = str(question['id'])
                    for level in levelDBData:
                        Logger().success(str(level))
                        if str(question['level']) == str(level['id']):
                            question['level'] = level['level']
                    optionResp = [option for option in optionDBData if str(option.get('question')) == str(question_id)]

                    merged_question = {
                        'options': optionResp,
                        'question': question
                    }

                    merged_data.append(merged_question)

            # return JsonResponse({
            #     "status": status.HTTP_200_OK,
            #     "message": "Data fetched successfully",
            #     "data": merged_data,
            # })
            return Response(
                data=merged_data,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )

        except Exception as e:
            Logger().error(f'Error from AllQuestions GET: {e}')

            return Response(
                data={
                    "successMessage": None,
                    "errorMessage": f"InternalServerError: {e}",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content_type="application/json",
            )

