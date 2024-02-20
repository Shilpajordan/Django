from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat vegan!",
    "february":"Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Learn python for at least 20 minutes every day",
    "may": "Cook vegetarian food every day",
    "june": "Eat vegan!",
    "july": "Cook vegetarian food every day",
    "august": "Learn Django for at least 20 minutes every day",
    "september": "Cook vegetarian food every day",
    "october": "Cook vegetarian food every day",
    "november": "Learn Django for at least 20 minutes every day",
    "december": "Eat vegan!"
}

# Create your views here.

# def january(request):
#     return HttpResponse("Eat vegan!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day ")
def my_page_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) # returns a list of keys

    if month > len(months):
        return HttpResponseNotFound("Invalid error")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges" + redirect_month)

def my_page(request, month): # adding the dynamic url parameter here
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except :
        return HttpResponseNotFound("This month is not supported!")
    