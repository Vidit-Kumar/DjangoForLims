from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

    def ready(self):
        # Call your initialization function here
        from . import userrole
        userrole.remove_user('lims')
        #Regular user
        regular_user = userrole.create_user('lims_user', 'lims', 'lims@example.com', 'lims', 'regular', is_admin=False)
        # Admin User
        admin_user = userrole.create_user('lims_admin', 'admin', 'limsadmin@example.com', 'lims', 'admin', is_admin=True)
        print(f"Admin User {admin_user.username} created successfully.")
