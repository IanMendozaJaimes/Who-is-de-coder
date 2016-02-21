"""WhoIsTheCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hackaton.views import home, HackatonList, index
from users import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', index),
    url(r'^home/$', home),
    url(r'^hackaton/preview/$', HackatonList.as_view(), name='hackaton-list'),
    url(r'^user/login/', views.loginView),
    url(r'^user/signup/$', views.signup),
    url(r'^user/registroUser/$', views.registroUser),
    url(r'^user/loginUser/$', views.loginUser),
    url(r'^user/coderView/$', views.coderView),
    url(r'^user/reclutadorView/$', views.reclutadorView),
    url(r'^user/crearCoder/$', views.crearCoder),
    url(r'^user/crearReclutador/$', views.crearReclutador),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
