from django.db import models

class MyUser(models.Model):
    # 定义模型类的字段，与数据库表的列对应
    id = models.AutoField(primary_key=True)  # 使用 AutoField 来表示自增主键
    account = models.CharField(max_length=100, db_column='account')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    password = models.CharField(default='123456',max_length=100, db_column='password')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    nickName = models.CharField(max_length=100, db_column='nick_name')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    phone = models.CharField(max_length=20, db_column='phone')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    email = models.EmailField(db_column='email')  # 使用 EmailField 来表示邮箱字段，设置 db_column 指定数据库中的列名
    isDel = models.BooleanField(default=False, db_column='is_del')  # 使用 BooleanField 来表示布尔类型字段，设置 db_column 指定数据库中的列名
    ctime = models.DateTimeField(auto_now_add=True, db_column='ctime')  # 使用 DateTimeField 来表示日期时间字段，设置 auto_now_add=True 表示在创建对象时自动添加当前时间，设置 db_column 指定数据库中的列名
    utime = models.DateTimeField(auto_now=True, db_column='utime')  # 使用 DateTimeField 来表示日期时间字段，设置 auto_now=True 表示在每次保存对象时自动更新当前时间，设置 db_column 指定数据库中的列名
    roleId = models.EmailField(db_column='role_id')   
    class Meta:
        # 指定数据库表的名称
        db_table = 'user'
        
class MyRole(models.Model):
    # 定义模型类的字段，与数据库表的列对应
    id = models.AutoField(primary_key=True)  # 使用 AutoField 来表示自增主键
    name = models.CharField(max_length=100, db_column='name')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    sort = models.CharField(max_length=100, db_column='sort')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    remarks = models.CharField(max_length=100, db_column='remarks')  # 使用 CharField 来表示字符类型字段，设置 db_column 指定数据库中的列名
    isDel = models.BooleanField(default=False, db_column='is_del')  # 使用 BooleanField 来表示布尔类型字段，设置 db_column 指定数据库中的列名
    ctime = models.DateTimeField(auto_now_add=True, db_column='ctime')  # 使用 DateTimeField 来表示日期时间字段，设置 auto_now_add=True 表示在创建对象时自动添加当前时间，设置 db_column 指定数据库中的列名
    utime = models.DateTimeField(auto_now=True, db_column='utime')  # 使用 DateTimeField 来表示日期时间字段，设置 auto_now=True 表示在每次保存对象时自动更新当前时间，设置 db_column 指定数据库中的列名
    
    class Meta:
        # 指定数据库表的名称
        db_table = 'role'
