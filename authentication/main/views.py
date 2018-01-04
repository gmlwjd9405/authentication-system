from django.shortcuts import render
from django.views import View


# 유저 메인화면
class HomeView(View):

    def get(self, request, *args, **kwargs):
        print("testttttttttt")
        bg_image = "../static/img/background.jpg"
        context = {
            "title": "Heejeong's Page",
            "bg_image": bg_image
        }
        template = "account/home.html"

        return render(request, template, context)
