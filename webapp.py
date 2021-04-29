import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.
x = 0

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1',methods=['GET','POST'])
def renderPage1():
    return render_template('page1.html')
    
@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if 'firstQ' not in session:
        session["firstQ"]=request.form['firstQ']
    return render_template('page2.html')
    
@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if 'secondQ' not in session:
        session["secondQ"]=request.form['secondQ']
    return render_template('page3.html', Q1A = get_q1(session["firstQ"]), Q2A = get_q2(session["secondQ"]), testPercent = get_per(session["firstQ"],session["secondQ"]))



def get_q1(ans):
    if ans == "2":
        return "correct"
    else:
        return "incorrect"
  
def get_q2(ans):
    if ans == "4":
        return "correct"
    else:
        return "incorrect"
 
def get_per(ans1,ans2):
    i = 0
    if ans1 == "2":
        i = i+1
    if ans2 == "4":
        i = i+1
    return ((i/2)*100)
 
    
if __name__=="__main__":
    app.run(debug=True)
