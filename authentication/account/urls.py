from django.conf.urls import url
from account.views import signup, delete_user, login, logout

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^delete/$', delete_user, name='delete_user'),

    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/account/login/'}, name='logout'),
]