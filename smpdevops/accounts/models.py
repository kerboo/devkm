#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import  timezone



class MyGroups(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u'用户组'
        verbose_name_plural = u'用户组'
        db_table = 'mygroups'    
        

class MyUserManager(BaseUserManager):
    def  _create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError('Users must have an usename')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
                
    def create_user(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',False)

        return self._create_user(username, password,**extra_fields)
    
    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self._create_user(username,password,**extra_fields)

class MyUsers(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(max_length=255,verbose_name=u'邮箱')
    username = models.CharField(max_length=50,verbose_name=u'用户名',unique=True)
    is_active = models.BooleanField(default=True,verbose_name=u'激活用户',help_text=('设置用户状态'),)
    is_staff = models.BooleanField(default=False,verbose_name=u'管理站点',help_text=('是否可以管理站点'),)
    name = models.CharField(u'姓名',max_length=20,null=True)
    
    #所属用户组
    group = models.ForeignKey('MyGroups',null=True,blank=True,verbose_name=u'属组')
    
    date_joined = models.DateTimeField(verbose_name=u'创建时间', default=timezone.now)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def __str__(self):
        return self.usename
    
    
    
    @property
    def is_admin(self):
        return self.is_staff
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        verbose_name = u'用户管理'
        verbose_name_plural = u'用户管理'
        db_table = 'myusers'
    
    
class History_Login(models.Model):
    user = models.ForeignKey(MyUsers)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(auto_now=True)
    request_method = models.CharField(max_length=12,null=True)
    request_url = models.CharField(max_length=100, null=True)
    user_ip = models.GenericIPAddressField()
    
    class Meta:
        verbose_name = u'登录历史'
        verbose_name_plural = u'登录历史'
        

class Operation(models.Model):
    Opuser = models.CharField(max_length=12, null=True)
    Optime = models.DateTimeField(auto_now_add=True)
    Opaction = models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name = u'操作记录'
        verbose_name_plural = u'操作记录'
        
     
    
    
