from django.conf.urls import patterns,url
from accounts.views import user_list,SysrestUserpassword,SendResetEmail,index
#                          Register,
#                         Activate,
#                         SendResetEmail,
#                         ResetPassword,
#                         ,
                          

urlpatterns = patterns('', 
    url(r'index/$', index, name='Index'),
#    url(r'register/$', Register, name='Register'),

#    url(r'activate/(?P<token>\w+@\w+.\w+.[-_\w]*\w+.[-_\w]*\w+)/$', Activate, name='Activate'),
    url(r'reset/$',SendResetEmail,name='SendResetEmail'),
#    url(r'resetpass/(?P<token>\w+@\w+.\w+.[-_\w]*\w+.[-_\w]*\w+)/$', ResetPassword, name='ResetPassword'),
    url(r'userlist/$',user_list, name='user_list'),
    url(r'restuserpass/(\d+)$', SysrestUserpassword, name='SysrestUserpassword'),

)