from django.conf.urls import url
from django.contrib import admin
from users.views import *
from posts.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^posts/(?P<slug>\w+)/$', PostDetailView.as_view(), name="post"),
    url(r'^posts/(?P<slug>\w+)/tags/$', PostTagCreateView.as_view(), name="post-tags"),
    url(r'^(?P<slug>\w+)/$', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
