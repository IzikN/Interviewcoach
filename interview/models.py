from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Q: {self.text[:50]}..."

class InterviewSession(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} for {self.role.name}"

class Answer(models.Model):
    session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer to {self.question.text[:50]}..."
