from cloze import db
from models import Meal
from flask_login import current_user

def getTotals(type):
    if(type == "calories"):
        return getTotalCalories()
    if(type == "fat"):
        return getTotalFat()
    if(type == "carbs"):
        return getTotalCarbs()
    if(type == "protein"):
        return getTotalProtein()

def getTotalCalories():
    mealList = db.session.query(Meal).filter_by(owner=current_user)
    totalCalories = 0
    for meal in mealList:
        totalCalories += (meal.calories * meal.servings)
    return totalCalories

def getTotalFat():
    mealList = db.session.query(Meal).filter_by(owner=current_user)
    totalFat = 0
    for meal in mealList:
        totalFat += (meal.fats * meal.servings)
    return totalFat

def getTotalCarbs():
    mealList = db.session.query(Meal).filter_by(owner=current_user)
    totalCarbs = 0
    for meal in mealList:
        totalCarbs += (meal.carbs * meal.servings)
    return totalCarbs

def getTotalProtein():
    mealList = db.session.query(Meal).filter_by(owner=current_user)
    totalProtein = 0
    for meal in mealList:
        totalProtein += (meal.protein * meal.servings)
    return totalProtein
