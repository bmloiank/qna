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


'''
DB 테이블을 여러개 관계를 맺으면서 사용할기
sqlite, mysql, postgresql => 관계형 데이터베이스
mongoDB, ... -> 비관계형 데이터베이스

1:1 관계 회원 - 멤버십카드
1:N(1:다) 관계 회원 - 배송지관리
N:M(다:다) 팔로우 팔로잉
'''

'''
# <기획서 - 개발아닌사람이 작성하는 문서>
# <기능정의서 - 개발자가 작성하는 문서>
댓글 comments
- 제목
- 질문id
- 작성자 : 삭제시 set_null
- 내용
- 조회수
- 생성일자
- 수정일자
'''

class Comments(models.Model):
    # 질문번호가 담긴 컬럼을 만들기 - 어떤 질문에 속한 답변인지를
    # 답글 : 질문question
    # 질문입장이 : 답글들 comments (related_name)
    # 삭제정책 : on_delete = models.CASCADE
    question = models.ForeignKey(Questions, related_name='comments', on_delete=models.CASCADE)
    # 작성자 
    # 댓글 다 - 1 유저 
    # null 값 허용하기 => null=True
    writer = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

