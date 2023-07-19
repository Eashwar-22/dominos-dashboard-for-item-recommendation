from flask import Flask,render_template,url_for,jsonify,request,redirect
import pandas as pd

data = pd.read_csv('../Final_Data_Dominos.csv')

app=Flask(__name__)

@app.route("/home")
@app.route("/")
def home_page():
    return render_template('home.html',
                           title="Dominos Pizza Info")

if __name__ == '__main__':
    app.run(debug=True)