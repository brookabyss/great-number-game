from flask import Flask, render_template, session, redirect, request
app=Flask(__name__)
app.secret_key="1234"
@app.route('/')
def index():
    import random
    session["num"]=random.randrange(1,100)
    print session["num"]
    return render_template("index.html")
@app.route('/number', methods=['POST'])
def checker():
   session['user']=int(request.form['user'])
   return redirect('/')

@app.route('/reset')
def reset():
    session.pop('user')
    return redirect('/')
app.run(debug=True)
