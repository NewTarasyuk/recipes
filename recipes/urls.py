"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from calculator.views import home_view,time_view,index

urlpatterns = [
    path('', home_view, name='home'),
    path('time/', time_view, name='time'),
    path('omlet/', index, name='index'),
    path('pasta/', index, name='index'),
    path('buter/', index, name='index'),
    # здесь зарегистрируйте вашу view-функцию
]
