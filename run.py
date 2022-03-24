from flask import Flask, render_template, url_for, request, flash, session, redirect, jsonify, json
from numpy import array
import psycopg2, os, random, time
from json import *
from werkzeug.utils import secure_filename
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())
test5 = ''
KEY = os.environ.get("KEY")
date = datetime.today().strftime('%Y-%m-%d')
host = 'localhost'
app = Flask(__name__)
app.secret_key = KEY



def databaseQuery(query):
   
    conn = psycopg2.connect(f" host={host} dbname=postgres user=postgres password=sa")
    cur = conn.cursor()
    cur.execute(query)
    if query.startswith("SELECT"):
        a = cur.fetchone()
        return a
    else:
        print('Query Success!')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/', methods =["GET", "POST"])
def main():
    authenticate = 0
    if  request.method == "POST":
        if  (request.form['loginBtn'] == 'Login'):
            main.username = request.form.get("fname")
            session["user"] = main.username
            password = request.form.get("lname") 
            fetching = databaseQuery(f"SELECT id FROM mainNoteAppUsers WHERE username = '{main.username}' AND pwd = crypt('{password}', pwd);")
            if (fetching is not None):
                htmlLoad2 =  databaseQuery(f"SELECT html from mainNoteAppUsers where username = '{main.username}';")
                renderArrayHTML = " " 
                main.renderJoin = renderArrayHTML.join(htmlLoad2)
                id = htmlLoad2 =  databaseQuery(f"SELECT id from mainNoteAppUsers where username = '{main.username}';")
                databaseQuery(f"UPDATE notebookUsersData Set timeslogin = timeslogin + 1 WHERE id = '{id[0]}';")
                databaseQuery(f"UPDATE notebookUsersData Set lastlogin = {date} WHERE id = '{id[0]}';")
                return render_template("login.html", value=main.renderJoin)
            else:
                time.sleep(2)
                flash('Wrong Username or Password!')      
        else:
            time.sleep(2)
            flash('Wrong Username or Password!')    
    return render_template("index.html")
            
################################################################### LOGIN

@app.route('/login', methods =["GET", "POST"])
def login():
    if ("user" in session):
        htmlLoad2 =  databaseQuery(f"SELECT html from mainNoteAppUsers where username = '{main.username}';")
        renderArrayHTML = " " 
        main.renderJoin = renderArrayHTML.join(htmlLoad2)
        user = session["user"]
       
        if  request.method == "POST":
            login.image = request.files['image']
        
            if login.image.filename.endswith('.jpeg') or login.image.filename.endswith('.jpg') or login.image.filename.endswith('.png'):
                
                login.image.filename = getuserdir.jsdataFile
                login.image.save(os.path.join(f'static/filestorage/{main.username}/', login.image.filename))
                login.result = 'saved'
                htmlLoad2 =  databaseQuery(f"SELECT html from mainNoteAppUsers where username = '{main.username}';")
                renderArrayHTML = " " 
                renderJoin = renderArrayHTML.join(htmlLoad2)
                print('Saved file')

                return render_template("login.html", value=main.renderJoin)
                return render_template('login.html', title="Note Appz", value=main.renderJoin)
                #, jsonfile=json.dumps('helo')
                return render_template("login.html")
            else:
                login.result = 'failed'
                htmlLoad2 =  databaseQuery(f"SELECT html from mainNoteAppUsers where username = '{main.username}';")
                renderArrayHTML = " " 
                renderJoin = renderArrayHTML.join(htmlLoad2)
                return render_template("login.html", value=renderJoin)
             
        return render_template("login.html", value=main.renderJoin)
        
    else: 
        return redirect(url_for("main" ))
####################################################### upload image


@app.route('/uploadImage')
def uploadUrl():
    if ("user" in session):
        username = main.username
        user = session["user"]
        arrayOfsss = os.listdir(f"static/filestorage/{main.username}/") 
        return render_template("uploadimage.html", arrayOfsss=arrayOfsss, username=username)


@app.route('/getusername', methods =["GET", "POST"])
def getusername():
    if ("user" in session):
        user = session["user"]
        return jsonify(main.username) 

@app.route('/getimagedata', methods =["GET", "POST"])
def sendImageDetails():
    if ("user" in session):
        username = main.username
        user = session["user"]
        return jsonify(main.username, login.fileName, login.result) 
    
@app.route('/getuserdir', methods = ['GET', 'POST'])
def getuserdir():
    if ("user" in session):
        getuserdir.jsdataFile = request.get_json('javascriptData') 
        if getuserdir.jsdataFile in os.listdir(f"static/filestorage/{main.username}/") :
            getuserdir.jsdataFile = str(random.randrange(1, 14342340))+getuserdir.jsdataFile
            return jsonify(main.username)
        else:
            return jsonify(main.username)
@app.route('/getuserdir2', methods = ['GET', 'POST'])
def getuserdir2():
    if ("user" in session):
        return jsonify(getuserdir.jsdataFile, main.username)
      

################################################# registration
@app.route('/register', methods =["GET", "POST"])
def register22():
    
    if request.method == "POST":
        if (request.form['registerBtn'] == 'Register'):
            register22.regusername = request.form.get("regusername")
            regpassword = request.form.get("regpassword") 
            regpassword2 = request.form.get("regpassword2") 
            
            fetching = databaseQuery(f"SELECT * from mainNoteAppUsers WHERE username = '{register22.regusername}';")
            
            if (fetching is not None or register22.regusername == "" or len(register22.regusername) < 4 or register22.regusername.isalnum() == False):
                
                    flash('Username is taken or contains special characters!')
            else:
               
                if (regpassword == "" or len(regpassword) < 5): 
                    flash('Password cannot be empty or less than 5 characters!')
               
                elif (regpassword == regpassword2):
                    html = '<!DOCTYPE html> <html lang="en"> <meta charset="UTF-8"> <title>Note App</title> <meta name="viewport" content="width=device-width,initial-scale=1"> <link rel="stylesheet" href="static/styles.css"> <script defer src="static/app.js"></script> <body > <main> <div id="categoryBoxEdit2" class="categoryBoxEdit2"> <textarea  id="titleBoxEdit" maxlength="20">  </textarea> <textarea  id="categoryBoxEdit" >  </textarea> <button id="categoryBoxEditButton" >    save</button> <button id="categoryBoxEditButton2" >    exit</button> </div> <div id="grid-container2" class="grid-container2"> <div class="grid-item2"> <p>  Title </p><input class = "typein" maxlength="20" type="text" id="categoryBox" pattern="[^()/><\][\\\x22,;|]+" > </div> <div class="grid-item2"> <p>  Text  </p><textarea class = "typein2" id="categoryBox2" >  </textarea> </div> <div class="grid-item2"> <button id="btnSave">Submit</button> </div> <div class="grid-item2"> <button id="changePw">Change Password</button> </div> <div class="grid-item2"> <button id="logout">Logout</button> </div> </div> <div id="gridAdd-container"> </div> </main> </body> </html>'
                    databaseQuery(f"INSERT INTO mainNoteAppUsers(username, pwd, HTML) VALUES('{register22.regusername}', crypt('{regpassword}', gen_salt('bf')), '{html}' )")
                
                    os.mkdir(f'static/filestorage/{register22.regusername}')
                    flash('Account created!')
                    
                   
        
                    conn = psycopg2.connect(f" host={host} dbname=postgres user=postgres password=sa")
                    cur = conn.cursor()
                   
                    cur.execute(f"INSERT INTO notebookUsersData (id, created) values ((select id from mainNoteAppUsers where username = '{register22.regusername}'), '{date}');") 
                    
                    conn.commit()
                    cur.close()
                    conn.close()
                 
                    
                    return render_template("index.html")
                else:
                    flash('Passwords do not match!')
    return render_template('register.html')

############################################ SEND DATA TO JS

@app.route('/postmethod', methods = ['GET', 'POST'])
def getPost():
    
    getPost.jsdata = request.get_json('javascriptData') 
    databaseQuery(f"UPDATE mainNoteAppUsers SET html = '{getPost.jsdata}' WHERE username = '{main.username}';")
    return jsonify(getPost.jsdata)

################# CHANGE PASSWORD 
@app.route('/changepw', methods =["GET", "POST"])
def changepw():
    if ("user" in session):
        user = session["user"]

        if request.method == "POST":
            if (request.form['ChangePws'] == 'ChangePws'):
                currpassword = request.form.get("currpassword") 
                regpassword = request.form.get("regpassword") 
                regpassword2 = request.form.get("regpassword2") 
                if (regpassword == "" or len(regpassword) < 5): 
                    flash('Password cannot be empty or less than 5 characters!')
               
                elif (regpassword == regpassword2):
                    fetching = databaseQuery(f"SELECT id FROM mainNoteAppUsers WHERE username = '{main.username}' AND pwd = crypt('{regpassword}', pwd);")
                    if (fetching is None):
                        databaseQuery(f"UPDATE mainNoteAppUsers SET pwd = crypt('{regpassword}', gen_salt('bf')) WHERE username = '{main.username}';")
                        flash('Password was changed!')
                        session.pop("user", None)
                        return redirect(url_for("main"))
                
                    else:
                        flash('Passwords do not match or wrong current password!')
                        

                else:
                    flash('Passwords do not match or wrong current password!')
                    


        return render_template("changepw.html")
    # savink i duombaze return to mai napge to log in su nauju pw
    else: 
        return redirect(url_for("main" ))
        
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main"))

if __name__ == '__main__':
    app.run( debug = True)






