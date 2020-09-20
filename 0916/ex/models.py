from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from datetime import datetime
# Create your models here.

class LLuser(AbstractUser):
    refresh = models.IntegerField(default = 0 , verbose_name = '접속횟수') #접속횟수 : 네모칸 이렇게뜸

    def countup(self):
        self.refresh += random.randrange(1,101) #서버가 이 코드를 마주칠때 1씩 늘어남.
        self.save()
        return self.refresh  

class employee(models.Model):
    number = models.IntegerField(primary_key= True ,verbose_name = '사원번호')
    name = models.CharField(max_length = 30, verbose_name = '이름')
    gender = models.CharField(max_length = 10, verbose_name = '성별')
    birth = models.DateField(verbose_name = '생일')
    department = models.CharField(max_length=30, verbose_name ='부서')
    rank = models.CharField(max_length=30, verbose_name = '직급')

    class Meta:
        verbose_name_plural = '직원' 

    #def __str__(self):
        #return 'No: %d, Name : %s' % (self.number, self.name)
        #return self.name object(1) 이런거 말고 이름으로 보이게

class Photo(models.Model):
    name = models.CharField(max_length = 100 , verbose_name = '제목')
    photo = models.ImageField(upload_to = '%d')

class Nara(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '이름')
    gender = models.CharField(max_length = 10, verbose_name = '성별')
    birth = models.DateField(verbose_name = '생일')
    photo = models.ImageField(upload_to = '%d')
    debut = models.DateField(verbose_name = '데뷔')
    site = models.CharField(max_length = 100, verbose_name = '사이트')
    school = models.CharField(max_length = 100, verbose_name = '학력')
    job = models.CharField(max_length=100, verbose_name ='직업')
    today = models.IntegerField(null = True)
    total = models.IntegerField(null = True)
    today_f = models.TextField(null = True)

    class Meta:
        verbose_name_plural = '나라' 
        
    @property #템플릿 안에서 이 함수를 쓰겠다.

    def today_fnc(self):  
        today = datetime.today().strftime("%Y-%m-%d") #2020-09-21=>string으로
        if self.today_f != today:#오늘이랑 어제랑 다르면 5<>3
            self.today_f = today  #오늘 날짜를 todayf 로 넣고 today_f = 3
            self.today = 0 #초기화 today = 0
            self.today += 1 #today=1
            self.total += 1 #total = 51
            self.save()
        
        else : 
            self.today += 1
            self.total += 1
            self.save()