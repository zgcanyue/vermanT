from . import views
from django.urls import path
from version import settings
from django.conf.urls import url
from django.views import static

#创建命名空间
app_name = 'verman'

urlpatterns = [

    #path('',views.index,name='index'),
    # path('login/',views.userlogin,name='userlogin'),
    # path('logout/',views.userlogout,name='userlogout'),
    # path('regist/',views.regist,name='regist'),
    # path('index/',views.index,name='index'),
    # path('users/',views.ManageUser,name='ManageUser'),
    # path('apps/',views.ManageApp,name='ManageApp'),
    # path('newapp/',views.NewApp,name='NewApp'),
    # path('delapp/',views.DelApp,name='DelApp'),
    # path('editapp/',views.EditApp,name='EditApp'),
    # path('newuser/',views.NewUser,name='NewUser'),
    # path('editok/',views.EditOk,name='EditOk'),

    path('',views.login1,name='login'),
    path('login1/',views.login1,name='login1'),
    path('index1/',views.index1,name='index1'),
    path('app1/',views.app1,name='app1'),
    path('user1/',views.user1,name='user1'),
    path('addapp1/',views.addapp1,name='addapp1'),
    path('delapp1/',views.delapp1,name='delapp1'),
    #path('editapp1/',views.editapp1,name='editapp1'),
    path('logout1/',views.logout1,name='logout1'),
    path('editok1/',views.editok1,name='editok1'),
    path('adduser1/',views.adduser1,name='adduser1'),
    path('deluser1/',views.deluser1,name='deluser1'),
    path('edituser1/',views.edituser1,name='edituser1'),
    path('edituserok1/',views.edituserok1,name='edituserok1'),
    path('download/',views.download,name='download'),

    #path('static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),


]

#自定义错误页面
handler404  = 'verman.views.page_not_found'