from django.conf.urls import url
from main.views import MainView, HomeView

urlpatterns = [
    url(r'^$', MainView.as_view()),

    url(r'^home/$', HomeView.as_view()),
]