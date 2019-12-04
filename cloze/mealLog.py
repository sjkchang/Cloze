"""
mealLog.py
====================================
Used to calculate totals for the meal log
"""

from . import db
from .models import Meal

def getTotals(type, owner):
    """
    Returns the totals for meal log

    Parameters
    ----------
    type
        string determining the type of total to be returned calories, servings, carbs, ect.
    owner
        User who's totals are being calculated
    """
    if(type == "calories"):
        return getTotalCalories(owner)
    if(type == "fat"):
        return getTotalFat(owner)
    if(type == "carbs"):
        return getTotalCarbs(owner)
    if(type == "protein"):
        return getTotalProtein(owner)

def getTotalCalories(owner):
    """
    Returns the total calories consumed by a user

    Parameters
    ----------
    owner
        The user who's total is being calculated
    """
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalCalories = 0
    for meal in mealList:
        totalCalories += (meal.calories * meal.servings)
    return totalCalories

def getTotalFat(owner):
    """
    Returns the total fats consumed by a user

    Parameters
    ----------
    owner
        The user who's total is being calculated
    """
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalFat = 0
    for meal in mealList:
        totalFat += (meal.fats * meal.servings)
    return totalFat

def getTotalCarbs(owner):
    """
    Returns the total carbs consumed by a user

    Parameters
    ----------
    owner
        The user who's total is being calculated
    """
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalCarbs = 0
    for meal in mealList:
        totalCarbs += (meal.carbs * meal.servings)
    return totalCarbs

def getTotalProtein(owner):
    """
    Returns the total protein consumed by a user

    Parameters
    ----------
    owner
        The user who's total is being calculated
    """
    mealList = db.session.query(Meal).filter_by(owner=owner)
    totalProtein = 0
    for meal in mealList:
        totalProtein += (meal.protein * meal.servings)
    return totalProtein
