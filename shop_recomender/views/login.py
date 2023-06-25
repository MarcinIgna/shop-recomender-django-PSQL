from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from shop_recomender.models.user import User
from django.contrib.auth.hashers import check_password
from shop_recomender.froms.login import UserFromLogin
from django.contrib.auth.hashers import make_password


def login(request):
    form = UserFromLogin()
    if request.method == 'POST':
        form = UserFromLogin(request.POST)
        username = form.data.get('username')
        password = form.data.get('password')
        if form.is_valid():
            # Check if the user exists in the database
            try:
                db_user = User.objects.get(username=username)
            except User.DoesNotExist:
                # User does not exist in the database
                print(f"User {username} does not exist in the database.")
                return redirect('user:regiestration')
            # Check if the password is correct
            if check_password(password, db_user.password):
                if db_user.is_admin:
                    request.session['my_user_id'] = db_user.id
                    print(f"User {username} welcome admin user.")
                    return redirect('user:admin_home')
                else:
                    request.session['my_user_id'] = db_user.id
                    print(f"User {username} logged in successfully.")
                    return redirect('user:main_home')
            else:
                # Invalid password
                print(f"Invalid password for user {username}.")
                return redirect('user:login')
        else:
            # Invalid username or password
            print(f"Invalid username or password for user {username}.")
            return redirect('user:login')
    else:
        # Return the login form for the GET request method
        return render(request, 'user/login.html', {'form': form})