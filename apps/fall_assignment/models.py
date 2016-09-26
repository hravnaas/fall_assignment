from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User
import datetime

class QuoteMgr(models.Manager):

    # Add a new quote.
    def addNew(self, data, userID):
        response = {}
        validationErrors = self.Validate(data)

        if len(validationErrors) > 0:
            response["validated"] = False
            response["added"] = False
            response["errors"] = validationErrors
        else:
            quote = Quote.objects.create(
                    message = data['Message'],
                    origin = data['Quoted By'],
                    user = User.objects.get(id = userID)
                )
            response["added"] = True
            response["validated"] = True
            response["quote"] = quote
        return response

    # Validate new quote before it's added.
    def Validate(self, data):
        MIN_QUOTED_BY_LEN = 4 # Must be more than 3 char.
        MIN_MSG_LEN = 11 # Must be more than 10 char.
        validationErrors = []

        if len(data["Quoted By"]) < MIN_QUOTED_BY_LEN:
            validationErrors.append("'Quoted By' field must contain at least 4 characters.")

        if len(data["Message"]) < MIN_MSG_LEN:
            validationErrors.append("'Message' field must contain at least 11 characters.")

        return validationErrors

    # Get all quotes that are not in logged in user's favorite list.
    def getQuotable(self, userID):
        #return Quote.objects.exclude(is_favorite = True, user_id = userID)
        #return Quote.objects.exclude(users__user_id_id = userID)
        return Quote.objects.all()

    # Get all quotes entered by the logged in user.
    def getQuotesByUser(self, userID):
        return Quote.objects.filter(user_id = userID)

    # Get all favorite quotes for logged in user.
    def getCurrentFavorites(self, userID):
        #return Quote.objects.filter(user_id = userID).exclude(is_favorite = False)
        return Quote.objects.all()

class Quote(models.Model):
    message = models.CharField(max_length=300)
    origin = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteMgr()

class FavoriteMgr(models.Manager):
    def addQuote(self, userID, quoteID):
        favorite = Favorite.objects.create(
            user = User.objects.get(id = userID),
            quote = Quote.objects.get(id = quoteID)
        )
        return favorite

    def removeQuote(self, userID, quoteID):
        Favorite.objects.get(user_id = userID, quote_id = quoteID).delete()
        return

class Favorite(models.Model):
    user = models.ForeignKey(User, null=True, related_name='users')
    quote = models.ForeignKey(Quote, null=True, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FavoriteMgr()
