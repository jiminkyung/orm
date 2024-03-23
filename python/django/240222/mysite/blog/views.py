from django.shortcuts import render

blog_database = [
    {
        "id": 1,
        "title": "제목1",
        "content": "내용1",
        "created_at": "2021-02-22",
        "updated_at": "2021-02-22",
        "author": "홍길동",
        "category": "일상",
        "tag": ["태그1", "태그2"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 3,
        "like_user": [10, 20, 21],
    },
    {
        "id": 2,
        "title": "제목2",
        "content": "내용2",
        "created_at": "2021-02-23",
        "updated_at": "2021-02-23",
        "author": "김철수",
        "category": "일기",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 10,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 3,
        "title": "제목3",
        "content": "내용3",
        "created_at": "2021-02-24",
        "updated_at": "2021-02-24",
        "author": "이영희",
        "category": "맛집",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 20,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
    {
        "id": 4,
        "title": "제목4",
        "content": "내용4",
        "created_at": "2021-02-25",
        "updated_at": "2021-02-25",
        "author": "박민수",
        "category": "여행",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "https://picsum.photos/200/300",
        "like_count": 30,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    }
]

def blog_list(request):
    # blog = Blog.objects.all()
    # 실제로 가져오는 방식은 위와 같다.
    context = { "blog_list": blog_database }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk)
    # 실제로 가져오는 방식은 위와 같다.

    context = { "blog": blog_database[int(pk) - 1] }
    return render(request, "blog/blog_detail.html", context)

# render(request, html파일, context(고정, 딕셔너리 형태))
# => html파일을 일반 텍스트로 가져옵니다. 중괄호와 같은 문법이 나오면 context에 있는 값을 가져와서
# 넣어줍니다. 그리고 이것을 사용자에게 넘겨주는 역할을 합니다.
# 넘겨줄때에는 HttpResponse를 사용합니다.