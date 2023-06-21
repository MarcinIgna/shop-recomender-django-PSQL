from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from shop_recomender.models.user import User

def after_login(request):
    user_id = request.session.get('my_user_id')
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/main_home.html', {'user': user})