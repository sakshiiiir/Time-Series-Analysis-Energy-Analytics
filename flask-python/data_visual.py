import pandas as pd
import plotly.figure_factory as ff 
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import mpld3
#gas = pd.read_excel('Price_NaturalGas.xls', sheet_name="Data 1", skiprows=2)

def display_data():
    gas = pd.read_excel('Price_NaturalGas.xls', sheet_name="Data 1", skiprows=2)
    gas['Date']=pd.to_datetime(gas['Date'])
    gas.index= pd.DatetimeIndex(gas['Date'])
    gas['month']=[gas.index[i].month for i in range(len(gas))]
    gas['year']=[gas.index[i].year for i in range(len(gas))]
    df1=gas[['U.S. Natural Gas Wellhead Price (Dollars per Thousand Cubic Feet)','Date']].dropna().head()
    df = ff.create_table(df1,height_constant=20)
    return plotly.offline.plot(df,output_type='div')


def display_data1():
    elec = pd.read_excel('Electricity.xlsx', sheet_name="Monthly Data", skiprows=10)
    elec['Month']=pd.to_datetime(elec['Month'])
    elec.index= pd.DatetimeIndex(elec['Month'])
    elec['month']=[elec.index[i].month for i in range(len(elec))]
    elec['year']=[elec.index[i].year for i in range(len(elec))]
    df1=elec[['Electricity Net Imports','Month']].dropna().head()
    df = ff.create_table(df1, height_constant=20)
    return plotly.offline.plot(df,output_type='div')


def display_data2():
    pet = pd.read_excel('Petroleum.xls', sheet_name="Data 1", skiprows=2)
    pet['Date']=pd.to_datetime(pet['Date'])
    pet.index= pd.DatetimeIndex(pet['Date'])
    pet['month']=[pet.index[i].month for i in range(len(pet))]
    pet['year']=[pet.index[i].year for i in range(len(pet))]
    df1=pet[['Weekly U.S. Field Production of Crude Oil  (Thousand Barrels per Day)', 'Date']].dropna().head()
    df = ff.create_table(df1, height_constant=20)
    return plotly.offline.plot(df,output_type='div')


def input():
    gas = pd.read_excel('Price_NaturalGas.xls', sheet_name="Data 1", skiprows=2)
    gas['Date']=pd.to_datetime(gas['Date'])
    gas.index= pd.DatetimeIndex(gas['Date'])
    gas['month']=[gas.index[i].month for i in range(len(gas))]
    gas['year']=[gas.index[i].year for i in range(len(gas))]
    df1=gas[['U.S. Natural Gas Wellhead Price (Dollars per Thousand Cubic Feet)', 'Date']].copy().dropna()
    return df1 

def plot1():
    df1=input()
    fig = px.line(df1, x='Date', y='U.S. Natural Gas Wellhead Price (Dollars per Thousand Cubic Feet)')
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
    title='Time Series with Rangeslider for Wellhead Price - Univariate TS PLOT',
    xaxis_title='Date',
    yaxis_title='Price')
    return plotly.offline.plot(fig,output_type='div')


def input3():
    gas = pd.read_excel('Price_NaturalGas.xls', sheet_name="Data 1", skiprows=2)
    gas['Date']=pd.to_datetime(gas['Date'])
    gas.index= pd.DatetimeIndex(gas['Date'])
    gas['month']=[gas.index[i].month for i in range(len(gas))]
    gas['year']=[gas.index[i].year for i in range(len(gas))]
    return gas


"""def plot2():
    #seasonal plot using lineplot function
    gas=input2()
    fig=sns.lineplot(data=gas, 
             x='month', 
             y='U.S. Natural Gas Wellhead Price (Dollars per Thousand Cubic Feet)', 
             hue='year', 
             legend='full')

    # add title
    plt.title('Seasonal plot')

    # move the legend outside of the main figure
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
    plot_html = mpld3.fig_to_html(plt.gcf())
    return plot_html"""

def input2():
    gas = pd.read_excel('Price_NaturalGas.xls', sheet_name="Data 3", skiprows=2)
    gas['Date']=pd.to_datetime(gas['Date'])
    gas.index= pd.DatetimeIndex(gas['Date'])
    gas['month']=[gas.index[i].month for i in range(len(gas))]
    gas['year']=[gas.index[i].year for i in range(len(gas))]
    df1=gas[['U.S. Natural Gas Imports (MMcf)', 'Date', 'U.S. Natural Gas Exports (MMcf)']].copy().dropna()
    return df1

def plot2():
    df1=input2()
    fig = px.scatter(df1, x="U.S. Natural Gas Imports (MMcf)", y="U.S. Natural Gas Exports (MMcf)", 
                   color_continuous_scale=px.colors.sequential.Agsunset, render_mode="webgl",title="Scatter Plot Export Vs Imports for Natural Gas - Multivariate TS PLOT")
    return plotly.offline.plot(fig,output_type='div')

   
    
