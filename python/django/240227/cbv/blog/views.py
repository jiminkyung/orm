from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q

# 클래스 기반 뷰가 꼭 제네릭 뷰는 아닙니다!
# 클래스로 HttpResponse를 반환하게 하면 그것도 클래스 기반 뷰입니다.
# 실무에서는 클래스 기반 뷰를 제네릭 뷰라고 부르는 경우가 많습니다.
# (동일한 용어로 취급하지만, 실제로 동일하진 않아요.)
# 제네릭 뷰는 장고에서 제공하는 여러가지 기능을 미리 구현해 놓은 클래스 기반 뷰입니다.

class PostList(ListView):
    model = Post
    ordering = "-pk"
    # 기본값은 최신 게시물이 맨 아래로 가기 때문에 pk를 기준으로 내림차순 정렬
    # template_name = "blog/내가_원하는_파일명.html" # 기본값: blog/post_list.html

    def get_queryset(self):
        queryset = super().get_queryset()

        # request에서 GET 파라미터 q를 가져옴
        q = self.request.GET.get("q", "")

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            ).distinct()
        return queryset


class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy('postdetail', args=[str(self.object.pk)])
    # 그냥 reverse를 사용하면 db에 생성값이 들어가는 시간을 고려하지않고
    # 바로~ 이동해버린다. reverse_lazy는 db에 반영되는 시간을 기다려준다.


class PostUpdate(UpdateView):
    model = Post
    fields = "__all__"
    succeess_url = reverse_lazy("blog_list")

class PostDelete(DeleteView):
    model = Post
    succeess_url = reverse_lazy("blog_list")

class PostTest(CreateView):
    model = Post

    # 이렇게 재정의 하는것을? 메서드 오버라이딩이라고 합니다.
    def get(self, request):
        return HttpResponse("get 요청이 왔습니다.")
    
    def post(self, request):
        return HttpResponse("post 요청이 왔습니다.")
    
# 실무에서는 바로 as_view()를 붙여서 사용합니다.
# urls의 패턴을 우리가 배운 형태되로 유지하기 위해서 아래처럼 사용하겠습니다.
blog_list = PostList.as_view()
blog_details = PostDetail.as_view()
blog_write = PostCreate.as_view()
blog_edit = PostUpdate.as_view()
blog_delete = PostDelete.as_view()
test = PostTest.as_view()

# python manage.py runserver로 지난시간까지 작동 되었던 것 확인
# ListView의 기본 get_queryset 메서드는 model 속성에서 정의된 모델의 전체 객체 목록을 반환합니다. PostList 뷰에서 model = Post로 정의되어 있어 기본적으로 Post 모델의 모든 객체를 반환하게 됩니다.
# super().get_queryset() 호출은 Post 모델의 전체 객체 목록을 반환합니다.