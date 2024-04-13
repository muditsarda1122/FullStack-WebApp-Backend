"""
URL configuration for customers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from customers import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#'api/customers/' is the path and 'views.customers' is the function that should be called whenever a request is sent to the path
urlpatterns = [
    #this path gets us the token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #this path refreshes the token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/customers/', views.customers, name='customers'),
    path('api/customers/<int:id>', views.customer, name='customer'),
    path('api/register/', views.register, name='register')
]
