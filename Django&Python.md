1. Django官网下载地址：[https://www.djangoproject.com/download/](https://www.djangoproject.com/download/) 

 
2. 安装    
	- 将django解压到python安装目录同级目录下    
	- 在django根目录下执行命令：python setup.py install  
	- 将python安装目录下的\Lib\site-packages\django配置到环境变量中（Lib\site-packages路径下的django所在的文件夹可能不叫django，这样配就可以了，不用和文件夹的名字保持一致）    
这样  django就安装完成了。  
安装完成之后，在python中运行命令，检查安装是否成功  
    import django  
    django.get_version()  
![](https://i.imgur.com/eSs8OQt.png)

3. 进入任意目录，执行命令就可以创建一个django工程  
    django-admin startproject Helloworld  
![](https://i.imgur.com/LHGl97z.png)