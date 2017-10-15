from flask import * 
SECRET_KEY = 'Chocolate chip cookies'
 
app = flask(__name__) 
app.config.from_object(__name__)
@app.route("/login", methods = ['GET', 'POST'])    
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "fish" or request.form['password'] == 'chips':
            session['logged_in'] = True
            return redirect(url_for('secret'))
        else:
            error = "Wrong username or password, dude"
 
    return render_template("login.html", error=error)
	
	@app.route("/secret")    
def secret():
    return render_template("secret.html")
 
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))