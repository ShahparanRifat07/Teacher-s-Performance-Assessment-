from django.db import models
from django.utils import timezone
from stakeholder.models import Student, Parent, Teacher, Administrator
from course.models import Class


class StakeholderTag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Factor(models.Model):
    title = models.CharField(max_length=128)
    tag = models.ManyToManyField(StakeholderTag)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.TextField()
    factor = models.ForeignKey(Factor, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.question


class EvaluationEvent(models.Model):
    Primary = 1
    Secondary = 2
    Tertiary = 3

    INSTITUTION = (
        (Primary, 'Primary'),
        (Secondary, 'Secondary'),
        (Tertiary, 'Tertiary'),
    )

    period = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    institution = models.CharField(max_length=3, choices=INSTITUTION, blank=True, null=True)
    factors = models.ManyToManyField(Factor)
    stakeholders = models.ManyToManyField(StakeholderTag)
    questions = models.ManyToManyField(Question)
    created_time = models.DateField(default=timezone.now())

    def __str__(self):
        return self.pk + " -> " + self.period + "(" + str(self.start_date) + "-" + str(self.end_date) + ")"


class StudentEvaluation(models.Model):
    evaluation_event = models.ForeignKey(EvaluationEvent, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class ParentEvaluation(models.Model):
    evaluation_event = models.ForeignKey(EvaluationEvent, on_delete=models.CASCADE)
    user = models.ForeignKey(Parent, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class PeerEvaluation(models.Model):
    evaluation_event = models.ForeignKey(EvaluationEvent, on_delete=models.CASCADE)
    user = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='%(class)s_evaluation_teacher')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='%(class)s_evaluated_teacher')
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class AdministratorEvaluation(models.Model):
    evaluation_event = models.ForeignKey(EvaluationEvent, on_delete=models.CASCADE)
    user = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
