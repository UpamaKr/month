from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    'january': 'Start a daily sketching habit',
    'february': 'Create a 3D model of a dynamic human figure',
    'march': 'Learn a new programming language',
    'april': 'Analyze a dataset related to a topic you love',
    'may': 'Create a map using GIS of your local area',
    'june': 'Draw a comic strip or graphic novel',
    'july': 'Create a GIS map that reflects changes over the past year',
    'august': 'Build a small app or tool using your favorite programming language',
    'september': 'Take a deep dive into a complex data analysis topic',
    'october': 'Participate in Inktober with a twist - make all your drawings 3D',
    'november': 'Contribute to an open source project',
    'december': None
}


def monthly_challenge_by_number(request, month):
    # Get a list of the keys (months) from the monthly_challenges dictionary
    months = list(monthly_challenges.keys())

    # If the requested month number is greater than the number of months, return a 404 error
    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    # Otherwise, get the month name corresponding to the month number
    redirect_month = months[month-1]

    # Use Django's reverse function to get the URL for the specific month's challenge
    redirect_path = reverse('month-challenge', args=[redirect_month])

    # Redirect to the specific month's challenge
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()

        })
    except:
        raise Http404


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months

    })
