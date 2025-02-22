import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt
import io
import base64
from django.http import JsonResponse
import subprocess
import numpy as np


def run_management_command(request):
    try:
        subprocess.run(["python", "manage.py", "migrate"], check=True)  # Replace "migrate" with your command
        return JsonResponse({"message": "Command executed successfully"})
    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": str(e)}, status=500)

def generate_plot():
    # Create the figure and axis
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])  # Sample plot
    ax.set_title("Sample Plot")
    

  

    # Save the plot to a BytesIO buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    
    # Encode the image to Base64
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close(fig)
    
    return image_base64

def plot_api(request):
    try:
        image_data = generate_plot()
        response = JsonResponse({"image": image_data})
        response.flush()  # Force sending response immediately
        return response
    except BrokenPipeError:
        pass

def generate_pie():
    # Define categories and values
    categories = [
        "Lecture", "Realtime Writing", "Moving Guiding", "Answer Student Question",
        "Pose Question", "Follow-up Question", "Individual Discussion",
        "Demonstrate Video", "Administrative Task", "Waiting", "Other"
    ]
    
    pie_values = np.array([20, 5, 10, 15, 10, 10, 15, 5, 10, 0, 0])

    # Create Pie Chart
    fig, ax = plt.subplots()
    ax.pie(pie_values, labels=categories, autopct='%1.1f%%', startangle=140)
    ax.set_title("Time Distribution in Lecture")

    # Save Pie Chart as PNG
    Generate_Image = io.BytesIO()
    plt.savefig(Generate_Image, format="png")
    Generate_Image.seek(0)

    # Encode image to Base64
    pie_image_base64 = base64.b64encode(Generate_Image.read()).decode('utf-8')
    Generate_Image.close()
    plt.close(fig)

    return pie_image_base64

def pie_api(request):
    try:
        pie_image = generate_pie()
        pie_response = JsonResponse({"image": pie_image})
        return pie_response
    except BrokenPipeError:
        pass