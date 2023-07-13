from django.shortcuts import render, redirect
from shop_recomender.models.user import User
from django.contrib.auth.hashers import check_password
from shop_recomender.forms.login import UserFromLogin
from django.contrib import messages
from django.contrib.auth.hashers import make_password



def authenticate(username, password):
    hashed_password = make_password(password, salt="defaultSalt")
    try:
        user = User.objects.get(username=username, password=hashed_password)
        return user
    except:
        return None

def login_util(request, user):
    try:
        user.is_authenticated = True
        request.user = user
    except:
        return request

def login(request):
    form = UserFromLogin()
    if request.method == 'POST':
        form = UserFromLogin(request.POST)
        username = form.data.get('username')
        password = form.data.get('password')
        if form.is_valid():
            user = authenticate(username=username, password=password)
            print(user)
            try:
                db_user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, f"User {username} does not exist in the database.")  # Display error message
                return redirect('user:registration')
            
            if check_password(password, db_user.password):
                if db_user.is_admin:
                    request.session['my_user_id'] = db_user.id
                    login = auth_login(request, user)
                    return redirect('user:admin_home')
                else:
                    request.session['my_user_id'] = db_user.id
                    login = auth_login(request, user)
                    return redirect('user:main_home')
            else:
                messages.error(request, f"Invalid password for user {username}.")  # Display error message
                return redirect('user:login')
        else:
            messages.error(request, f"Invalid username or password for user {username}.")  # Display error message
            return redirect('user:login')
    else:
        return render(request, 'registration/login.html', {'form': form})
