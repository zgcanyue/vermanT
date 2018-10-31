from django.core.serializers import json
from django.shortcuts import render,render_to_response,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import AppDate,User1
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

#获得IP
def get_ip(request):
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ''
    return regip

#获得登录用户名
def get_user(request):
    username = request.user
    return username

'''
#注册
def regist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username, password=password, email=email)
        return HttpResponse('Regist Success!')
        # uf = UserForm(request.POST)
        # if uf.is_valid():
        #     username = uf.cleaned_data['username']
        #     password = uf.cleaned_data['password']
        #     email = uf.cleaned_data['email']
        #     User.objects.create_user(username=username,password=password,email=email)
        #     return HttpResponse('Regist Success!')
    # else:
    #     uf = UserForm()
    return render_to_response('verman/regist.html')

#登录
def userlogin(request):
    if request.method == 'POST':
            username = request.POST.get('username_l')
            password = request.POST.get('password_l')
            user = authenticate(username=username,password=password)
            if user is not None:
                #login()方法验证的是django自带模块admin里注册的用户
                login(request,user)
                return render_to_response('verman/index.html')
            else:
                return HttpResponseRedirect('/verman/login/')
    return render_to_response('verman/login.html')


@login_required
def index(request):
    return render_to_response('verman/index.html')

@login_required
def ManageUser(request):
    users = User.objects.all()
    return render(request,'verman/users.html',{'users':users})

@login_required
def NewUser(request):
    if request.method == 'POST':
        username = request.POST.get('username_r')
        password = request.POST.get('password_r')
        email = request.POST.get('email_r')
        User.objects.create_user(username=username, password=password, email=email)
        return render(request,'verman/users.html')
    return render_to_response('verman/new-user.html')

@login_required
def ManageApp(request):
    apps = AppDate.objects.all()
    return render(request,'verman/app.html',{'apps':apps})

@login_required
def NewApp(request):
    if request.method == 'POST':
        appname = request.POST.get('appname')
        adnroid = request.POST.get('adnroid')
        ios = request.POST.get('ios')
        address = request.POST.get('address')
        testaccount = request.POST.get('testaccount')
        appdate = AppDate(app_name=appname,adnroid=adnroid,ios=ios,address=address,test_account=testaccount)
        appdate.save()
        #直接返回html页面表格下面的数据不显示，考虑重定向
        #return render(request, 'verman/app.html')
        return redirect(reverse('verman:ManageApp'))
    return render(request,'verman/new-app.html')

@login_required
def DelApp(request):
    id = request.GET.get('id')
    AppDate.objects.filter(id=id).delete()
    return redirect(reverse('verman:ManageApp'))

@login_required
def EditApp(request):
    global spid
    spid= request.GET.get('id')
    edit = AppDate.objects.filter(id=spid)
    return render(request,'verman/edit-app.html',{'edit':edit})

@login_required
def EditOk(request):
    AppDate.objects.filter(id=spid).delete()
    appname = request.POST.get('appname')
    adnroid = request.POST.get('adnroid')
    ios = request.POST.get('ios')
    address = request.POST.get('address')
    testaccount = request.POST.get('testaccount')
    #AppDate.objects.filter(id=spid).update(app_name=appname, adnroid=adnroid, ios=ios, address=address, test_account=testaccount)
    update = AppDate(app_name=appname, adnroid=adnroid, ios=ios, address=address, test_account=testaccount)
    update.save()
    return render(request,'verman/editok.html')

#退出
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/verman/login/')
'''

#-----------------------new-----------------------

#登录
def login1(request):
    if request.method == 'POST':
            username = request.POST.get('username_l')
            password = request.POST.get('password_l')
            user = authenticate(username=username,password=password)
            if user is not None:
                #login()方法验证的是django自带模块admin里注册的用户
                login(request,user)
                # ip = get_ip(request)
                # user = User(ip_address=ip)
                # user.save()
                return redirect(reverse('verman:index1'))
            else:
                return HttpResponseRedirect('/verman/login1/')
    return render_to_response('verman/login.html')

@login_required
def index1(request):
    user = get_user(request)
    return render(request,'verman/index1.html',{'user':user})

@login_required
def app1(request):
    apps = AppDate.objects.all()
    return render(request,'verman/app1.html',{'apps':apps})

@login_required
def addapp1(request):
    if request.method == 'POST':
        appname = request.POST.get('appname')
        adnroid = request.POST.get('adnroid')
        ios = request.POST.get('ios')
        address = get_ip(request)
        testaccount = get_user(request)
        if appname and adnroid and ios:
            appdate = AppDate(app_name=appname,adnroid=adnroid,ios=ios,address=address,test_account=testaccount)
            appdate.save()
        else:
            return HttpResponse('请填写完整信息')
        #直接返回html页面表格下面的数据需要刷新才能显示，需要重定向
        #return render(request, 'verman/app.html')
        return redirect(reverse('verman:app1'))
    return render(request,'verman/app1.html',{'address':get_ip(request),'testaccount':get_user(request)})

@login_required
def delapp1(request):
    user = request.user
    if user.is_superuser:
        id = request.GET.get('id')
        AppDate.objects.filter(id=id).delete()
        return redirect(reverse('verman:app1'))
    else:
        return HttpResponse('管理员才能删除！')

# #修改之后不需要这个视图了
# @login_required
# def editapp1(request):
#     spid= request.GET.get('id')
#     edit = AppDate.objects.filter(id=spid)
#     return render(request,'verman/editapp1.html',{'edit':edit})

@login_required
def editok1(request):
    #AppDate.objects.filter(id=spid).delete()
    id = request.POST.get('id')
    #account = AppDate.objects.get(id=id).test_account
    user = get_user(request)
    #userid = AppDate.objects.get(test_account=user).id
    if user.is_superuser:
        appname = request.POST.get('appname1')
        adnroid = request.POST.get('adnroid1')
        ios = request.POST.get('ios1')
        #address = request.POST.get('address')
        address = get_ip(request)
        #testaccount = request.POST.get('testaccount')
        testaccount = get_user(request)
        #AppDate.objects.filter(id=spid).update(app_name=appname, adnroid=adnroid, ios=ios, address=address, test_account=testaccount)
        AppDate.objects.filter(id=id).update(app_name=appname, adnroid=adnroid, ios=ios,)
        #update.save()
        return redirect(reverse('verman:app1'))
        #return render(request,'verman/app1.html',{'account':account})
    else:
        return HttpResponse('管理员才能修改')

@login_required
def user1(request):
    users = User.objects.all()
    return render(request,'verman/user1.html',{'users':users})

@login_required
def adduser1(request):
    user = get_user(request)
    # 判断用户是否是管理员
    if user.is_superuser:
    #if request.method == 'POST':
        username = request.POST.get('username_r')
        password = request.POST.get('password_r')
        email = request.POST.get('email_r')
        User.objects.create_user(username=username, password=password, email=email)
        return redirect(reverse('verman:user1'))
    else:
        return HttpResponse('管理员才能添加账号！')
    #return redirect(reverse('verman:user1'))

@login_required
def deluser1(request):
    # te1 = request.user
    # #tt1 = User.objects.get(username=te1).id
    # return render(request,'verman/user1.html',{'tel':te1})
    # 获取当前登录用户，判断是否有权限删除
    user = get_user(request)
    id = request.GET.get('id')
    #if User.objects.get(id=id).is_superuser:
    if user.is_superuser:
        User.objects.filter(id=id).delete()
        return redirect(reverse('verman:user1'))
    else:
        return HttpResponse("你没有权限删除！！！")

@login_required
def edituser1(request):
    user = get_user(request)
    #管理员才能修改
    if user.is_superuser:
        id= request.GET.get('id')
        editu = User.objects.filter(id=id)
        return render(request,'verman/edituser1.html',{'editu':editu})
    else:
        return HttpResponse('你不能修改')
    #return render(request,'verman/edituser1.html')

@login_required
def edituserok1(request):
    id = request.POST.get('id')
    username = request.POST.get('username_r')
    password = request.POST.get('password_r')
    email = request.POST.get('email_r')
    if username and password and email:
        User.objects.filter(id=id).update(username=username, email=email)
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
    return redirect(reverse('verman:user1'))

@login_required
def logout1(request):
    logout(request)
    return HttpResponseRedirect('/verman/login1/')

def page_not_found(request):
    return render(request,'verman/404.html')

def download(request):
    return render(request,'verman/download.txt')