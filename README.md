# Python-WebApp
My own WEB-Application template written in Python(backend) and AngularJS(frontend)

####FOLLOW THE DOCUMENTATION IN THE FILES, IT'S THE MOST IMPORTANT THING IN THIS ENTIRE PROJECT!

##Overview
    
####Folders
- Backend
    - app
- Web
    - app

####Application Files (Backend)

- /app
    - __init__.py turns whole application backend together with all imports and data
    - __controllers__.py the action happens here
    - __models__.py defines our classes, required for database and managing objects
    
---
####Database and backend tools
- __config__.py is our configuration data, we will look into it soon
- __db_create__.py creates our database from __models.py__
- __db_downgrade__.py downgrade database version
- __db_migrate__.py each time you change your __model__.py you need to migrate database too, run this to keep your models synced with database
- __db_upgrade__.py upgrade database to next or last version
- __Procfile__ used to run application on container and cloud machines like heroku
- __requirements__.txt required packages are listed here
- __run__.py run application (on local machines)
- __runproc__.py run application with forced debug mode
- __runserver__.py run application on server (will not work for local machine)

---
####Application Files (Frontend)
- __index__.html index file (displayed in browser)
- /app/__app__.js main application file, used to connect webapp with backend
- /app/__app__.css application stylesheet

###Requirements
- Python 2.7 and higher
- Flask
- Flask-CORS
- SQLAlchemy ORM
- Relational Database such as MySQL, PostgreSQL or even SQLite
- Time to get started with ;)

##Setup
###Install Depencies
__Notice:__ I have tons of depencies in requirements, but this will do your work quicklier if you need to scale your application ;)

``` pip install -r requirements.txt ```

---                
###Setup Database
I use PostgreSQL to work with data, but if you need you can use any other supported databases

- Open __config__.py located in /Backend/__config__.py
                
- Change      
``` SQLALCHEMY_DATABASE_URI = 'postgres://username:password@server:5432/database' ```
to your data and __save__

- Run __db_create__.py to create database
- (Optional) Run __db_migrate__.py to make your first migration!

---

###Get started & run application
####Run server side
- Run (from console or your IDE) located at /Backend/__run__.py
``` python2 run.py ```
- Visit __127.0.0.1:5000__ to check if everything is OK

####Run Web application
- Move to /Web/__index__.html
- Start Webserver
__If you are familiar with Python__ you may use SimpleHTTP server
```python -m SimpleHTTPServer```
__Or use other web-servers__ to store server your application

- Visit __127.0.0.1:80__ __NOTICE:__ The address is depending on which server you are running the web application, you may have to use yours

##Message from Developer

I hope you enjoying RESTful concept like i do, so i hope you are very happy with my little skeleton app, stay tuned for updates!