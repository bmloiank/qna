from django.shortcuts import render, redirect
from .models import Questions
# render : html 새롭게 생성하기
# redirect : 기존에 있떤 url별칭로 바로 넘어가기

# Create your views here.

def main(request):
    return render(request, 'index.html')

def write(request):
    #  로그인한 녀석을 가져와서 보여줘야한다.

    return render(request, 'qna/write.html')

def create(request):
    # POST방법으로 던져졌는지를 확인해야한다.
    if request.method == 'POST':
        new_questions = Questions()
        new_questions.title = request.POST['title']
        new_questions.text = request.POST['text']
        #  request.user 객체
        new_questions.writer = request.user
        new_questions.save()
        return redirect('main')




