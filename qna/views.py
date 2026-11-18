from django.shortcuts import render, redirect
from .models import Questions, Comments
from django.core.paginator import Paginator
# render : html 새롭게 생성하기
# redirect : 기존에 있떤 url별칭로 바로 넘어가기

# Create your views here.


def main(request):
    # 만약에 필터 혹은 검색이 추가되면 순서는 줄어요. 
    # (1)검색 & 필터 (2) 정렬 (3) 페이지네이션

    # GET방식 데이터 받기
    search = request.GET.get('search')
    sort = request.GET.get('sort', '-created_at')
    page = request.GET.get('page', 1)

    question_list = Questions.objects.all()
    # 만약에 search가 있다면 search를 걸고 아니라면, 전체
    # 모델이름.objects.filter(컬럴속성며명="찾을내용") : 여러개의 데이터를 찾는 목표
    # 모델이름.objects.get(id="찾을내용") : 1개 데이터를 찾는게 목표

    # "안"
    # "안녕하세요"
    # "제안"
    # "물놀이안전수칙"
    # => 포함된 데이터 찾기 : 모델객체.filter(컬럼명__contains="찾을 단어")

    if search:
        question_list = question_list.filter(title__icontains=search)
    


    # 정렬해서 갖구와!
    # 모델이름.objects.order_by('정렬할컬럼명') 기본이 오름차순 반대 -내림차순
    # 오름차순 넘길때는 컬럼명 / 내림차순을 넘길때 컬럼명desc
    # question_list = Questions.objects.all()
    if sort:
        question_list = question_list.order_by(sort)


    #TODO: 검색할때는 초기화 페이지네이션 정렬 정리하기
    # if sort == 'title':
    #     question_list = Questions.objects.order_by('title')
    # elif sort == 'viewdecs':
    #     question_list = Questions.objects.order_by('')
    # elif sort == 'createddesc':
    #     question_list = Questions.objects.order_by('-created_at')
    # elif sort == 'createdasc':
    #     question_list = Questions.objects.order_by('created_at')


    # 페이지를 request에서 GET방식으로 가져오기 -------------------
    # - 페이지값이 없으면 기본값으로 1페이지를 보여주게하기
    
    # 페이지네이션 하기위해서 paginator 패키지를 가져오기
    # 페이지내이션 원하는 길이만큼 잘라서 보여주기
    # 데이터는 = Paginator(모델리스트, 보여주고싶은 페이지길이)
    page_list = Paginator(question_list, 10)
    # 내가 원하느 페이지 선택하기
    # 선택한페이지데이터 = page_list.get_page(페이지번호)
    page_get = page_list.get_page(page)

    data = {
        'questions':page_get,
    }

    return render(request, 'index.html', data)



def write(request):
    #  로그인한 녀석을 가져와서 보여줘야한다.

    return render(request, 'qna/write.html')

def create(request):
    # POST방법으로 던져졌는지를 확인해야한다.
    if request.method == 'POST':
        new_question = Questions()
        new_question.title = request.POST['title']
        new_question.text = request.POST['text']
        #  request.user 객체
        new_question.writer = request.user
        new_question.save()
        return redirect('main') 
    elif request.method == 'GET':
        return render(request, '404.html')

def detail(request, q_id):
    # get 가져오기 : 1개 가져올때
    question_detail = Questions.objects.get(id=q_id)
    
    # 다른질문은 필요없고, 해당하는 질문에 작성된 댓글만 보여지게하고 싶어! filter
    # 질문이 질문id랑 같은것
    comment_list = Comments.objects.filter(question=q_id)
    # (둘다가능) comment_list = Comments.objects.filter(question=question_detail)

    data = {
        'question':question_detail,
        'comments':comment_list,
    }
    return render(request, 'qna/detail.html', data)

def delete(request, q_id):
    question = Questions.objects.get(id=q_id)
    question.delete()
    return redirect('main')

def edit(request, q_id):
    question = Questions.objects.get(id= q_id)
    data = {
        'question':question,
    }
    return render(request, 'qna/edit.html', data)

def update(request, q_id):
    # 딕셔너리 값 가져오는 방법
    # 딕셔너리.get("key")이름
    # 딕셔너리['key']
    question = Questions.objects.get(id=q_id)
    question.title = request.POST.get('title')
    question.text = request.POST['text']
    question.save()
    return redirect('main')


def comment_create(request, q_id):
    # post방식일때만 저장가능 / Get은 막아주자. -> 404로 가자
    if request.method == 'POST':
        # 객체
        new_comment = Comments()
        new_comment.question = Questions.objects.get(id=q_id)
        new_comment.writer = request.user
        new_comment.text = request.POST['text']
        # DB
        new_comment.save()
        # return redirect("url별칭", 변수 = 넣어줄데이터 )
        return redirect('detail', q_id=q_id)


# delete 만들고 있어봐
# - *누구*를 삭제할지

def comment_delete(request, c_id):
    delete_comment = Comments.objects.get(id=c_id)
    delete_comment_q_id = delete_comment.question.id
    delete_comment.delete()
    return redirect('detail', q_id=delete_comment_q_id)

def comment_update(request, c_id):
    if request.method == 'POST':
        comment_modified = Comments.objects.get(id=c_id)
        comment_modified.text = request.POST['comment_text']
        comment_modified.save()
    return redirect('detail', q_id=comment_modified.question.id)
    





