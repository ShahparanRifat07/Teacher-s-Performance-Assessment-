from django.contrib import admin
from .models import StakeholderTag, Factor, Question, EvaluationEvent, StudentEvaluation, PeerEvaluation, ParentEvaluation, AdministratorEvaluation

# Register your models here.

admin.site.register(StakeholderTag)
admin.site.register(Factor)
admin.site.register(Question)
admin.site.register(EvaluationEvent)
admin.site.register(StudentEvaluation)
admin.site.register(PeerEvaluation)
admin.site.register(ParentEvaluation)
admin.site.register(AdministratorEvaluation)
