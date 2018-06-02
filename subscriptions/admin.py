from django.contrib import admin
from .models import Websites,Feedback,SaveArticles,ReadArticles
# Register your models here.
admin.site.register(Websites)
admin.site.register(Feedback)
admin.site.register(SaveArticles)
admin.site.register(ReadArticles)