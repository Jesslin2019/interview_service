from django.db import models


# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=500, verbose_name='题目')
    type_id = models.IntegerField(verbose_name="类型id")
    type = models.CharField(max_length=100, verbose_name='类型')
    answer = models.CharField(max_length=2000, verbose_name='答案')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    reason = models.CharField(max_length=100, verbose_name='删除理由')

    class Meta:
        db_table = 'questions'
        verbose_name = '试题表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

    # def to_dict(self):
    #     questions_dict = {
    #         "id": self.id,
    #         "title": self.title,
    #         "type": self.type_id,
    #         "answer": self.answer,
    #         "reason": self.reason,
    #     }





