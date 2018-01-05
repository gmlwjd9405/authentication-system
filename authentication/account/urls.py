from django.conf.urls import url
from account.views import signup, delete_user, signin, log_out

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^delete/$', delete_user, name='delete'),

    url(r'^login/$', signin, name='login'),
    url(r'^logout/$', log_out, name='logout'),
]