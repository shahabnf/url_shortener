from fileinput import filename
from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint  
# import library to our project, flask , render template folder, request from form, redirect to URL, 
# url_for to redirect or route of url to function, show message to user, abort functionality, 
# use session or cookies in browser , pass list get json file, Add Blueprint feature
import json
import os.path 
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort', __name__)

@bp.route('/')             # redirect or route for home page OR '/'
def home():                 # Define a new function for our code
    return render_template('home.html', codes=session.keys())   # recall another url and pass variable into home page
    # return render_template('home.html', name="Shahab")   # print or return string
    # we pass codes as variable into renderer, and value of codes var is session keys (all keys)

@bp.route('/your-url', methods=['GET','POST'])                         # redirect or route for home page OR '/'
def your_url():                                 # Define a new function for our code
    if request.method == 'POST':
        urls = {}                                       # create json dictionary with empty value 

        if os.path.exists('urls.json'):                 # check if the file exist already
            with open('urls.json') as urls_file:        # open file, alias is urls_file
                 urls = json.load(urls_file)            # load exist dictionary (urls_file) with our file's contents

        if request.form['code'] in urls.keys():         # search in key section, if our code exist in dictionary
            flash('That short name has already been taken. Please select another name.')    # use flash to show message and pass to html page
            return redirect(url_for('urlshort.home'))            # go back to home

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}    # urls dictionary, key is code, value is json, key is url value is url req
        else:
            f = request.files['file'] # 1st save the file, 2nd save in the dictionary
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('D:\\Coding\\python\\url-shortener\\urlshort\\static\\user_files\\' + full_name)
            urls[request.form['code']] = {'file':full_name}

        # save data in JSON file, code as KEY and url as VALUE
        with open('urls.json', 'w') as url_file:    # create or open a file , w as write, if it was successful, alias is url_file
            json.dump(urls, url_file)               # save url to file in json format
        session[request.form['code']] = True        # we enable  session or cookie and save and put code in that
        return render_template('your_url.html', code=request.form['code'])     # recall another url, use form when using POST
        #return render_template('your_url.html', code=request.args['code'])     # use request.args for link include argument 
    else:
        return redirect(url_for('urlshort.home'))
        # return redirect('/')
        # return render_template('home.html')
 

@bp.route('/about')                    # redirect or route for home page OR '/'
def about():                            # Define a new function for our code
    return 'This is a url shortener.'   # print or return string


# create a variable route
@bp.route('/<string:code>')            # strat from home, look for string after / and put it in code variable
def redirect_to_url(code):
    if os.path.exists('urls.json'):                 # if file exist 
        with open('urls.json') as urls_files:       # open and put the file location as alias 
            urls = json.load(urls_files)            # upload file content to urls var
            if code in urls.keys():                 # if code was in urls key
                if 'url' in urls[code].keys():      # and if url was enter code ind as key
                    return redirect(urls[code]['url'])      # show url from json matches the code 
                else:
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))   # return url from location (static + user_files) and look into dictionary, 
                    # url_for: we pass route to this fuction
    
    return abort(404)

@bp.errorhandler(404)          # page not found 404
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))        # pass list of session keys and turn into json 

