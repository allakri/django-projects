
from django.contrib import admin
from django.urls import path,include
from users.views import register ,profile
from django.contrib.auth import views as auth_view
from users.views import logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("food/",include("food.urls")),
    path('register/',register,name="register"),
    path('login/',auth_view.LoginView.as_view(template_name="users/login.html"),name="login"),
    # path('logout/', auth_view.LogoutView.as_view(template_name="users/logout.html", extra_context={"allow_get": True}), name="logout"),
    path('logout/', logout_view, name="logout"),
    path('profile/',profile ,name="profile"),
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)