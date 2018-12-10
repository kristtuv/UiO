import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO

def plot_CO2(start_year, end_year, y_axis_max = None, y_axis_min = None, show_plot = False):
    """Plots the CO2 in the atmosphere between 1751 and 2012.
    y_axis_max and y_axis_min are optional parameters to change the values
    of the y-axis.
    Show_plot = False is used for implementation in web application

    Example:
        plot_CO2(1756, 1839, y_axis_max = None, y_axis_min = None, show_plot = True):

    """
    if not isinstance(start_year, int):
        raise TypeError("start_year must be an int. Example usage: plot_CO2(1816, 1849)")
    if start_year < 1751 or end_year > 2012:
        raise ValueError("start_year and end_year must be between 1751 and 2012")
    if not isinstance(end_year, int):
        raise TypeError("end_year must be an int. Example usage: plot_CO2(1816, 1849)")
    ######################
    ### Importing file ###
    ######################
    CO2 = pd.read_csv("../csv/co2.csv", sep=",")
    CO2 = CO2.set_index("Year")
    start_year_index = CO2.index.get_loc(start_year) #Use Year as index, locate which "Normal" index this corresponds to
    end_year_index = CO2.index.get_loc(end_year)

    #######################
    ##### Ploting CO2 #####
    #######################
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.style.use('ggplot')
    plt.ylabel("Carbon [million tons]")
    plt.title("Carbon in the atmosphere between {} and {}".format(start_year, end_year))

    if y_axis_max and y_axis_min is not None:
        # If y-max and y-min is given, adjust axis
        ax.set_ylim([y_axis_min,y_axis_max])

    #Ploting temperature on y axis and year on x axis
    CO2["Carbon"][start_year_index:end_year_index].plot()

    if show_plot:
        plt.show()
        return
    else:
        # Saving the plot as bytes to be implemented in web
        CO2file = BytesIO()
        plt.savefig(CO2file, format='png')
        CO2file.seek(0)  # rewind to beginning of file
        import base64
        #Encoding the string as base64 to implement on the web.
        #Base64 return a byte-string. Python 3 cares about this. Python 2 does not.
        #Decoding to return a UTF-8 string so it can be used in python 3.
        CO2data_png = base64.b64encode(CO2file.getvalue()).decode()
        return CO2data_png

def plot_temperature(month, start_year, end_year, y_axis_max = None, y_axis_min = None, show_plot = False):
    """
    Plots the temperature of one month in year-interval given.
    start_year and end_year must be between 1816 and 2012.
    Month must be a string with captial first letter.
    y_axis_max and y_axis_min is optional parameters for adjusting the y-axis.
    show_plot = False is used for web implementation
    Example usage:
        plot_temperature('January', 1816, 1849)")
    """

    if not isinstance(month, str):
        raise TypeError("month must be a string, start_year and end_year must be int. Example usage: plot_temperature('January', 1816, 1849)")
    if not isinstance(start_year, int):
        raise TypeError("start_year must be an int. Example usage: plot_temperature('January', 1816, 1849)")
    if not isinstance(end_year, int):
        raise TypeError("end_year must be an int. Example usage: plot_temperature('January', 1816, 1849)")
    if start_year < 1816 or end_year > 2012:
        raise ValueError("start_year and end_year must be between 1816 and 2012")

    ######################
    ### Importing file ###
    ######################
    temperature = pd.read_csv('../csv/temperature.csv', sep=',')
    temperature = temperature.set_index("Year")
    start_year_index = temperature.index.get_loc(start_year) #Use Year as index, locate which "Normal" index this corresponds to
    end_year_index = temperature.index.get_loc(end_year)

    ###############################
    ##### Ploting temperature #####
    ###############################
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    if y_axis_max and y_axis_min is not None:
        # If y-max and y-min is given, ajust axis
        ax.set_ylim([y_axis_min,y_axis_max])

    #Changing style and size of plot
    plt.style.use('ggplot')

    #Ploting temperature on y axis and year on x axis
    temperature[month][start_year_index:end_year_index].plot()
    plt.ylabel(r"Temperature$ \quad [C^{\circ}$]")
    plt.title("Temperature for {} between {} and {}".format(month, start_year, end_year))
    if show_plot:
        plt.show()
        return
    else:
        # Saving the plot as bytes to be implemented in web
        tempfile = BytesIO()
        fig.savefig(tempfile, format='png') #Saving the file as bytes
        tempfile.seek(0)  # rewind to beginning of file
        import base64
        #Encoding the string as base64 to implement on the web.
        #Base64 return a byte-string. Python 3 cares about this. Python 2 does not.
        #Decoding to return a UTF-8 string so it can be used in python 3.
        tempdata_png = base64.b64encode(tempfile.getvalue()).decode()
        return tempdata_png

def plot_CO2_by_country(upper_threshold, lower_threshold, start_year, end_year, show_plot=True):
    """Plots CO2 emissions by country  in the year-interval given.
    start_year and end_year must be between 1960 and 2016.
    Upper and lower threshold finds all the countries with emissions in this interval.
    show_plot = False is used for web implementation.

    The countries on the x-axis will be given in country-code. F.eks USA

    Because the list of
    countries is very comprehensive it is not recommended to plot more than a
    couple of years at the time, if not the plot will be pretty much unreadable.
    It is also recommended to not use to big of an interval for the upper-lower
    threshold for the same reason.

    Example:
        plot_CO2_by_country(25, 15, 2000, 2004, show_plot=True)
    """
    if not isinstance(start_year, int):
        raise TypeError("start_year must be an int. Example usage: plot_CO2_by_country(25, 15, 2000, 2004, show_plot=True)")
    if not isinstance(end_year, int):
        raise TypeError("end_year must be an int. Example usage: plot_CO2_by_country(25, 15, 2000, 2004, show_plot=True)")
    if start_year < 1960 or end_year > 2016:
        raise ValueError("start_year and end_year must be between 1960 and 2016")
    ######################
    ### Importing file ###
    ######################

    CO2_by_country = pd.read_csv("../csv/CO2_by_country.csv", sep=",")
    CO2_by_country = CO2_by_country.set_index("Country Code")


    ##########################
    # Ploting CO2 by country #
    ##########################
    fig = plt.Figure()
    ax = fig.add_subplot(1, 1, 1)

    #Changing style and size of plot
    plt.style.use('ggplot')
    #List of years to plot#
    years = [str(i) for i in range(start_year, end_year + 1)]

    # Finding countries where the upper and lower threshold holds for
    # all every year in our list#
    CO2_by_country = CO2_by_country[(CO2_by_country[years] <= upper_threshold).all(axis=1)]
    CO2_by_country = CO2_by_country[(CO2_by_country[years] >= lower_threshold).all(axis=1)]
    CO2_by_country.plot(y=years,kind="bar")
    plt.ylabel("Carbon, million tons per capita")
    plt.title("Carbon emissions by country\n Upper threshold {}, lower threshold {}".format(upper_threshold, lower_threshold))
    plt.tight_layout()

    if show_plot:
        plt.show()
        return
    else:
        # Saving the plot as bytes to be implemented in web
        CO2_by_country_file = BytesIO()
        plt.savefig(CO2_by_country_file, format='png')
        CO2_by_country_file.seek(0)  # rewind to beginning of file
        import base64
        #Encoding the string as base64 to implement on the web.
        #Base64 return a byte-string. Python 3 cares about this. Python 2 does not.
        #Decoding to return a UTF-8 string so it can be used in python 3.
        CO2_by_country_data_png = base64.b64encode(CO2_by_country_file.getvalue()).decode()
        return CO2_by_country_data_png
if __name__ == '__main__':
    plot_temperature('July', 1816, 2012, show_plot = True)
    plot_CO2(1816, 2012, show_plot = True)
    plot_CO2_by_country(25, 15, 2000, 2001, show_plot = True)
