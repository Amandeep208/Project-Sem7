# # from django.shortcuts import render

# # Create your views here.

# # Dummy data for display
# import requests
# from django.http import JsonResponse
# from django.shortcuts import render, redirect

# # Dummy data for display
# food_data = []
# exercise_data = []

# API_KEY = 'pL9RlvlifahsQXh4CRNq1w==4NXn4HKgkwoLgtL9'
# API_URL = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'

# def home(request):
#     # Calculate total calories from food and fitness tracker
#     total_calories_consumed = sum(item.get('calories', 0) for item in food_data)
#     total_calories_burned = sum(item.get('calories_burned', 0) for item in exercise_data)

#     # Pass the data to the template
#     return render(request, 'fitness_app/home.html', {
#         'calories_consumed': total_calories_consumed,
#         'calories_burned': total_calories_burned,
#     })
# def food_calorie(request):
#     if 'food_data' not in request.session:
#         request.session['food_data'] = []

#     if request.method == 'POST':
#         food_name = request.POST.get('food_name')
#         calories = int(request.POST.get('calories'))
#         food_data = request.session['food_data']
#         food_data.append({'name': food_name, 'calories': calories})
#         request.session['food_data'] = food_data  # Save data to session
#         request.session.modified = True  # Mark session as modified

#     return render(request, 'fitness_app/food_calorie.html', {
#         'food_data': request.session.get('food_data', []),
#     })

# def add_food(request):
#     if request.method == 'POST':
#         # Check if it's a delete request
#         if 'delete' in request.POST:
#             index = int(request.POST.get('index'))
#             del food_data[index]
#         else:
#             # Add food
#             food_name = request.POST.get('food_name')
#             calories = int(request.POST.get('calories'))
#             food_data.append({'name': food_name, 'calories': calories})
#     return render(request, 'fitness_app/add_food.html', {'food_data': food_data})

# def diet_plan(request):
#     return render(request, 'fitness_app/diet_plan.html')

# def fetch_all_activities():
#     # Fetch a sample activity to get the full list of possible activities
#     try:
#         response = requests.get(API_URL.format(''), headers={'X-Api-Key': API_KEY})
#         if response.status_code == 200:
#             data = response.json()
#             return [activity['name'] for activity in data]
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching activities: {str(e)}")
#     return []
# def get_activity_suggestions(request):
#     query = request.GET.get('query', '').lower()
#     if not query:
#         return JsonResponse({'suggestions': []})

#     try:
#         response = requests.get(API_URL.format(query), headers={'X-Api-Key': API_KEY})
#         if response.status_code == 200:
#             data = response.json()
#             suggestions = [activity['name'] for activity in data]
#             return JsonResponse({'suggestions': suggestions})
#         else:
#             return JsonResponse({'error': f"API Error: {response.status_code}"})
#     except requests.exceptions.RequestException as e:
#         return JsonResponse({'error': str(e)})
    
# def fitness_tracker(request):
#     global exercise_data
#     message = ""
#     suggestions = fetch_all_activities()
    
#     if request.method == 'POST':
#         if 'delete' in request.POST:
#             index = int(request.POST.get('index'))
#             del exercise_data[index]
#         else:
#             activity_name = request.POST.get('activity_name').lower()
#             duration = int(request.POST.get('duration'))
            
#             try:
#                 response = requests.get(API_URL.format(activity_name), headers={'X-Api-Key': API_KEY})
#                 if response.status_code == 200:
#                     data = response.json()
#                     activity = next((item for item in data if item['name'].lower().startswith(activity_name)), None)
#                     if activity:
#                         calories_per_hour = activity['calories_per_hour']
#                         calories_burned = (calories_per_hour * duration) / 60
#                         exercise_data.append({
#                             'name': activity['name'],
#                             'duration': duration,
#                             'calories_burned': round(calories_burned, 2),
#                         })
#                     else:
#                         message = "Sorry, this activity is not available in our database."
#                 else:
#                     message = f"API Error: {response.status_code}, {response.text}"
#             except requests.exceptions.RequestException as e:
#                 message = f"Network error occurred: {str(e)}"
    
#     return render(request, 'fitness_app/fitness_tracker.html', {
#         'exercise_data': exercise_data,
#         'message': message,
#         'suggestions': suggestions,
#     })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Exercise, FoodItem, Activity
import requests
from django.db.models import Sum

# API Configuration for Fitness Tracker
API_KEY = 'pL9RlvlifahsQXh4CRNq1w==4NXn4HKgkwoLgtL9'
API_URL = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'

# Home Page View
def home(request):
    total_food_calories = Food.objects.aggregate(Sum('calories'))['calories__sum'] or 0
    total_burned_calories = Exercise.objects.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

    context = {
        'total_food_calories': total_food_calories,
        'total_burned_calories': total_burned_calories
    }

    return render(request, 'fitness_app/home.html', context)


# Food Calorie Page View
# def food_calorie(request):
#     if request.method == 'POST':
#         # Get data from the form
#         food_name = request.POST.get('food_name')
#         calories = int(request.POST.get('calories'))

#         # Save the food entry to the database
#         Food.objects.create(name=food_name, calories=calories)

#     # Retrieve all food data
#     food_data = Food.objects.all()
#     return render(request, 'fitness_app/food_calorie.html', {
#         'food_data': food_data,
#     })
def food_calorie(request):
    if request.method == 'POST':
        # Save the food item to the database
        food_name = request.POST.get('food_name')
        calories = request.POST.get('calories')
        new_food = FoodItem(name=food_name, calories=calories)
        new_food.save()
        return redirect('food_calorie')  # Redirect after POST to refresh the page
    
    # Fetch all food items from the database to display in the table
    foods = FoodItem.objects.all()
    return render(request, 'fitness_app/food_calorie.html', {'foods': foods})


# Fitness Tracker Page View
# def fitness_tracker(request):
#     exercise_data = Exercise.objects.all()

#     if request.method == 'POST':
#         # Get data from the form
#         activity_name = request.POST.get('activity_name')
#         duration = int(request.POST.get('duration'))

#         # Call the API to get calories burned per hour
#         response = requests.get(API_URL.format(activity_name), headers={'X-Api-Key': API_KEY})
#         if response.status_code == 200:
#             api_data = response.json()

#             # Find the first matching activity
#             activity = next((item for item in api_data if activity_name.lower() in item['name'].lower()), None)
#             if activity:
#                 calories_per_hour = activity['calories_per_hour']
#                 calories_burned = (calories_per_hour / 60) * duration

#                 # Save the exercise entry to the database
#                 Exercise.objects.create(
#                     name=activity_name,
#                     duration=duration,
#                     calories_burned=calories_burned
#                 )
#             else:
#                 # Activity not found in the API database
#                 return render(request, 'fitness_app/fitness_tracker.html', {
#                     'exercise_data': exercise_data,
#                     'error': "Sorry, this activity is not available in our database.",
#                 })
#         else:
#             # API Error
#             return render(request, 'fitness_app/fitness_tracker.html', {
#                 'exercise_data': exercise_data,
#                 'error': "There was an error retrieving data from the API.",
#             })

#     return render(request, 'fitness_app/fitness_tracker.html', {
#         'exercise_data': exercise_data,
#     })
def fitness_tracker(request):
    if request.method == 'POST':
        activity_name = request.POST.get('activity_name')
        duration = int(request.POST.get('duration'))  # Convert to integer
        
        # Call the API to get calories burned for the activity
        api_url = f'https://api.api-ninjas.com/v1/caloriesburned?activity={activity_name}'
        response = requests.get(api_url, headers={'X-Api-Key': 'pL9RlvlifahsQXh4CRNq1w==4NXn4HKgkwoLgtL9'})

        if response.status_code == 200:
            data = response.json()
            for activity in data:
                calories_burned = activity['calories_per_hour'] * (duration / 60)  # Calculate calories burned based on duration
                new_activity = Activity(name=activity_name, duration=duration, calories_burned=calories_burned)
                new_activity.save()
                break  # Stop after saving the first result

        return redirect('fitness_tracker')  # Redirect to refresh the page
    
    activities = Activity.objects.all()  # Get all activities from the database
    return render(request, 'fitness_app/fitness_tracker.html', {'activities': activities})

# Delete Food Entry
def delete_food(request, id):
    food_item = get_object_or_404(FoodItem, id=id)  # Use FoodItem model instead of Food
    food_item.delete()
    return redirect('food_calorie')


# Delete Exercise Entry
def delete_exercise(request, id):
    activity = get_object_or_404(Activity, id=id)  # Use Activity model instead of Exercise
    activity.delete()
    return redirect('fitness_tracker')
