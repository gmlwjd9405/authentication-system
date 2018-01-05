from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from account.forms import UserCreationForm, LoginForm
from account.models import User

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse


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
    print('tttttttttttt')
    user = User.objects.get(email=request.user.email)
    user.delete()

    return HttpResponseRedirect('/')


# 로그인
def signin(request):

    template = 'account/login.html'
    login_form = LoginForm()
    message = ""

    # form 작성 후 post method 시
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # 사용자 검증
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, '로그인 성공!')
                # 사용자가 admin인 경우
                if user.is_staff:
                    return HttpResponseRedirect('/admin/')
                # 사용자가 일반user인 경우
                else:
                    return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your account is not active, please contact the site admin")
        else:
            return HttpResponse("로그인 실패! : Your username and/or password were incorrect")

    # get method 시
    else:
        if request.user.is_anonymous:
            context = {"loginForm": login_form, "message": message}
            return render(request, template, context)
        # 이미 로그인을 한 상태면 home으로 이동.
        else:
            return HttpResponseRedirect('/home/')
            # redirect_url = reverse('/home/')
            # return redirect(redirect_url)


# 로그아웃
def log_out(request):
    logout(request)

    return HttpResponseRedirect('/')