Welcome


# URL Shortener                                   
# File and folder structure                             


    This web app will shorten the URL with the name we provide for it.

    "test_main.py" will be used to test app.

    User's files will be saved into web application path "urlshort/static/user_files"

    Webpages are located under "url/template"

    Main python code is "urlshort.py"


<b> To deploy the project use the following commands</b>

 <table><th>Row</th> <th>Command </th> <th> Description  </th> 
  <tr><td> 1 </td><td>clone the project</td> <td> Navigate to the place you want to deploy your application </td> </tr>
  <tr><td> 2 </td><td>pip3 install pipenv</td> <td> Install pipenv  </td> </tr>
  <tr><td> 3 </td><td>pipenv install</td> <td> Create a virtualized pipenv </td> </tr>
  <tr><td> 4 </td><td>pipenv install flask</td> <td> Install flask on our env </td> </tr>
  <tr><td> 5 </td><td>pipenv shell</td> <td> Enter into shell envrionment </td> </tr>
  <tr><td> 6 </td><td>flask run</td> <td> Run Flask in shell environment </td> </tr>

<b> Set variable and enter into Development mode in Flask</b>
 <table><th>Row</th> <th>windows Command</th> <th>Linux Command </th> <th> Description  </th> 
  <tr><td> 1 </td> <td>set FLASK_APP=urlshort</td> <td>export FLASK_APP=urlshort</td> <td>run shell on pipenv</td> </tr>
  <tr><td> 2 </td> <td>set FLASK_ENV=development</td> <td>export FLASK_ENV=development</td> <td>Set our enviroment into development for realtime feedback</td> </tr>
 

    in case you want to deploy the app in Linux with Nginx and gunicorn

# install nginx in linux 
 
 <table> <th>Ubuntu Command</th> <th>RedHat Command </th> <th> Description  </th> 
  <tr> <td>sudo apt install nginx</td> <td>sudo yum install nginx</td> <td>install nginx in linux </td> </tr>
 
Check Nginx service status in Linux: systemctl status nginx

<b>Install guniform</b>
    pipenv install guniform

<b>run application as service</b>
    gunicorn "urlshort:create_app()" -b 0.0.0.0 --daemon

 
