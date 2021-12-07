# django-web
django web

# step1
    pip install django

# step2
    PS C:\Users\lsv40\PycharmProjects\django-web> pip list
    Package    Version
    ---------- -------
    asgiref    3.4.1
    Django     3.2.9
    pip        21.3.1
    pytz       2021.3
    setuptools 57.0.0
    sqlparse   0.4.2
    wheel      0.36.2

# step3
    django-admin.exe startproject django_web .

# step4
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    December 07, 2021 - 14:12:44
    Django version 3.2.9, using settings 'django_web.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

# step5
    python manage.py migrate

        PS C:\Users\lsv40\PycharmProjects\django-web> python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK
        PS C:\Users\lsv40\PycharmProjects\django-web>


# step6
    
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py createsuperuser
    Username (leave blank to use 'lsv40'): sangbinlee9
    Email address: sangbinlee9@gmail.com
    Password:
    Password (again):
    The password is too similar to the username.
    Bypass password validation and create user anyway? [y/N]:
    Password:
    Password (again):
    The password is too similar to the username.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    PS C:\Users\lsv40\PycharmProjects\django-web>

# step 7 
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    December 07, 2021 - 14:19:03
    Django version 3.2.9, using settings 'django_web.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

# step 8 
    http://127.0.0.1:8000/admin