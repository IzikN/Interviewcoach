# interview/views.py
from django.shortcuts import render, redirect
from .models import Role, Question, InterviewSession, Answer
import openai

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def home(request):
    roles = Role.objects.all()
    return render(request, 'home.html', {'roles': roles})

def start_interview(request, role_id):
    role = Role.objects.get(id=role_id)
    questions = Question.objects.filter(role=role)
    session = InterviewSession.objects.create(role=role)

    return render(request, 'interview.html', {'questions': questions, 'session': session})

def submit_answer(request, session_id):
    if request.method == 'POST':
        session = InterviewSession.objects.get(id=session_id)
        question = Question.objects.get(id=request.POST['question_id'])
        response = request.POST['response']

        # Call OpenAI for feedback
        feedback = get_feedback_from_openai(response)

        answer = Answer.objects.create(
            session=session,
            question=question,
            response=response,
            feedback=feedback
        )

        return redirect('interview:show_feedback', session_id=session.id)

def get_feedback_from_openai(answer_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Give feedback on this interview answer: {answer_text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def show_feedback(request, session_id):
    session = InterviewSession.objects.get(id=session_id)
    answers = Answer.objects.filter(session=session)
    return render(request, 'feedback.html', {'answers': answers})
