from django.contrib import admin
# 모델으리 가져오기
from .models import Questions, Comments

# Register your models here.
# 어드민에 추가하기
# admin.site.register(모델이름)
admin.site.register(Questions)
admin.site.register(Comments)