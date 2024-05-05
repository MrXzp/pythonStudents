from app01 import models
from django.http import JsonResponse
# Create your views here. 
# 回应模板
def generate_response(status_code,data, message):
    return JsonResponse({'code': status_code, 'data': data if data else '', 'msg': message})
# 登录
def login(request):
    if request.method == 'POST':
        # 获取 POST 请求中的参数
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 查询数据库
        user = models.MyUser.objects.filter(account=username, password=password).first()
        if user:
            # 获取用户角色
            role = models.MyRole.objects.filter(id=user.role_id).first()
            data = {
                user:user,
                role:role
            }
            print("登录成功:",data)
            return generate_response(200,data,'登录成功')
        else:
            return generate_response(500,'用户名或密码错误')
    else:
        return generate_response(500,'请使用 POST 请求方式')
# 获取用户角色
def user_add(request):
    models.MyUser.objects.create(nickName="刘禅",account='liuc',phone='15777478591',roleId='20003')
    return generate_response(200,{},'返回用户列表接口')
 



 