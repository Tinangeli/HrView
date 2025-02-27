import matplotlib
matplotlib.use('Agg')

from django.core.management import call_command
import matplotlib.pyplot as plt
import io
import base64
from django.http import JsonResponse
import numpy as np
from .models import StudentCategories, InstructorCategories  # Import models

# Generic function to generate pie chart data
def generate_pie_chart_data(scores, categories, descriptions=None):
    data = [
        {
            "category": categories[i],
            "score": int(scores[i]),
            "description": descriptions[i] if descriptions else None
        }
        for i in range(len(categories))
    ]
    return JsonResponse({"data": data})

# instructor pie chart api
def instructor_generate_pie(request):
    categories = [
        "lecture", "realtime writing", "moving/guiding", "answer student question",
        "pose question", "follow-up question", "individual discussion",
        "demonstrate/video", "administrative task", "waiting", "other"
    ]
    
    instructor_data = InstructorCategories.objects.first()  # fetch first row (modify as needed)
    if not instructor_data:
        return JsonResponse({"error": "no instructor data found."})
    
    scores = [
        instructor_data.overall_lecture, instructor_data.overall_realtime_writing,
        instructor_data.overall_moving_guiding, instructor_data.overall_answer_student_question,
        instructor_data.overall_pose_question, instructor_data.overall_follow_up_question,
        instructor_data.overall_individual_discussion, instructor_data.overall_demonstrate_video,
        instructor_data.overall_administrative_task, instructor_data.overall_waiting,
        instructor_data.overall_other
    ]
    
    return generate_pie_chart_data(scores, categories)

# student pie chart api
def student_generate_pie(request):
    categories = [
        "listening", "individual thinking", "group activity", "answer question",
        "ask question", "whole class discussion", "student presentation",
        "test", "waiting", "other"
    ]
    
    student_data = StudentCategories.objects.first()  # fetch first row (modify as needed)
    if not student_data:
        return JsonResponse({"error": "no student data found."})
    
    scores = [
        student_data.overall_listening, student_data.overall_individual_thinking,
        student_data.overall_group_activity, student_data.overall_answer_question,
        student_data.overall_ask_question, student_data.overall_whole_class_discussion,
        student_data.overall_student_presentation, student_data.overall_test,
        student_data.overall_waiting, student_data.overall_other
    ]
    
    descriptions = [
        "listening attentively to lectures.",
        "thinking critically on their own.",
        "engaging in group discussions and activities.",
        "answering questions posed by the instructor.",
        "asking questions to clarify doubts.",
        "participating in whole-class discussions.",
        "delivering student presentations.",
        "taking tests and assessments.",
        "time spent waiting or off-task.",
        "other unclassified activities."
    ]
    
    return generate_pie_chart_data(scores, categories, descriptions)

# plot api (placeholder)
def plot_api(request):
    return JsonResponse({"message": "plot api response"})

# run management command api
def run_management_command(request):
    try:
        call_command("your_command_name")  # replace with your actual management command
        return JsonResponse({"status": "success", "message": "command executed successfully"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
