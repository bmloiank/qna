from django.shortcuts import render, redirect
from .models import Questions, Comments

# render : html 새롭게 생성하기
# redirect : 기존에 있떤 url별칭로 바로 넘어가기

# Create your views here.

def main(request):
    question_list = Questions.objects.all()
    data = {
        'questions':question_list,
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
    





