from . import db
from .models import Meal

def getTotals(type, owner):
    if(type == "calories"):
        return getTotalCalories(owner)
    if(type == "fat"):
        return getTotalFat(owner)
    if(type == "carbs"):
        return getTotalCarbs(owner)
    if(type == "protein"):
        return getTotalProtein(owner)

def getTotalCalories(owner):
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalCalories = 0
    for meal in mealList:
        totalCalories += (meal.calories * meal.servings)
    return totalCalories

def getTotalFat(owner):
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalFat = 0
    for meal in mealList:
        totalFat += (meal.fats * meal.servings)
    return totalFat

def getTotalCarbs(owner):
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalCarbs = 0
    for meal in mealList:
        totalCarbs += (meal.carbs * meal.servings)
    return totalCarbs

def getTotalProtein(owner):
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalProtein = 0
    for meal in mealList:
        totalProtein += (meal.protein * meal.servings)
    return totalProtein
