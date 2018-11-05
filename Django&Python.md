- Django官网下载地址：[https://www.djangoproject.com/download/](https://www.djangoproject.com/download/) 
- 安装    
	- 将django解压到python安装目录同级目录下    
	- 在django根目录下执行命令：python setup.py install  
	- 将python安装目录下的\Lib\site-packages\django配置到环境变量中（Lib\site-packages路径下的django所在的文件夹可能不叫django，这样配就可以了，不用和文件夹的名字保持一致）    
这样  django就安装完成了。  
安装完成之后，在python中运行命令，检查安装是否成功  
    import django  
    django.get_version()  
![](https://i.imgur.com/eSs8OQt.png)

- 进入任意目录，执行命令就可以创建一个django工程  
    django-admin startproject Helloworld  
![](https://i.imgur.com/LHGl97z.png)  
- 创建admin后台管理员命令  
python manage.py createsuperuser  
![](https://i.imgur.com/zvoGybP.png)  
manage.py中包含大量命令，详细命令可以查询
- django工作流程图
![](https://i.imgur.com/gLA8ZQW.png)  
- 把数据存取逻辑、业务逻辑和表现逻辑组合在一起的概念有时被称为软件架构的Model-View-Controller(MVC)模式。在这个模式中，Model代表数据存取层，View代表的是系统中显示什么和怎么显示的部分，Controller指的是系统中根据用户输入并视需要访问模型，以决定使用哪个视图的部分。
在django中，MVC各自的定义：
 - M：数据存取部分，由django数据层处理
 - V：选择哪些数据要显示以及怎么显示的部分，由视图和模版处理
 - C：根据用户输入委派视图的部分，由django框架根据URLconf设置，对给定URL调用适当的python函数  
  
 在django中，C由框架自行处理，用户更关注的是模型（Model）、模版（Template）和视图（View），所以django也被称为MTV模式

 - M：Model，数据存取层。该层处理与数据相关的所有事务：如何存取、如何验证有效
 - T：Template，表现层。该层处理与表现相关的决定：如何在页面或其它类型文档中进行显示
 - V：View，业务逻辑层。该层包含存取模型及调取恰当模板的相关逻辑。
 


- 在模版html文件中，就可以指定请求的方法，get OR post
![](https://i.imgur.com/UMoKMsM.png)  
```<form method="post" action="/login/">
```  

- post方法接收参数方法
```
def login(request):  
	username=request.POST.get('username','')  
	password=request.POST.get('password','') 
``` 
定义一个login函数，这个函数的参数是request，也就是一个请求；在请求中找username参数对应的值，如果没有值，赋个空值；参数的名字和html中name属性的值是相同的
```
<form method='post' action='/login/'>
	<input name="username" type="text" placeholder="username">
	<input name="password" type="password" placeholder="password">
	<button id="btn" type="submit" >logn</button>
</form>
```
get方法接收参数与post方法类似，将POST替换为GET即可

- 可以通过enumerate生成一个包含索引和值的迭代序列

```
 #coding=utf-8 
 list1=range(10)
 for i,j in enumerate(list1):
     print "%d th is %d" %(i,j)
```

- \_\_name\_\_是python中的只读内置变量。在模块中访问该变量时，其随着模块的被调用方式的不同而有不同值：当该模块被直接调用执行时，\_\_name\_\_的值是\_\_main\_\_；当该模块被其他模块用import语句调用时，该值为当前模块名；在python中，所有的内置变量都以\_\_开头、结尾命名；另一个常用的内置变量是\_\_classs\_\_，在类内部使用时，其内容为当前类名