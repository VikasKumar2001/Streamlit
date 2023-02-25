import pandas as pd
import streamlit as st
from matplotlib import image
import matplotlib as plt
import seaborn as sns
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

st.title("Titanic Dashboard")
img = image.imread(IMAGE_PATH)

st.image(img)
df=pd.read_csv(DATA_PATH)


Sex = st.selectbox("Select the Gender", df['sex'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['sex'] == Sex], y="pclass")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['sex'] == Sex], y="pclass")
col2.plotly_chart(fig_2, use_container_width=True)

col3, col4 = st.columns(2)
fig_3 = px.scatter(df[df['sex'] == Sex], y="pclass")
col3.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.bar(df[df['sex'] == Sex], y="pclass")
col4.plotly_chart(fig_4, use_container_width=True)
