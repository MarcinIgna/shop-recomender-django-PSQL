import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from shop_recomender.models.user import User

def update_passwords():
    users = User.objects.all()
    for user in users:
        user.password = make_password(user.password)
        user.save()

if __name__ == '__main__':
    update_passwords()