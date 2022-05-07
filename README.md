Welcome


# URL Shortener
# File and folder structure


    This web app will shorten the URL with the name we provide for it.

    "test_main.py" will be used to test app.

    User's files will be saved into web application path "urlshort/static/user_files"

    Webpages are located under "url/template"

    Main python code is "urlshort.py"

# -------------------------------------------------------------------------------- #
#                  To deploy the project use the following commands                #
# -------------------------------------------------------------------------------- #


# Navigate to the place you want to deploy your application
1) clone the project

# Install pipenv 
2) pip3 install pipenv

# Create a virtualized pipenv
pipenv install

# Install flask on our env
pipenv install flask

# run shell on pipenv
windows) set FLASK_APP=urlshort
Linux) export FLASK_APP=urlshort

# Set our enviroment into development for realtime feedback
Windows) set FLASK_ENV=development
Linux) export FLASK_ENV=development

# Enter into shell envrionment
pipenv shell

# Run Flask in shell environment
flask run

# -------------------------------------------------------------------------------- #
#       in case you want to deploy the app in Linux with Nginx and gunicorn        #
# -------------------------------------------------------------------------------- #

# install nginx in linux 
Ununtu) sudo apt install nginx
RedHat) sudo yum install nginx
systemctl status nginx

# Install guniform
pipenv install guniform

# run application as service
gunicorn "urlshort:create_app()" -b 0.0.0.0 --daemon

