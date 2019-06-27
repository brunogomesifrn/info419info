"""info419info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.views import index, listaprodutos, produtoespecifico, login, cadastro, perfil, tipos, cadastrartipo, produtos, produto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('produtos/', listaprodutos, name="listaprodutos"),
    path('produtos/<int:id>/', produtoespecifico, name="produtoespecifico"),
    path('login/', login, name="login"),
    path('cadastrar/', cadastro, name="cadastro"),
    path('perfil/', perfil, name="perfil"),
    path('perfil/tipos/', tipos, name="tipos"),
    path('perfil/tipos/cadastrar', cadastrartipo, name="cadastrartipo"),
    path('perfil/produtos', produtos, name="produtos"),
    path('perfil/produtos/cadastrar', produto, name="produto"),
]