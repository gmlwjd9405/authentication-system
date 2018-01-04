from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from account.forms import UserCreationForm
from account.models import User

from django.contrib import messages
from django.contrib.auth import login, authenticate


# 회원가입
def signup(request):

    # 이미 로그인한 상태 -> redirect
    if request.user.is_anonymous:
        pass
    elif request.user:
        return HttpResponseRedirect('/')

    template = 'account/signup.html'
    signup_form = UserCreationForm()
    message = ""

    # form 작성 후 post 액션 시
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST, request.FILES or None)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()

            # 계정 활성화 과정 필요
            # return HttpResponse('Please confirm your email address to complete the registration')
            # return HttpResponse('회원가입 성공!')
            context = {"message": '회원가입 성공!'}
            return render(request, 'account/signup_success.html', context)
        else:
            message = "비밀번호 미일치"

    elif request.method == "GET":
        pass

    context = {"signupForm": signup_form, "message": message}
    return render(request, template, context)


# 회원탈퇴
def delete_user(request):
    user = User.objects.get(email=request.user.email)
    user.delete()

    return HttpResponseRedirect('/')


# 로그인
def login(request):

    template = 'account/login.html'
    message = ""

    # form 작성 후 post method 시
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, _('로그인 성공!'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Your account is not active, please contact the site admin")
        else:
            return HttpResponse("로그인 실패! : Your username and/or password were incorrect")
    else:
        # get method
        # TODO: 로그인 계정의 is_active에따라 redirect 다르게 설정 필요
        # 이미 로그인을 한 상태면 home으로 이동.
        if request.user.is_anonymous:
            context = {"message": message}
            return render(request, template, context)
        else:
            return HttpResponseRedirect('/')


# 로그아웃
def logout(request):
    logout(request)

    return HttpResponseRedirect('/')