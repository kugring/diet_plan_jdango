"""
URL configuration for Jinstagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from Jinstagram.views import Sub
from content.views import Main, UploadFeed, Kugring
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',Main.as_view()),
    path('kugring/',Kugring.as_view()),
    path('',include('content.urls')),
    path('', include('user.urls'))
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


# 왜 content/upload에서 "/"가 빠지는지는 알 수 없다