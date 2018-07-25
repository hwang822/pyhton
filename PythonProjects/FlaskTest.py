from flask import Flask, redirect, render_template
app = Flask(__name__) 
@app.route('/a-redirect')
def a_redirect():
    """Redirect the user"""
    return redirect("www.cnn.com")

@app.route('/a-template')    
def a_template():
    """Redirect a page using a Jinga2 template"""
    return render_template('a_template')
    
