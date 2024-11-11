<h1 align="center"> 👋 This is my Olx project and it's clone of one of the pages of olx.</h1>
<h3 align="center">A passionate full-stack developer from Uzbekistan</h3>
<h1> Intro </h1>


## Before start pull my files to your lap top.
    git clone git@github.com:bobur22/Olx-drf
## And then open your terminal and start creating by env file
      python3 -m venv .env
## then activate env file.
## And after that start with installing requirements.txt
    pip install -r requirements.txt
## then make a migrations.
    ./manage.py makemigrations

## and after that migrate it.
    ./manage.py migrate

## before runing server create super user in order to open admin panel.
    ./manage.py createsuperuser

## then finally start project.
    ./manage.py runserver

#Then you can open website on your local host but you should remember that when you want to authenticate by facebook, google and register you have to edit settings there.
## and project is ready.
