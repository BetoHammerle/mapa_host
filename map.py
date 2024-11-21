import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")

st.title("Progress Map")

st.sidebar.image('adda-principal-azul.svg',None,115)

st.sidebar.title("Project Alto dos Ventos - Macau, RN")


st.sidebar.info(

    """
    Field Tema
    Roberto
    Caio
    Solonildo
    """
)

st.sidebar.image('legenda.svg',None,150)

st.sidebar.title("Field Work Log")

file = open ('cac.txt',"r",-1)
      
content = file.read()

st.sidebar.info(
content)


st.sidebar.title("Contact information")
st.sidebar.info(
    """
    roberto.hammerle@addaconsultoria.com.br
    """
)


df = pd.read_csv('pts.csv')

st.map(df, latitude="lat", longitude="lon",color="cor")
