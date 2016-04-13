from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
# from posts.utils.sms import send_sms


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content',
        'thumbnail_image',
    ]
    template_name = "posts/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

#    send_sms(
#        "01091777233",
#        "01091777233",
#        "this is test",
#    )
