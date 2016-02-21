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
from hackaton.views import home, HackatonList, index, HackatonListUser, HackatonEquiposList, HackatonDetail, hackatones, EquiposBusquedaView, SponsorsList
from users import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', index),
    url(r'^home/$', home),
    url(r'^hackaton/preview/$', HackatonList.as_view(), name='hackaton-list'),
    url(r'^hackaton/preview/(?P<username>[0-9a-zA-Z_-]+)/$', HackatonListUser.as_view(), name='hackaton-list-user'),
    url(r'^hackaton/(?P<id>[0-9]+)/$', HackatonDetail.as_view(), name='hackaton-detail'),
    url(r'^hackaton/(?P<id>[0-9]+)/equipos/$', HackatonEquiposList.as_view(), name='hackaton-equipos'),
    url(r'^hackaton/(?P<id>[0-9]+)/sponsores/$', SponsorsList.as_view(), name='sponsors-list'),
    #url(r'^hackaton/(?P<id>[0-9]+)/tecnologia/$', HackatonEquiposList.as_view(), name='hackaton-equipos'),
    url(r'^user/login/', views.loginView),
    url(r'^user/signup/$', views.signup),
    url(r'^user/registroUser/$', views.registroUser),
    url(r'^user/loginUser/$', views.loginUser),
    url(r'^user/coderView/$', views.coderView),
    url(r'^user/reclutadorView/$', views.reclutadorView),
    url(r'^user/crearCoder/$', views.crearCoder),
    url(r'^user/crearReclutador/$', views.crearReclutador),
    url(r'^hackatones/(?P<idHackaton>[0-9a-aA-Z_-]+)/$', hackatones),
    url(r'^find/(?P<parametro>[0-9a-zA-Z_-]+)/$', EquiposBusquedaView.as_view(), name='equipos-busqueda'),
    url(r'^user/resultadosView/$', views.resultadosView)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
