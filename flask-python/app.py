from flask import Flask, render_template
from data_visual import display_data, display_data1, display_data2, input, plot1,plot2

app = Flask(__name__)

@app.route("/Dashboard")
def home():
    return render_template("main.html")

@app.route('/Dashboard/Resources')
def menu():
    data = display_data()
    data1 = display_data1()
    data2=display_data2()
    return render_template('index.html', returnList = data, returnList1=data1, returnList2=data2)

@app.route('/Dashboard/Resources/Visualizations')
def visual():
    visual1 = plot1()
    visual2 = plot2()
    return render_template('visuals.html', visual_1=visual1, visual_2=visual2)
