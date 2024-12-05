from django.db import models

# Model for Food Data
class Food(models.Model):
    name = models.CharField(max_length=200)  # Food name
    calories = models.IntegerField()  # Calories in the food item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"


# Model for Exercise Data
class Exercise(models.Model):
    name = models.CharField(max_length=200)  # Exercise activity name
    duration = models.IntegerField()  # Duration of exercise in minutes
    calories_burned = models.FloatField()  # Calories burned during the exercise

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=200)
    duration = models.IntegerField()  # duration in minutes
    calories_burned = models.FloatField()

    def __str__(self):
        return self.name