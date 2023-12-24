from django.apps import AppConfig
import sys

class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

    def ready(self):
        # Call your initialization function here
        if 'makemigrations' in sys.argv or 'migrate' in sys.argv:            
            return

        # Your code to run on server start goes here
        print("Executing code on server start...")
        from . import userrole
        userrole.remove_user('lims')
        #Regular user
        regular_user = userrole.create_user('lims_user', 'lims', 'lims@example.com', 'lims', 'regular', is_admin=False)
        # Admin User
        admin_user = userrole.create_user('lims_admin', 'admin', 'limsadmin@example.com', 'lims', 'admin', is_admin=True)
        print(f"Admin User {admin_user.username} created successfully.")
