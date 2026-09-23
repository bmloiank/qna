from django.shortcuts import render, redirect
from .models import Questions
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
    question_detail = Questions.objects.get(id=q_id)
    data = {
        'question':question_detail,
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

