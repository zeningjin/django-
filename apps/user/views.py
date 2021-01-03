from django.shortcuts import render, redirect, reverse
from apps.user.models import *
from django.http import HttpResponseRedirect
from apps.user.sms.yunpian import sms
from django.core import serializers
from django.http import JsonResponse
from apps.order.models import *


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(name=username).first()
        if user and user.pwd == password:
            request.session['is_login'] = True
            request.session['username'] = user.name
            request.session['user_id'] = user.id
            return redirect(reverse('goods:index'))
        return render(request, 'user/login.html', {'mes': '账号或密码错误'})


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    if request.method == 'POST':
        user_dict = request.POST.dict()
        if User.objects.filter(name=user_dict['username']).first():
            return render(request, 'user/register.html', {'mes': '用户名已存在'})
        phone = Phone.objects.filter(phone=user_dict['phone'], code=user_dict['auth_code'])
        if not phone:
            return render(request, 'user/register.html', {'mes': '验证码不正确'})
        if user_dict['password']:
            user = User.objects.create(
                name=user_dict['username'],
                pwd=user_dict['password'],
                phone=user_dict['phone']
            )
            request.session['is_login'] = True
            request.session['username'] = user.name
            request.session['user_id'] = user.id
            return redirect(reverse('goods:index'))
        return redirect(reverse('user:register'))


def logout(request):
    request.session.flush()
    return redirect('user:login')


def perCen(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        context = {
            'user': user
        }
        return render(request, 'user/PerCen.html', context=context)
    elif request.method == 'POST':
        info_dict = request.POST.dict()
        print(info_dict)
        user = User.objects.filter(id=user_id).update(
            name=info_dict['username'],
            # pwd=info_dict['password'],
            phone=info_dict['phone']
        )
        if all([info_dict['receiver'], info_dict['address'], info_dict['phone1']]):
            Address.objects.create(
                user_id=user,
                receiver=info_dict['receiver'],
                address=info_dict['address'],
                phone=info_dict['phone1'],
            )
        return HttpResponseRedirect(reverse("user:perCen", args=(user_id,)))


def addr_default(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        addr_id = request.GET.get('id')
        Address.objects.filter(is_default=1).update(is_default=0)
        Address.objects.filter(id=addr_id).update(is_default=1)
        return HttpResponseRedirect(reverse("user:perCen", args=(user_id,)))


def sending_sms(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        print(phone)
        user_phone = User.objects.filter(phone=phone)  # 判断用户手机是否存在
        if user_phone:
            return JsonResponse({"content": "用户手机已注册"}, safe=False)
        user_list = sms(phone)
        if user_list[0] != 0:
            return JsonResponse({"content": user_list[0]}, safe=False)
        info = Phone.objects.filter(phone=phone)
        if info:
            Phone.objects.filter(phone=phone).update(code=user_list[1])
            return JsonResponse({"content": user_list}, safe=False)
        Phone.objects.create(phone=phone, code=user_list[1])
        return JsonResponse({"content": user_list}, safe=False)


def register1(request):
    if request.method == 'GET':
        return render(request, 'user/retr_pwd.html')
    if request.method == 'POST':
        user_dict = request.POST.dict()
        user = User.objects.filter(name=user_dict['username'])
        if not user:
            return render(request, 'user/retr_pwd.html', {'mes': '用户名不存在'})
        phone = Phone.objects.filter(phone=user_dict['phone'], code=user_dict['auth_code'])
        if not phone:
            return render(request, 'user/retr_pwd.html', {'mes': '验证码不正确'})
        if user_dict['password']:
            user.update(
                pwd=user_dict['password'],
            )
            request.session['is_login'] = True
            request.session['username'] = user.first().name
            request.session['user_id'] = user.first().id
            return redirect(reverse('goods:index'))
        return redirect(reverse('user:register1'))


def sending_sms1(request):
    if request.method == "GET":
        phone = request.GET.get("phone")
        print(phone)
        user_phone = User.objects.filter(phone=phone)  # 判断用户手机是否存在
        if not user_phone:
            return JsonResponse({"content": "用户手机未注册"}, safe=False)
        user_list = sms(phone)
        if user_list[0] != 0:
            return JsonResponse({"content": user_list[0]}, safe=False)
        info = Phone.objects.filter(phone=phone)
        if info:
            Phone.objects.filter(phone=phone).update(code=user_list[1])
            return JsonResponse({"content": user_list}, safe=False)
        Phone.objects.create(phone=phone, code=user_list[1])
        return JsonResponse({"content": user_list}, safe=False)