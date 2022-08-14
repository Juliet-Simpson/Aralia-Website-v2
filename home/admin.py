from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import InvestorUpdate


class InvestorUpdateAdmin(SummernoteModelAdmin):
    """docstring"""
    
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']

    summernote_fields = ('content',)


admin.site.register(InvestorUpdate, InvestorUpdateAdmin)
