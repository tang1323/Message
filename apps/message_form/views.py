from django.shortcuts import render


# 配置一个html页面显示的步骤
# 1.配置url
# 2.配置对应的views逻辑
# 3.拆分静态（css,js,image）放入到static,html放入到template之下
    # 1.可以放到对应的app下面
    # 2.也可以放入到全局的tempate和static(更建议这个做法)
# 4.配置全局的static文件访问路径的配置STATICFILES_DIRS
from apps.message_form.models import Message

# 1.get 提取(拉),就是把数据放到前端来, 2.post是把数据放到数据库中(推)
def message_form(request):

    # 通过models取数据,Message注入一个objects对象,是我们操作的核心,all()方法将所有数据取出来
    # queryset 1.进行for循环 2.进行切片
    # queryset本身并没有执行sql操作
    # all_message = Message.objects.all()
    # sliced_query = Message.objects.all()[:1]
    # print(all_message.query)# 打印sql语句
    # print(sliced_query.query)# 打印sql语句

    # 2.filter()方法
    # all_message = Message.objects.filter(name="tangming")
    # print(all_message.query)  # 打印sql语句
    # all_message.delete()
    # for message in all_message:
    #     print(message.name)

    # 3.get()方法,返回的是一个对象,数据不存在或者有多余数据存在会抛出异常
    # try:
    # message = Message.objects.get(name="tangming1")
    # 会抛出两个种异常,自己根据需求来定义这两个异常
    # except Message.DoesNotExist as e:
    #     pass
    # except Message.MultipleObjectsReturned as e:
    #     pass
    # message.delete()# 删除
    # print(message.name)



    # 进行数据插入操作
    # message = Message()# 实例化类一个对象
    # message.name = "tangming"
    # message.email = "tangming@qq.com"
    # message.address = "北京市"
    # message.message = "留言信息"
    #
    # message.save()# 1.如果存在则更新, 如果不存在则插入


    # 从html中提取数据保存到数据库中
    # 这个name要跟前头的name的值一致, name="name",name="email",name="address",name="message"
    if request.method == "POST":

        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        message_text = request.POST.get("message", "")

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()

        # 在view中,不管代码什么逻辑,除非我们抛了一个异常去django接管处理,只要正常执行,最终view一定一定要调用这个return
        return render(request, "message_form.html", {
            "message_ins": message
        })
    # if request.method =="GET":
    #
    #     # 从数据库里取出数据到前端来
    #     # 一般我们用filter()方法,因为如果数据库没有数据,可以返回一个空列表回来
    #     all_message = Message.objects.filter()
    #     if all_message:
    #         message = all_message[0]# 取第0个数据,转化成一个message对象
    #         # 数据库有数据才render
    #         return render(request, "message_form.html", {
    #             "message_ins": message# "message_ins",随便写,只是为了把message传进来
    #         })# 传递一个dict,dict的key就是变量的名称
    #     else:
    #         # 没有数据就很执行这个,因为它一定必须要返回 一个http的response的对象或者一个render
    #         return render(request, "message_form.html", )



    if request.method == "GET":
        # 这个是优化后的,因为一定要返回一个东西回去,那就定义一个空字典
        # 从数据库里取出数据到前端来
        # 一般我们用filter()方法,因为如果数据库没有数据,可以返回一个空列表回来
        var_dict = {}
        all_message = Message.objects.filter()
        if all_message:
            message = all_message[0]# 取第0个数据,转化成一个message对象
            var_dict = {
                "message_ins": message# "message_ins",随便写,只是为了把message传进来
            }
            # 数据库有数据才render,最后一定一定一定会调用render的
        return render(request, "message_form.html", var_dict)# 传递一个var_dict
        # else:
        #     # 没有数据就很执行这个,因为它一定必须要返回 一个http的response的对象或者一个render
        #     return render(request, "message_form.html", )
















