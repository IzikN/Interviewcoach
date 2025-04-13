from django.contrib import admin
from .models import Role, Question, InterviewSession, Answer

admin.site.register(Role)
admin.site.register(Question)
admin.site.register(InterviewSession)
admin.site.register(Answer)
