
from flask import Flask
import pandas as pd
from flask import render_template_string, render_template
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('Agg')
import io
from io import BytesIO
import base64


app = Flask(__name__)
mp.use('Agg') 
assault_metadata_path = "/Users/anastasiiaskrypnyk/Desktop/GitHub/project-3_old/Assault_Open_Data.csv"
break_and_enter_metadata_path = "/Users/anastasiiaskrypnyk/Desktop/GitHub/project-3_old/Break_and_Enter_Open_Data.csv"
robbery_metadata_path = "/Users/anastasiiaskrypnyk/Desktop/GitHub/project-3_old/Robbery_Open_Data.csv"
theft_over_open_metadata_path = "/Users/anastasiiaskrypnyk/Desktop/GitHub/project-3_old/Theft_Over_Open_Data.csv"

assault_metadata = pd.read_csv(assault_metadata_path)
break_and_enter_metadata = pd.read_csv(break_and_enter_metadata_path)
robbery_metadata = pd.read_csv(robbery_metadata_path)
theft_over_open_metadata = pd.read_csv(theft_over_open_metadata_path)

offence_by_year_count = assault_metadata["REPORT_YEAR"].value_counts()
offence_by_hood_count = assault_metadata["NEIGHBOURHOOD_140"].value_counts()

b_e_by_year_count = break_and_enter_metadata["REPORT_YEAR"].value_counts()
b_e_by_hood_count = break_and_enter_metadata["NEIGHBOURHOOD_140"].value_counts()

robberies_year_count = robbery_metadata["REPORT_YEAR"].value_counts()
robberies_hood_count = robbery_metadata["NEIGHBOURHOOD_140"].value_counts()

theft_year_count = theft_over_open_metadata["REPORT_YEAR"].value_counts()
theft_hood_count = theft_over_open_metadata["NEIGHBOURHOOD_140"].value_counts()

@app.route('/')
def home():
    return "Hello, Flask!"

def create_plot():
    plt.figure()
    offence_by_year_count.plot.barh(color='firebrick')  
    plt.xlabel("Number of Assaults Recorded")
    plt.ylabel("Report Year")
    plt.title("Number of General Assault Cases by Year")
    # plt.rcParams["figure.figsize"] = (30, 15)
    # plt.rcParams.update({'font.size': 22})

    line_file = './static/images/create_plot.png'
    plt.savefig(line_file, bbox_inches = 'tight')

    return line_file

def create_plot1():
    plt.figure()
    offence_by_hood_count[0:30].plot.barh(color='firebrick')  
    plt.xlabel("Number of Assaults Recorded")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Assaults Recorded by Neighbourhood(140) (1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file1 = './static/images/create_plot1.png'
    plt.savefig(line_file1, bbox_inches = 'tight')

    return line_file1

def create_plot2():
    plt.figure()
    offence_by_hood_count[31:61].plot.barh(color='firebrick')  
    plt.xlabel("Number of Assaults Recorded")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Assaults Recorded by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file2 = './static/images/create_plot2.png'
    plt.savefig(line_file2, bbox_inches = 'tight')

    return line_file2

def create_plot3():
    plt.figure()
    offence_by_hood_count[61:91].plot.barh(color='firebrick')  
    plt.xlabel("Number of Assaults Recorded")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Assaults Recorded by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file3 = './static/images/create_plot3.png'
    plt.savefig(line_file3, bbox_inches = 'tight')

    return line_file3

def create_plot4():    
    plt.figure()
    offence_by_hood_count[91:121].plot.barh(color='firebrick')  
    plt.xlabel("Number of Assaults Recorded")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Assaults Recorded by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file4 = './static/images/create_plot4.png'
    plt.savefig(line_file4, bbox_inches = 'tight')

    return line_file4

def create_plot5():
    plt.figure()
    offence_by_hood_count[121:141].plot.barh(color='firebrick')  
    plt.xlabel("Number of Assaults Recorded")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Assaults Recorded by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file5 = './static/images/create_plot5.png'
    plt.savefig(line_file5, bbox_inches = 'tight')

    return line_file5

def create_plot6():
    plt.figure()
    b_e_by_year_count.plot.barh(color='b')  
    plt.xlabel("Number of B & E's")
    plt.ylabel("Report Year")
    plt.title("Number of Breaking & Entering Cases by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file6 = './static/images/create_plot6.png'
    plt.savefig(line_file6, bbox_inches = 'tight')

    return line_file6

def create_plot7():
    plt.figure()
    b_e_by_hood_count[0:30].plot.barh(color='b')  
    plt.xlabel("Number of B & E's")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Breaking & Entering Cases by Neighbourhood(140)(1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file7 = './static/images/create_plot7.png'
    plt.savefig(line_file7, bbox_inches = 'tight')

    return line_file7

def create_plot8():    
    plt.figure()
    b_e_by_hood_count[31:61].plot.barh(color='b')  
    plt.xlabel("Number of B & E's")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Breaking & Entering Cases by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file8 = './static/images/create_plot8.png'
    plt.savefig(line_file8, bbox_inches = 'tight')

    return line_file8

def create_plot9(): 
    plt.figure() 
    b_e_by_hood_count[61:91].plot.barh(color='b')  
    plt.xlabel("Number of B & E's")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Breaking & Entering Cases by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file9 = './static/images/create_plot9.png'
    plt.savefig(line_file9, bbox_inches = 'tight')

    return line_file9

def create_plot10(): 
    plt.figure()
    b_e_by_hood_count[91:121].plot.barh(color='b')  
    plt.xlabel("Number of B & E's")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Breaking & Entering Cases by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file10 = './static/images/create_plot10.png'
    plt.savefig(line_file10, bbox_inches = 'tight')

    return line_file10

def create_plot11(): 
    plt.figure()
    b_e_by_hood_count[121:141].plot.barh(color='b')
    plt.xlabel("Number of B & E's")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Breaking & Entering Cases by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file11 = './static/images/create_plot11.png'
    plt.savefig(line_file11, bbox_inches = 'tight')

    return line_file11    

def create_plot12():
    plt.figure()
    robberies_year_count.plot.barh(color='lawngreen')  
    plt.xlabel("Number of Robberies")
    plt.ylabel("Report Year")
    plt.title("Number of Robberies Recorded by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file12 = './static/images/create_plot12.png'
    plt.savefig(line_file12, bbox_inches = 'tight')

    return line_file12 

def create_plot13():    
    plt.figure()
    robberies_hood_count[0:30].plot.barh(color='lawngreen')  
    plt.xlabel("Number of Robberies")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Robberies by Neighbourhood(140)(1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file13 = './static/images/create_plot13.png'
    plt.savefig(line_file13, bbox_inches = 'tight')

    return line_file13

def create_plot14(): 
    plt.figure()
    robberies_hood_count[31:61].plot.barh(color='lawngreen')  
    plt.xlabel("Number of Robberies")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Robberies by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file14 = './static/images/create_plot14.png'
    plt.savefig(line_file14, bbox_inches = 'tight')

    return line_file14

def create_plot15():
    plt.figure()
    robberies_hood_count[61:91].plot.barh(color='lawngreen')  
    plt.xlabel("Number of Robberies")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Robberies by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file15 = './static/images/create_plot15.png'
    plt.savefig(line_file15, bbox_inches = 'tight')

    return line_file15    

def create_plot16():
    plt.figure()
    robberies_hood_count[91:121].plot.barh(color='lawngreen')  
    plt.xlabel("Number of Robberies")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Robberies by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file16 = './static/images/create_plot16.png'
    plt.savefig(line_file16, bbox_inches = 'tight')

    return line_file16 

def create_plot17():
    plt.figure()
    robberies_hood_count[121:141].plot.barh(color='lawngreen')  
    plt.xlabel("Number of Robberies")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Robberies by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file17 = './static/images/create_plot17.png'
    plt.savefig(line_file17, bbox_inches = 'tight')

    return line_file17

def create_plot18():
    plt.figure()
    theft_year_count.plot.barh(color='plum')  
    plt.xlabel("Number of Thefts")
    plt.ylabel("Report Year")
    plt.title("Number of Theft Cases Recorded by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file18 = './static/images/create_plot18.png'
    plt.savefig(line_file18, bbox_inches = 'tight')

    return line_file18

def create_plot19():
    plt.figure()
    theft_hood_count[0:30].plot.barh(color='plum')  
    plt.xlabel("Number of Thefts")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Theft Cases Recorded by Neighbourhood(140)(1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file19 = './static/images/create_plot19.png'
    plt.savefig(line_file19, bbox_inches = 'tight')

    return line_file19

def create_plot20():
    plt.figure()
    theft_hood_count[31:61].plot.barh(color='plum')  
    plt.xlabel("Number of Thefts")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Theft Cases Recorded by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file20 = './static/images/create_plot20.png'
    plt.savefig(line_file20, bbox_inches = 'tight')

    return line_file20

def create_plot21():
    plt.figure()
    theft_hood_count[61:91].plot.barh(color='plum')  
    plt.xlabel("Number of Thefts")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Theft Cases Recorded by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file21 = './static/images/create_plot21.png'
    plt.savefig(line_file21, bbox_inches = 'tight')

    return line_file21

def create_plot22():
    plt.figure()
    theft_hood_count[91:121].plot.barh(color='plum')  
    plt.xlabel("Number of Thefts")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Theft Cases Recorded by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file22 = './static/images/create_plot22.png'
    plt.savefig(line_file22, bbox_inches = 'tight')

    return line_file22

def create_plot23():
    plt.figure()
    theft_hood_count[121:141].plot.barh(color='plum')  
    plt.xlabel("Number of Thefts")
    plt.ylabel("NEIGHBOURHOOD_140")
    plt.title("Number of Theft Cases Recorded by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

    line_file23 = './static/images/create_plot23.png'
    plt.savefig(line_file23, bbox_inches = 'tight')

    return line_file23



@app.route('/plot')
def compute():
    plots = [
        create_plot(), 
        create_plot1(),
        create_plot2(),
        create_plot3(),
        create_plot4(),
        create_plot5(),
        create_plot6(),
        create_plot7(),
        create_plot8(),
        create_plot9(),
        create_plot10(),
        create_plot11(),
        create_plot12(),
        create_plot13(),
        create_plot14(),
        create_plot15(),
        create_plot16(),
        create_plot17(),
        create_plot18(),
        create_plot19(),
        create_plot20(),
        create_plot22(),
        create_plot23()
    ]
    return render_template('index.html',
                           plots=plots)

    
if __name__ == '__main__':
    app.run(debug=True)