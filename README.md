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
        sangbinlee9/sangbinlee9

# step 9
    PS C:\Users\lsv40\PycharmProjects\django-web> git add .
    PS C:\Users\lsv40\PycharmProjects\django-web> git commit -m 'django 프로젝트 테스트 ...'
    [main c1c2846] django 프로젝트 테스트 ...
     19 files changed, 328 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 .idea/.gitignore
     create mode 100644 .idea/django-web.iml
     create mode 100644 .idea/inspectionProfiles/profiles_settings.xml
     create mode 100644 .idea/misc.xml
     create mode 100644 .idea/modules.xml
     create mode 100644 .idea/vcs.xml
     create mode 100644 db.sqlite3
     create mode 100644 django_web/__init__.py
     create mode 100644 django_web/__pycache__/__init__.cpython-310.pyc
     create mode 100644 django_web/__pycache__/settings.cpython-310.pyc
     create mode 100644 django_web/__pycache__/urls.cpython-310.pyc
     create mode 100644 django_web/__pycache__/wsgi.cpython-310.pyc
     create mode 100644 django_web/asgi.py
     create mode 100644 django_web/settings.py
     create mode 100644 django_web/urls.py
     create mode 100644 django_web/wsgi.py
     create mode 100644 manage.py
    PS C:\Users\lsv40\PycharmProjects\django-web>


# blog app 폴더 생성
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py startapp blog

# blog app 폴더 생성
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py startapp single_pages

# add app module [blog, single_pages] in settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
        'single_pages'
    ]

# blog/models.py
    from django.db import models
    
    # Create your models here.
    from django.db import models
    
    
    class Post(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()
        created_at = models.DateTimeField()




# migrate
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py makemigrations
    Migrations for 'blog':
      blog\migrations\0001_initial.py
        - Create model Post
    PS C:\Users\lsv40\PycharmProjects\django-web>

# migrate
    PS C:\Users\lsv40\PycharmProjects\django-web> python.exe .\manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, blog, contenttypes, sessions
    Running migrations:
      Applying blog.0001_initial... OK
    PS C:\Users\lsv40\PycharmProjects\django-web>

# blog/admin.py 
    from django.contrib import admin
    
    # Register your models here.
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
# python.exe .\manage.py runserver
    
# http://127.0.0.1:8000/admin


# models.py change 
    from django.db import models

# Create your models here.
    from django.db import models
    
    
    class Post(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()
        created_at = models.DateTimeField()
    
        def __str__(self):
            return f'[{self.pk}]{self.title}'

# timezone change in settings.py

    #TIME_ZONE = 'UTC'
    TIME_ZONE = 'Asia/Seoul'
             
    #USE_TZ = True
    USE_TZ = False



# blog/models.py

# from django.db import models

# Create your models here.
# from django.db import models

# Create your models here.
    from django.db import models
    
    
    class Post(models.Model):
        title = models.CharField(max_length=30)
        content = models.TextField()
    
        # 자동 날짜 저장
        # created_at = models.DateTimeField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        # title 수정
        def __str__(self):
            return f'[{self.pk}]{self.title}'
