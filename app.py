from flask import Flask, render_template,request
from tweets import QueryTwitter
import pandas as pd 
import json 

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
	if request.method == "GET":
		(a,b,c)=QueryTwitter("Python")
		return render_template('index.html',doughnut=json.dumps(a),tweet_map=b,sources_plot=json.dumps(c))

	else:
		search = request.form["srch-term"]
		(a,b,c)=QueryTwitter(search)
		return render_template('index.html',doughnut=json.dumps(a),tweet_map=b,sources_plot=json.dumps(c))

	return "<h1>Something went wrong !! </h1>"

if __name__ == "__main__":
	app.run(debug=True, port=5000,threaded=True)