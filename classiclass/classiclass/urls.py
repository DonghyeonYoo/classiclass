from django.conf.urls import url
from django.contrib import admin
from users.views import *
from posts.views import *
from tags.views import *
from posts.api import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name="home"),
    url(r'^posts/new/$', PostCreateView.as_view(), name="posts-create"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^posts/(?P<slug>\w+)/tags/$', PostTagCreateView.as_view(), name="post-tags"),
    url(r'^posts/(?P<slug>\w+)/$', PostDetailView.as_view(), name="post"),
    url(r'^api/posts/(?P<hash_id>\w+)/$', PostDetailAPIView.as_view(), name="api-post"),
    url(r'^filtering/tags/(?P<slug>\w+)/$', TagDetailView.as_view(), name="tag"),
    url(r'^(?P<slug>\w+)/$', ProfileView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
