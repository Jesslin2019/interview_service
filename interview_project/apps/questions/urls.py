from django.conf.urls import url

from questions import views

urlpatterns = [
    url(r'^api/questions/list/?$', views.QuestionsView.as_view()),      # 查询试题
    url(r'^api/questions/create$', views.QuestionsView.as_view()),     # 新增试题
    url(r'^api/questions/detail$', views.QuestionView.as_view()),      # 点击详情，即查看单条数据
    url(r'^api/questions/update$', views.QuestionView.as_view()),      # 点击编辑，即修改字段
    url(r'^api/questions/delete$', views.QuestionDelView.as_view()),   # 删除试题
]
