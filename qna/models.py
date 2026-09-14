# (1) 유저모델을 가져오기 
# django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Questions(models.Model):
    writer = models.ForeignKey(User, related_name='writer_questions', on_delete=models.CASCADE)

    # 질문 테이블 생성할때 필요한 내용
    # - 작성자 : 로그인한 유저로 자동으로 입력되게하기 
        #         => User모델과 연결 key(보통 id값) 
        #         => ForeignKey(모델명, related_name="User작성될 컬러명" , on_delete=삭제정책(models.CASCADE / SET_NULL))

    # - 제목 : 문자타임 models.CharField(max_length=100)
    # - 질문 내용 : 긴문자 models.TextField() 
    # - 생성일자 created_at = models.DateTimeField(auto_now_add=True)
    # - 수정일자 updated_at = models.DateTimeField(auto_now=True) # 저장하면 항상하기
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # DB 테이블명 정하기
        db_table='questions'
        # 관리자페이지 이름 설정
        # verbose_name = "단수이름 직접 정하기"
        # verbose_name_plural = "복수이름 직접 정하기"
        verbose_name='질문'
        verbose_name_plural='질문 목록'
        


# 과제1) 데이터베이스에 테이블 생성해보세요. > db.sqlite3에서 나오도록하기
# 과제2) admin페이지에가서 질문추가해보기