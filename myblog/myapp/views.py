from django.shortcuts import render ,redirect
from django.core.mail import send_mail,message 
from django.http import HttpRequest,HttpResponsePermanentRedirect,JsonResponse,HttpResponse
from django.conf import settings
from .models import article,user
from .verification import get_verification,hashs

 
# Create your views here.
 
def index(request):
    name = request.session.get('username','游客') 
    if (name=='游客'):
        return render(request,'myapp/index.html',{'articles':None ,'username':name})
    else:
        uerclass = user.users.get(username = name)   
        article_list = article.articles.all().filter(aemail = uerclass.email)
    return render(request,'myapp/index.html',{'articles':article_list ,'username':name})







#文章的发布

def articles(request,num):
    name = request.session.get('username','游客')

    if (name =='游客'):
        return HttpResponse('登录后再访问')
    
    userclass = user.users.get(username = name)
    content = article.articles.get(pk = num)
    
    if(content.aemail == userclass ):
        return render(request,'myapp/article.html',{'titles':content.title ,'context':content.context,'username':content.aemail.username})
    
    else:
        return HttpResponse('暂无权限访问')

def create_article(request):
    name = request.session.get('username','游客')
    if (name == '游客'):
        return redirect('/login/')
    else:
        return render(request,'myapp/create_article.html',{'username':name})







def release(request):
    name = request.session.get('username','游客')
    if (name == '游客'):
        return HttpResponse('请登录后再发布文章')
    else :
        tiele = request.POST['msg_title']
        content = request.POST['msg_content']
        userclass = user.users.get(username = name)
        article.articles.create_article(tiele,content,userclass)
        return HttpResponse('创建成功')


    
    








#注册账户    
    
def register(request):
    return render(request,'myapp/register.html')

def emails(request): 
    email = request.GET['info']
    try :
        user.users.get(pk = email)
        fail = ['该用户已存在！']
        return JsonResponse({'data':fail})
    except:
        status = ['验证码已发送！']
        lists = [email]
        capital = get_verification()
        request.session['ver'] = capital
        request.session.set_expiry(300)
        send_mail('验证码！',capital,settings.EMAIL_FROM,lists,fail_silently=True) 
        return JsonResponse({'data':status})


def registering(request):
    username = request.POST.get('username')
    e_mail = request.POST.get('e-mail')
    password = request.POST.get('password')
    input_ver = request.POST.get('ver')
    verification = request.session.get('ver')
    password = hashs(password)
    #比对验证码，创建用户
    if (input_ver == verification):
        user.users.create_user(username,e_mail,password)
        return HttpResponse('注册成功')
    else:
        return HttpResponse('注册失败')





#登录登出

def login(request):
    return render(request,'myapp/login.html')

def loading(request):
    account = request.POST.get('email')
    pd = hashs(request.POST.get('password'))
    try:
        right = user.users.get(pk = account)
        if (right.password == pd ):
            request.session['username'] = right.username
            request.session.set_expiry(0)
            return redirect ('/index/')
        else: 
            return HttpResponse(' 账号或密码错误')
    except:
        return HttpResponse('该账户不存在')


def quits(request):
    request.session.clear()
    return redirect('/index/')








    

 