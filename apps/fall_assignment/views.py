from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
#from django.db.models import Sum
from .models import User
from ..login_reg.models import User

def index(request):
    if "userID" not in request.session:
        # Prevent user from going to the success page if not logged in.
        return redirect(reverse('useradmin:index'))

    # User is logged in. Get the current status of pokes.
    context = {
        "firstName" : User.objects.get(id = request.session['userID']).alias
    }
    return render(request, 'fall_assignment/index.html', context)
