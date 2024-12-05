# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add_food/', views.add_food, name='add_food'),
#     path('diet_plan/', views.diet_plan, name='diet_plan'),
#     path('fitness_tracker/', views.fitness_tracker, name='fitness_tracker'),
#     path('get_activity_suggestions/', views.get_activity_suggestions, name='get_activity_suggestions'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    # Home page route
    path('', views.home, name='home'),

    # Food Calorie page route
    path('food_calorie/', views.food_calorie, name='food_calorie'),

    # Fitness Tracker page route
    path('fitness_tracker/', views.fitness_tracker, name='fitness_tracker'),

    # Route to delete a food entry
    path('delete_food/<int:id>/', views.delete_food, name='delete_food'),

    # Route to delete an exercise entry
    path('delete_exercise/<int:id>/', views.delete_exercise, name='delete_exercise'),
]
