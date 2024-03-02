from django.contrib import admin
from blog.models import Category, Post , Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# Register your models here.


class PostAdmin(SummernoteModelAdmin):

    date_hierarchy= "created_date"
    list_display= ("title","author","counted_view","status","created_date","published_date")
    list_filter = ("status","category")
    ordering = ["-published_date"]
    search_fields= ["content","title","author"]
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    ate_hierarchy= "created_date"
    list_display= ("name","subject","post","created_date","approve")
    list_filter = ("approve","post")
    ordering = ["-created_date"]
    search_fields= ["approve","post"]


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


admin.site.register(Category)

