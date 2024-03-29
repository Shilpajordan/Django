from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html", {
        "months":months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul"
    # return HttpResponse(response_data)

def my_page_challenge_by_number(request, month):
    months = list(monthly_challenges.keys()) # returns a list of keys

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january (dynamic path)
    return HttpResponseRedirect(redirect_path)

def my_page(request, month): # adding the dynamic url parameter here
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month # month.capitalize()
        })
    except :
        raise Http404()
    