from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import Quote, Favorite
from ..login_reg.models import User
from django.contrib import messages

def index(request):
    if "userID" not in request.session:
        # Prevent user from going to the success page if not logged in.
        return redirect(reverse('useradmin:index'))

    # User is logged in.
    userID = request.session['userID']
    context = {
        "alias" : User.objects.get(id = userID).alias,
        "quotes" : Quote.objects.getQuotable(userID),
        "favorites" : Quote.objects.getCurrentFavorites(userID)
    }
    return render(request, 'fall_assignment/index.html', context)

def userSummary(request, userID):
    if "userID" not in request.session:
        # Prevent user from going to the success page if not logged in.
        return redirect(reverse('useradmin:index'))

    # User is logged in.
    userID = request.session['userID']
    context = {
        "alias" : User.objects.get(id = userID).alias,
        "quotes" : Quote.objects.getQuotesByUser(userID)
    }
    return render(request, 'fall_assignment/user_summary.html', context)

def addQuote(request):
    if "userID" in request.session and request.method == 'POST':
        result = Quote.objects.addNew(request.POST, request.session['userID'])
        if not result["validated"] or not result["added"]:
            for err in result["errors"]:
                messages.add_message(request, messages.ERROR, err)

    return redirect(reverse('quotes:index'))

def addFavorite(request, quoteID):
    if "userID" in request.session:
        Favorite.objects.addQuote(request.session['userID'], quoteID)
    return redirect(reverse('quotes:index'))

def removeFavorite(request, quoteID):
    if "userID" in request.session:
        Favorite.objects.removeQuote(request.session['userID'], quoteID)
    return redirect(reverse('quotes:index'))
