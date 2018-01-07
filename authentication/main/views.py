from django.shortcuts import render
from django.views import View


# 메인화면
class MainView(View):

    def get(self, request, *args, **kwargs):
        bg_image = "../static/img/background.jpg"
        context = {
            "title": "Heejeong's Page",
            "bg_image": bg_image
        }
        template = "account/main.html"

        return render(request, template, context)


# 사용자 화면
class HomeView(View):

    def get(self, request, *args, **kwargs):
        print('HomeView getttttttttttt')

        bg_image = "../static/img/home_background.jpeg"
        context = {
            "title": "USER PAGE",
            "bg_image": bg_image
        }
        template = "account/home.html"

        return render(request, template, context)