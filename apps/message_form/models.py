from django.db import models

# Create your models here.
# 创建好mysql数据库后就可以到这里定义

# 继承这个models.Model,Message自己定义
# 运行之后会在数据库里生成一个表:message_from_message
class Message(models.Model):

    # 定义字段,CharField是数据库里的varchar类型....max_length是多长,如果不再定义,则在数据库己经定义了..primary_key=True定义主键
    name = models.CharField(max_length=20, verbose_name="姓名", primary_key=True)
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.TextField(verbose_name="留言信息")

    class Meta:
        verbose_name = "留言信息"

        # 如果不写这个,那在留言板会这样:留言信息s
        verbose_name_plural = verbose_name

        # 在数据库自定义生成一表名,可以为了类名Message保持一致,
        db_table = "message"








