# python-django-crud
Django-Python CRUD application

Django Tutorial to get started with a new project

https://docs.djangoproject.com/en/1.11/intro/tutorial01/

After checkout go to the checked out directory

1. <GIT_HOME>\pydjapp

2. execute the folowing command "python manage.py runserver"

  * Note by Rik: to have the app function properly now, you have to execute "python manage.py migrate" before "... runserver"
  * You'll then don't see the lines about the unapplied migrations.

You should see something like this
***********************************************************************************************************************************************
C:\Python\learntocodetogether\python-django-crud\pydjapp>python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes,
 sessions.
Run 'python manage.py migrate' to apply them.
September 03, 2017 - 13:36:03
Django version 1.11.4, using settings 'pydjapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
***********************************************************************************************************************************************

3. Go to browser and open this link "http://127.0.0.1:8000/"
You should see a webpage that we can use as our app's interface."

4. YOU CAN START CODING NOW ;)
