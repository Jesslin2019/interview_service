import json
from django import http
from django.core.paginator import Paginator
from django.views import View

from .models import Questions


class QuestionsView(View):

    def get(self, request):
        """
        查询试题
        :param request:前端传参
        :return:返回查询结果
        """
        args = request.GET
        type_id = args.get('type', '')
        title = args.get('title', '')
        pageSize = args.get('pageSize', 10)
        pageNumber = args.get('pageNumber', 1)

        try:
            if (type_id == '') & (title == ''):
                questions_lists = Questions.objects.filter(is_delete=False).order_by("-id")
            elif (type_id == '') & (title != ''):
                questions_lists = Questions.objects.filter(is_delete=False).filter(title__contains=title).order_by("-id")
            elif (int(type_id) in [1, 2, 3]) & (title == ''):
                questions_lists = Questions.objects.filter(is_delete=False).filter(type_id=int(type_id)).order_by("-id")
            elif (int(type_id) in [1, 2, 3]) & (title != ''):
                questions_lists = Questions.objects.filter(is_delete=False).filter(title__contains=title).filter(type_id=int(type_id)).order_by("-id")

            # 分页器
            total_count = len(questions_lists)      # 数据的条数
            paginator = Paginator(questions_lists, pageSize)
            questions_lists = paginator.page(pageNumber)  # 获取当前页数据
            questions_dicts = []
            for questions_list in questions_lists:
                questions_dict = {
                    "id": questions_list.id,
                    "title": questions_list.title,
                    "type": questions_list.type,
                    # "type": questions_list.type_id,
                }

                questions_dicts.append(questions_dict)

            return http.JsonResponse({
                "success": True,
                "data": questions_dicts,
                "pageSize": pageSize,
                "total": total_count,
                "pageNumber": pageNumber
            })

        except Exception as e:
            print(e)
            return http.JsonResponse({"success": False, "errormsg": "参数错误"})

    def post(self, request):
        """
        新增试题
        :param request:
        :return:
        """
        question_data = json.loads(request.body.decode())
        type_id = question_data.get('type')
        title = question_data.get('title')
        answer = question_data.get('answer')
        type_id = int(type_id)
        print(type_id, title, answer)

        if not all([type_id, title, answer]):
            return http.JsonResponse({"success": False, "errormsg": "参数错误"})

        if type_id == 1:
            q_type = "前端"
        elif type_id == 2:
            q_type = "后端"
        elif type_id == 3:
            q_type = "数据库"

        try:
            Questions.objects.create(
                title=title,
                type_id=type_id,
                type=q_type,
                answer=answer
            )
            return http.JsonResponse({"success": True})
        except:
            return http.JsonResponse({"success": False, "errormsg": "参数错误"})


class QuestionView(View):
    """详情，编辑"""
    def get(self, request):
        """
        点击详情，即查看单条数据
        :param request:
        :return:
        """
        id = request.GET.get("id")
        id = int(id)
        try:
            questions_dict = Questions.objects.filter(is_delete=False).get(id=id)
            questions_dict = {
                "id": questions_dict.id,
                "type": questions_dict.type_id,
                "title": questions_dict.title,
                "answer": questions_dict.answer
            }

            return http.JsonResponse({"success": True, "data": questions_dict})
        except:
            return http.JsonResponse({"success": False, "errormsg": "参数错误"})

    def post(self, request):
        """
        点击编辑，即修改 字段
        :param request:
        :return:
        """
        question_data = json.loads(request.body.decode())
        id = question_data.get("id")
        type_id = question_data.get("type")
        type_id = int(type_id)
        title = question_data.get("title")
        answer = question_data.get("answer")

        if type_id == 1:
            q_type = "前端"
        elif type_id == 2:
            q_type = "后端"
        elif type_id == 3:
            q_type = "数据库"

        try:
            Questions.objects.filter(id=id).update(type_id=type_id, type=q_type, title=title, answer=answer)
            return http.JsonResponse({"success": True})
        except:
            return http.JsonResponse({"success": False, "errormsg": "参数错误"})


class QuestionDelView(View):

    def post(self, request):
        """
        删除试题（逻辑删除）
        :param request:
        :return:
        """
        question_data = json.loads(request.body.decode())
        id = question_data.get("id")
        reason = question_data.get("reason")
        if not all([id, reason]):
            return http.JsonResponse({"success": False, "errormsg": "缺少必传参数"})

        try:
            Questions.objects.filter(id=id).update(is_delete=True, reason=reason)

            return http.JsonResponse({"success": True})
        except:
            return http.JsonResponse({"success": False, "errormsg": "参数错误"})



