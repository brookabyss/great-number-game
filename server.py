from flask import Flask, render_template, session, redirect
app=Flask(__name__)
app.secret_key="1234"
@app.route('/')
def index():
    import random
    session["num"]=random.randrange(1,100)
    print session["num"]
    return render_template("index.html")
app.run(debug=True)
