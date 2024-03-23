from django.shortcuts import render, redirect
from .models import Post, Comment, Tag
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TubeListView(ListView):
    model = Post
    template_name = 'tube/tube_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        q = self.request.GET.get("q", "")
        if q:
            return Post.objects.filter(title__contains=q) | Post.objects.filter(content__contains=q)
        return Post.objects.all()


class TubeDetailView(DetailView):
    model = Post
    template_name = 'tube/tube_detail.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            author = request.user
            message = form.cleaned_data["message"]
            c = Comment.objects.create(author=author, message=message, post=post)
            c.save()
            return redirect(reverse_lazy('tube_detail', args=[post.id]))
        else:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['error_message'] = '댓글을 입력해주세요.'
            return render(request, self.template_name, context)


class TubeTagListView(ListView):
    model = Post
    template_name = 'tube/tube_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__name__iexact=self.kwargs['tag'])


class TubeCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'tube/tube_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TubeUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'tube/tube_form.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class TubeDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'tube/tube_confirm_delete.html'
    success_url = reverse_lazy('tube_list')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)