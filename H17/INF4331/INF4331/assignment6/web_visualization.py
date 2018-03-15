from flask import Flask
from flask import render_template, request
from temperature_CO2_plotter import plot_temperature, plot_CO2
import requests

app = Flask(__name__)

@app.route("/")#, methods=['POST'])
def root():
	return render_template("root.html")

"""
def temp():
	plot_temperature('June', 1816, 2012)
	plot_CO2(1751, 2012)
	return render_template("test.html")
"""


@app.route("/plots", methods=['GET', 'POST'])
def plots():
	# try:
	# 	if request.form["startyear"]:
	# 		start_yearTemp = int(request.form["startyear"])
	# 	if request.form["endyearTemp"]:
	# 		end_yearTemp = int(request.form["endyear"])
	# 	return render_template("test.html")
	# except:
	return render_template("plots.html")

@app.route("/plots/temp_plot", methods =["GET", "POST"])

def plot():
	#r = requests.post("http://127.0.0.1:5000/plots")
	# if request.form["startyear"]:
	# 	start_yearTemp = int(request.form["startyear"])
	# if request.form["endyearTemp"]:
	# 	end_yearTemp = int(request.form["endyear"])
	# #plot_temperature('June', start_yearTemp, end_yearTemp)
	return "penis"

@app.route("/plots/error_temp")

def error_temp():
	return render_template("error_temp.html")

if __name__ == "__main__":
	app.run(debug=True)
