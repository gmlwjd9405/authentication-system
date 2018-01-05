from django import forms
# from django.contrib.auth.models import User
from account.models import User


# 로그인 form
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
        fields = ['email', 'password']

    email = forms.EmailField(
        label="email",
        strip=False,
        widget=forms.EmailInput,
    )

    password = forms.CharField(
        label="password",
        strip=False,
        widget=forms.PasswordInput,
    )


# 회원가입 시 데이터를 입력 받을 form
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        # html 상에서 form 태그의 input들이 가질 name
        fields = ("name", "email", "password1", "password2")

    # 에러메세지 설정
    error_messages = {
        'password_mismatch': "비밀번호가 일치하지 않습니다.",
    }

    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        strip=False,
        help_text="비밀번호 확인을 위해 위와 동일한 비밀번호를 입력하세요.",
    )


    # html에 tag로 생성됨
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
          'class': 'form-control',
          'placeholder': '이메일은 로그인 아이디로 사용됩니다',
        })
        self.fields['name'].widget.attrs.update({
          'class': 'form-control',
          'placeholder': '이름을 입력하세요',
        })
        self.fields['password1'].widget.attrs.update({
          'class': 'form-control',
          'placeholder': '패스워드를 입력하세요',
        })
        self.fields['password2'].widget.attrs.update({
          'class': 'form-control',
          'placeholder': '패스워드를 확인해주세요',
        })

    # form을 통해 받은 데이터를 저장
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"]) #비밀번호 암호화
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

    error_messages = {
        'password_mismatch': "비밀번호가 일치하지 않습니다.",
    }

    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        strip=False,
        help_text="비밀번호 확인을 위해 위와 동일한 비밀번호를 입력하세요.",
    )

    def save(self, user):
        user.save()