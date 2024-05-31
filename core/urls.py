from django.contrib import admin
from django.urls import path
from main.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage),
    path('logout/', LogoutPage),
    path('login/', LoginPage),
    path('login/add/', SigninPage),
    path('mail/search/<str:cmail>/<str:password>', MailPage),
    path('mail/add/<firstname>/<lastname>/<age>/<phone>/<cmail>/<password>/<male>', AddMailPage),
]
