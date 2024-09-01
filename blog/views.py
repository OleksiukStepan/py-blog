from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("-created_time")
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


def add_commentary(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        comment_text = request.POST.get("comment")

        if comment_text:
            Commentary.objects.create(
                post=post, user=request.user, content=comment_text
            )

    return redirect("blog:post-detail", pk=post.id)