# webapp-skeleton
A web portal where users can manage application links.

[home]: ./assets/home.PNG
[db-design]: ./assets/db_design.PNG

![alt text][home]

## Install and Run

### python pip
Python3 is preferred. Feel free to set up an virtualenv for following installation commands.
```
# install dependencies, pip3 for Linux 
pip install -r requirements.txt

# start the web app
python manage.py runserver
```
### Docker
Set up `docker-machine` and `docker-compose` for running following command.
```
docker-compose up
```

If the installation is correct, you should be able to see the Home page at the URL: `http://localhost:8000`.

## Programming
### Database Design

![alt text][db-design]


### Programming Frameworks
- Backend: Django, SQLite.

- Frontend: JQuery, JQuery UI, Ajax, Bootstrap.

## Features
The web app achieved following functions and features:
- Login control.
- Signup function is added.
- After login, the user’s associate apps are displayed in card layout. 
- Each app’s header and icon color change based on defined color in the application table.
- User can add apps by clicking the add button. 
- User can drag and drop each app card. The position is saved automatically.
- User can delete app by clicking the trash icon.
- Default apps are displayed for the first time login. If a user remove all apps, these default apps show up again.
- Administration is available at `http://ip:8000/admin`. You can manage apps and users in here. 
