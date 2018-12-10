from flask import Flask, make_response, render_template, request, send_file
import temperature_CO2_plotter as tcplot
app = Flask(__name__)


@app.route("/plot")
def choose_temp_or_CO2():
    """
    Making the first page of web application where we coose what to plot.
    """
    return render_template("chooseplot.html")

@app.route("/doc")
def documentation():
    """
    Documentationpage made with pydoc
    """
    return render_template("temperature_CO2_plotter.html")

@app.route("/temperature", methods=["GET", "POST"])
def plot_temperature():
    """
    Making temperature plots.
    Default plot is all the data available for January between 1816 and 2012,
    with no changes to the y-axis. Changes to the plot is given on the website.
    """
    try:
        startyeartemp = 1816
        endyeartemp = 2012
        ymaxtemp = None
        ymintemp = None
        month = "January"
        if request.form["StartYearTemp"]:
            startyeartemp = int(request.form["StartYearTemp"])
        if request.form["EndYearTemp"]:
            endyeartemp = int(request.form["EndYearTemp"])
        if request.form["Month"]:
            month = str(request.form["Month"])
        if request.form["YMaxTemp"]:
            ymaxtemp = float(request.form["YMaxTemp"])
        if request.form["YMinTemp"]:
            ymintemp = float(request.form["YMinTemp"])

        temperatureplot = tcplot.plot_temperature(month, startyeartemp, endyeartemp, ymaxtemp, ymintemp, show_plot = False)
        return render_template("plot_temperature.html", temperatureplot = temperatureplot)

    except:
        startyeartemp = 1816
        endyeartemp = 2012
        ymaxtemp = None
        ymintemp = None
        month = "January"
        temperatureplot = tcplot.plot_temperature(month, startyeartemp, endyeartemp, ymaxtemp, ymintemp, show_plot = False)
        return render_template("plot_temperature.html", temperatureplot = temperatureplot)

@app.route("/CO2", methods=["GET", "POST"])
def plot_CO2():
    """
    Making CO2 plots.
    Default plot is all the data available between 1816 and 2012,
    with no changes to the y-axis. Changes to the plot is given on the website.
    """
    try:
        startyearCO2 = 1816
        endyearCO2 = 2012
        ymaxCO2 = None
        yminCO2 = None
        if request.form["StartYearCO2"]:
            startyearCO2 = int(request.form["StartYearCO2"])
        if request.form["EndYearCO2"]:
            endyearCO2 = int(request.form["EndYearCO2"])
        if request.form["YMaxCO2"]:
            ymaxCO2 = float(request.form["YMaxCO2"])
        if request.form["YMinCO2"]:
            yminCO2 = float(request.form["YMinCO2"])

        CO2plot = tcplot.plot_CO2(startyearCO2, endyearCO2, ymaxCO2, yminCO2, show_plot = False)
        return render_template("plot_CO2.html", CO2plot = CO2plot)

    except:
        startyearCO2 = 1816
        endyearCO2 = 2012
        ymaxCO2 = None
        yminCO2 = None
        CO2plot = tcplot.plot_CO2(startyearCO2, endyearCO2, ymaxCO2, yminCO2, show_plot = False)
        return render_template("plot_CO2.html", CO2plot = CO2plot)

@app.route("/CO2bycountry", methods=["GET", "POST"])
def plot_CO2_by_country():
    """
    Making CO2 by country plots.
    Default plot is all the data available for between 2000 and 2004,
    with upper threshold 25 and lower threshold 15 .
    Changes to the plot is given on the website.
    """
    try:
        startyearCO2 = 2000
        endyearCO2 = 2004
        upper_threshold = 25
        lower_threshold = 15
        if request.form["StartYearCO2"]:
            startyearCO2 = int(request.form["StartYearCO2"])
        if request.form["EndYearCO2"]:
            endyearCO2 = int(request.form["EndYearCO2"])
        if request.form["UpperThreshold"]:
            upper_threshold = float(request.form["UpperThreshold"])
        if request.form["LowerThreshold"]:
            lower_threshold = float(request.form["LowerThreshold"])

        CO2plot_by_country = tcplot.plot_CO2_by_country(upper_threshold, lower_threshold, startyearCO2, endyearCO2, show_plot = False)
        return render_template("plot_CO2_by_country.html", CO2plot_by_country = CO2plot_by_country)

    except:
        startyearCO2 = 2000
        endyearCO2 = 2004
        upper_threshold = 25
        lower_threshold = 15
        CO2plot_by_country = tcplot.plot_CO2_by_country(upper_threshold, lower_threshold, startyearCO2, endyearCO2, show_plot = False)
        return render_template("plot_CO2_by_country.html", CO2plot_by_country = CO2plot_by_country)

if __name__ == "__main__":
    app.run(debug=True)
