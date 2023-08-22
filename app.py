
from flask import Flask
import pandas as pd
from flask import render_template_string, render_template
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('Agg')
import io
import base64


app = Flask(__name__)
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
    offence_by_year_count.plot.bar(color='firebrick')  
    plt.xlabel("REPORT_YEAR")
    plt.ylabel("Number of Assaults")
    plt.title("Number of General Assaults by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img():
    # Create plot
    create_plot()
    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    # Convert BytesIO object to base64 string
    img_b64 = base64.b64encode(img.getvalue()).decode()
    return img_b64

def create_plot1():
    offence_by_hood_count[0:30].plot.bar(color='firebrick')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Assaults")
    plt.title("Number of General Assaults by Neighbourhood(140) (1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img1():
    # Create plot
    create_plot1()
    # Save plot to a BytesIO object
    img1 = io.BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_1 = base64.b64encode(img1.getvalue()).decode()
    return img_b64_1

def create_plot2():
    offence_by_hood_count[31:61].plot.bar(color='firebrick')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Assaults")
    plt.title("Number of General Assaults by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img2():
    # Create plot
    create_plot2()
    # Save plot to a BytesIO object
    img2 = io.BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_2 = base64.b64encode(img2.getvalue()).decode()
    return img_b64_2

def create_plot3():
    offence_by_hood_count[61:91].plot.bar(color='firebrick')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Assaults")
    plt.title("Number of General Assaults by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img3():
    # Create plot
    create_plot3()
    # Save plot to a BytesIO object
    img3 = io.BytesIO()
    plt.savefig(img3, format='png')
    img3.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_3 = base64.b64encode(img3.getvalue()).decode()
    return img_b64_3

def create_plot4():    
    offence_by_hood_count[91:121].plot.bar(color='firebrick')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Assaults")
    plt.title("Number of General Assaults by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img4():
    # Create plot
    create_plot4()
    # Save plot to a BytesIO object
    img4 = io.BytesIO()
    plt.savefig(img4, format='png')
    img4.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_4 = base64.b64encode(img4.getvalue()).decode()
    return img_b64_4

def create_plot5():
    offence_by_hood_count[121:141].plot.bar(color='firebrick')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Assaults")
    plt.title("Number of General Assaults by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img5():
    # Create plot
    create_plot5()
    # Save plot to a BytesIO object
    img5 = io.BytesIO()
    plt.savefig(img5, format='png')
    img5.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_5 = base64.b64encode(img5.getvalue()).decode()
    return img_b64_5

def create_plot6():
    b_e_by_year_count.plot.bar(color='b')  
    plt.xlabel("REPORT_YEAR")
    plt.ylabel("Number of B & E's")
    plt.title("Number of Breaking & Enterings by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img6():
    # Create plot
    create_plot6()
    # Save plot to a BytesIO object
    img6 = io.BytesIO()
    plt.savefig(img6, format='png')
    img6.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_6 = base64.b64encode(img6.getvalue()).decode()
    return img_b64_6

def create_plot7():
    b_e_by_hood_count[0:30].plot.bar(color='b')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of B & E's")
    plt.title("Number of Breaking & Enterings by Neighbourhood(140)(1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img7():
    # Create plot
    create_plot7()
    # Save plot to a BytesIO object
    img7 = io.BytesIO()
    plt.savefig(img7, format='png')
    img7.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_7 = base64.b64encode(img7.getvalue()).decode()
    return img_b64_7

def create_plot8():    
    b_e_by_hood_count[31:61].plot.bar(color='b')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of B & E's")
    plt.title("Number of Breaking & Enterings by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img8():
    # Create plot
    create_plot8()
    # Save plot to a BytesIO object
    img8 = io.BytesIO()
    plt.savefig(img8, format='png')
    img8.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_8 = base64.b64encode(img8.getvalue()).decode()
    return img_b64_8

def create_plot9():  
    b_e_by_hood_count[61:91].plot.bar(color='b')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of B & E's")
    plt.title("Number of Breaking & Enterings by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img9():
    # Create plot
    create_plot9()
    # Save plot to a BytesIO object
    img9 = io.BytesIO()
    plt.savefig(img9, format='png')
    img9.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_9 = base64.b64encode(img9.getvalue()).decode()
    return img_b64_9

def create_plot10(): 
    b_e_by_hood_count[91:121].plot.bar(color='b')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of B & E's")
    plt.title("Number of Breaking & Enterings by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img10():
    # Create plot
    create_plot10()
    # Save plot to a BytesIO object
    img10 = io.BytesIO()
    plt.savefig(img10, format='png')
    img10.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_10 = base64.b64encode(img10.getvalue()).decode()
    return img_b64_10

def create_plot11(): 
    b_e_by_hood_count[121:141].plot.bar(color='b')
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of B & E's")
    plt.title("Number of Breaking & Enterings by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img11():
    # Create plot
    create_plot11()
    # Save plot to a BytesIO object
    img11 = io.BytesIO()
    plt.savefig(img11, format='png')
    img11.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_11 = base64.b64encode(img11.getvalue()).decode()
    return img_b64_11    

def create_plot12(): 
    robberies_year_count.plot.bar(color='lawngreen')  
    plt.xlabel("REPORT_YEAR")
    plt.ylabel("Number of Robberies")
    plt.title("Number of Robberies by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img12():
    # Create plot
    create_plot12()
    # Save plot to a BytesIO object
    img12 = io.BytesIO()
    plt.savefig(img12, format='png')
    img12.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_12 = base64.b64encode(img12.getvalue()).decode()
    return img_b64_12 

def create_plot13():    
    robberies_hood_count[0:30].plot.bar(color='lawngreen')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Robberies")
    plt.title("Number of Robberies by Neighbourhood(140)(1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img13():
    # Create plot
    create_plot13()
    # Save plot to a BytesIO object
    img13 = io.BytesIO()
    plt.savefig(img13, format='png')
    img13.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_13 = base64.b64encode(img13.getvalue()).decode()
    return img_b64_13

def create_plot14(): 
    robberies_hood_count[31:61].plot.bar(color='lawngreen')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Robberies")
    plt.title("Number of Robberies by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img14():
    # Create plot
    create_plot14()
    # Save plot to a BytesIO object
    img14 = io.BytesIO()
    plt.savefig(img14, format='png')
    img14.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_14 = base64.b64encode(img14.getvalue()).decode()
    return img_b64_14

def create_plot15():
    robberies_hood_count[61:91].plot.bar(color='lawngreen')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Robberies")
    plt.title("Number of Robberies by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img15():
    # Create plot
    create_plot15()
    # Save plot to a BytesIO object
    img15 = io.BytesIO()
    plt.savefig(img15, format='png')
    img15.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_15 = base64.b64encode(img15.getvalue()).decode()
    return img_b64_15    

def create_plot16():
    robberies_hood_count[91:121].plot.bar(color='lawngreen')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Robberies")
    plt.title("Number of Robberies by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img16():
    # Create plot
    create_plot16()
    # Save plot to a BytesIO object
    img16 = io.BytesIO()
    plt.savefig(img16, format='png')
    img16.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_16 = base64.b64encode(img16.getvalue()).decode()
    return img_b64_16 

def create_plot17():
    robberies_hood_count[121:141].plot.bar(color='lawngreen')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Robberies")
    plt.title("Number of Robberies by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img17():
    # Create plot
    create_plot17()
    # Save plot to a BytesIO object
    img17 = io.BytesIO()
    plt.savefig(img17, format='png')
    img17.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_17 = base64.b64encode(img17.getvalue()).decode()
    return img_b64_17

def create_plot18():
    theft_year_count.plot.bar(color='plum')  
    plt.xlabel("REPORT_YEAR")
    plt.ylabel("Number of Thefts")
    plt.title("Number of Thefts Over Open by Year")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img18():
    # Create plot
    create_plot18()
    # Save plot to a BytesIO object
    img18 = io.BytesIO()
    plt.savefig(img18, format='png')
    img18.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_18 = base64.b64encode(img18.getvalue()).decode()
    return img_b64_18

def create_plot19():
    theft_hood_count[0:30].plot.bar(color='plum')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Thefts")
    plt.title("Number of Thefts Over Open by Neighbourhood(140)(1)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img19():
    # Create plot
    create_plot19()
    # Save plot to a BytesIO object
    img19 = io.BytesIO()
    plt.savefig(img19, format='png')
    img19.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_19 = base64.b64encode(img19.getvalue()).decode()
    return img_b64_19

def create_plot20():
    theft_hood_count[31:61].plot.bar(color='plum')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Thefts")
    plt.title("Number of Thefts Over Open by Neighbourhood(140)(2)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img20():
    # Create plot
    create_plot20()
    # Save plot to a BytesIO object
    img20 = io.BytesIO()
    plt.savefig(img20, format='png')
    img20.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_20 = base64.b64encode(img20.getvalue()).decode()
    return img_b64_20

def create_plot21():
    theft_hood_count[61:91].plot.bar(color='plum')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Thefts")
    plt.title("Number of Thefts Over Open by Neighbourhood(140)(3)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img21():
    # Create plot
    create_plot21()
    # Save plot to a BytesIO object
    img21 = io.BytesIO()
    plt.savefig(img21, format='png')
    img21.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_21 = base64.b64encode(img21.getvalue()).decode()
    return img_b64_21

def create_plot22():
    theft_hood_count[91:121].plot.bar(color='plum')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Thefts")
    plt.title("Number of Thefts Over Open by Neighbourhood(140)(4)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img22():
    # Create plot
    create_plot22()
    # Save plot to a BytesIO object
    img22 = io.BytesIO()
    plt.savefig(img22, format='png')
    img22.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_22 = base64.b64encode(img22.getvalue()).decode()
    return img_b64_22

def create_plot23():
    theft_hood_count[121:141].plot.bar(color='plum')  
    plt.xlabel("NEIGHBOURHOOD_140")
    plt.ylabel("Number of Thefts")
    plt.title("Number of Thefts Over Open by Neighbourhood(140)(5)")
    plt.rcParams["figure.figsize"] = (30, 15)
    plt.rcParams.update({'font.size': 22})

def plot_to_img23():
    # Create plot
    create_plot23()
    # Save plot to a BytesIO object
    img23 = io.BytesIO()
    plt.savefig(img23, format='png')
    img23.seek(0)
    # Convert BytesIO object to base64 string
    img_b64_23 = base64.b64encode(img23.getvalue()).decode()
    return img_b64_23



@app.route('/plot')
def plot():
    # Convert plot to image
    img_b64 = plot_to_img()

    # Render HTML with base64 image
    html = f'<img src="data:image/png;base64,{img_b64}" class="blog-image">'


    return render_template_string(html)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)