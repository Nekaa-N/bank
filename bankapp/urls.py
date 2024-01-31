from django.urls import path

import statistics
from django.conf import settings
from django.urls import path
from .views import home, result, login_view,signup

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path('result/', result, name='result'),

]

