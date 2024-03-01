import streamlit as st
import pandas as pd
import plotly.express as px
# Data Set
data = pd.read_csv("avocado_full.csv")
# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
# Horizontal Bar Graph
bar_graph = px.bar(
al_df,
x = "Large Bags",
y = "Date",
title = "Bar Graph",
color="Large Bags",
orientation='h'
)
st.header("Bar Chart")
st.plotly_chart(bar_graph)
