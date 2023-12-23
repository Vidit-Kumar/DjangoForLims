from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test


def create_user(username, password, email='', first_name='', last_name='', is_admin=False):
    user = User()
    if not User.objects.filter(username=username).exists():
        if is_admin:
            user = User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

    return user

def remove_user(name):
    try:
        user_to_delete = User.objects.get(username=name)
        user_to_delete.delete()
        print(f"User {user_to_delete.username} has been deleted.")
    except User.DoesNotExist:
        print("User does not exist.")


        # library/views.py


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()


