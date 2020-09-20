from django.contrib import admin
from .models import LLuser, employee, Photo, Nara #모델 참조할게
from django.utils.safestring import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.

#객체 테이블 형식으로 보여주기 
class DisplayEmployee(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', )
    # search_fields = ('name', 'job',) #서치해서 찾을수있게 검색창뜸
    # list_filter = ('gender', ) #성별로 찾을 수 있게 필터박스
    # ordering = ('-number',) #정렬
    #list_editable=('name', 'department',) #바로 수정 가능하게

    # def has_add_permission(self, request):
    #     return False #add 버튼 없애줌

#객체 사진 바로 보여주기
class DisplayPhoto(admin.ModelAdmin):
    list_display = ('name', 'photo', 'get_image') #하나일땐 무조건 , 있어야함

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height ="{height}"/>'.format(
            url = obj.photo.url,
            width = 200,
            height = 200,
        ))

class DisplayNara(admin.ModelAdmin):
    list_display = ('name', 'photo', 'get_image') #하나일땐 무조건 , 있어야함

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width} height ="{height}"/>'.format(
            url = obj.photo.url,
            width = 200,
            height = 200,
        ))

admin.site.register(LLuser)
admin.site.register(employee, DisplayEmployee) #이걸 기반으로 이 모델 출력해줄게
admin.site.register(Photo , DisplayPhoto)
admin.site.register(Nara, DisplayNara)


