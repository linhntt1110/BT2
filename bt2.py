import streamlit as st
import pandas as pd
import plotly.express as px

# Data Set
data = pd.read_csv("avocado_full.csv")
# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
#Bar
bar_graph = px.bar(
y = al_df["Date"],
x = al_df["Large Bags"],
title = "Bar Graph",
color=al_df["Large Bags"]
),
orientation='h'
)
st.header("Bar Chart")
st.plotly_chart(bar_graph)
