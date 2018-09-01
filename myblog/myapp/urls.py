from django.contrib import admin
from django.urls import path ,include,re_path
from myapp.views import*

app_name = 'myapp'
urlpatterns = [


    #注册
    path('register/',register,name = 'register'),
    path('email/',emails),
    path('registering/',registering,),
    #首页
    
    path('index/',index,name = 'index'),


    #登录
    path('login/',login,name = 'login'),
    path ('loading/',loading,name = 'loading'),
    path('quits/',quits,name = 'quits'),

    #内容
    re_path('article/(\d*)/',articles,name = 'article'),
    path('create_article/',create_article,name = 'create_article'),
    path('release/',release,name = "release")


]