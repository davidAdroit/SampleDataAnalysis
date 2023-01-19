import streamlit as st
import pandas as pd
import plotly.graph_objs as go
#I'm going to use whatever I make here to make a video on, whatever that may be lol.
#https://www.contextures.com/xlsampledata01.html#download <--- sample data source
#https://docs.streamlit.io/library/api-reference

st.header("Office Supplies Data Analysis")


tabs = ['Region Data', 'Representative Data', 'Order Date Info', 'Credits & Sources']
selected_tab = st.sidebar.selectbox("select a tab to view", tabs)
region_data = pd.read_excel("SampleData.xlsx")
data = pd.read_excel("SampleData.xlsx") #did this because i realized the above variable is redundant
if selected_tab == "Region Data":
    st.subheader("Region Data")
    selected_region = st.selectbox("Select a region", region_data["Region"].unique())
    filtered_data_region = region_data[region_data["Region"] == selected_region]
    st.dataframe(filtered_data_region)
    item_counts = filtered_data_region["Item"].value_counts()
    st.write('The chart below shows the amount of items for the data selected')
    st.bar_chart(item_counts)
    region_totals = filtered_data_region.groupby("Region")["Total"].sum()
    st.write("the chart below shows the total cost, it's kind of pointless")
    st.bar_chart(region_totals)
    unit_cost = filtered_data_region["Unit Cost"]

    st.write("The chart below shows : Unit Cost over time")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    unit_cost = filtered_data_region["Unit Cost"].tolist()
    filtered_data_region["Unit Cost"].plot(kind='line')
    st.pyplot()
    st.write("x-axis : Index")
    st.write("y-axis : Unit Cost")

if selected_tab == "Representative Data":
    st.subheader("Representative Data")
    st.success("I used plotly for the data visualization below")
    rep_units = data.groupby("Rep")["Units"].sum()
    trace1 = go.Bar(x=rep_units.index, y=rep_units.values, name = 'Units Sold')
    layout = go.Layout(title = "Units sold by Representative", xaxis=dict(title='Representative'), yaxis=dict(title='Units Sold')
                       )
    fig=go.Figure(data=[trace1], layout=layout)
    st.plotly_chart(fig)
##########################
    rep_totals = data.groupby("Rep")["Total"].sum()
    trace2 = go.Pie(labels=rep_totals.index, values=rep_totals.values, name='Total Cost')
    layout = go.Layout(title="Total Cost by Representative")
    fig = go.Figure(data=[trace2], layout=layout)
    st.plotly_chart(fig)



if selected_tab == "Order Date Info":
    st.subheader("This tab will deal with order date info")
    st.success("I also used plotly for this")
    data["OrderDate"] = pd.to_datetime(data["OrderDate"])
    date_units = data.groupby("OrderDate")["Units"].sum()

    trace1 = go.Scatter(x=date_units.index, y=date_units.values, name='Units Sold',mode="lines+markers")
    layout = go.Layout(title="Units Sold over Time", xaxis=dict(title='Order Date'), yaxis=dict(title='Units Sold'))
    fig = go.Figure(data=[trace1], layout=layout)
    st.plotly_chart(fig)

#### second below

    date_totals = data.groupby("OrderDate")["Total"].sum()
    trace2 = go.Bar(x=date_totals.index, y=date_totals.values, name='Total Cost', marker=dict(color='rgb(55, 83, 109)'))
    layout2 = go.Layout(title="Total Cost over Time", xaxis=dict(title='Order Date'), yaxis=dict(title='Total Cost'))
    fig2 = go.Figure(data=[trace2], layout=layout2)
    st.plotly_chart(fig2)
## third below
    trace3 = go.Scatter(x=data["OrderDate"], y=data["Unit Cost"], mode='markers', name='Unit Cost')
    layout3 = go.Layout(title="Unit Cost by Order Date", xaxis=dict(title='Order Date'), yaxis=dict(title='Unit Cost'))
    fig3 = go.Figure(data=[trace3], layout=layout3)
    st.plotly_chart(fig3)

if selected_tab == "Credits & Sources":
    st.subheader("Credits and Sources Used")
    st.write("I used sample data from this website : https://www.contextures.com/xlsampledata01.html#download")
    st.write("all credits for this data go to : Contextures Inc. 2023")
    st.write("and Deborah Dalgeish for writing the article")
    st.write("david wrote the code")
    st.success("Below are dataframe(s) that contains the raw data used. Both contain the same data")
    st.dataframe(data)
    st.table(data)
