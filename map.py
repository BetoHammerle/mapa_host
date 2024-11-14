import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")

st.title("Progresso de Campo")

st.sidebar.image('adda-principal-azul.svg',None,110)

st.sidebar.title("Projeto Alto dos Ventos - Macau, RN")


st.sidebar.info(
   
    """
    Equipe em Campo
    - Roberto (ADDA)
     11 93472-8279
    - Julio (ADDA)
     11 99750-0083
     - Caio (ADDA)
     19 98182-4262
    """
)

st.sidebar.image('legenda.svg',None,150)

st.sidebar.title("Registros de Campo")

file = open ('cac.txt',"r",-1)
      
content = file.read()

st.sidebar.info(
content)


st.sidebar.title("Contato")
st.sidebar.info(
    """
    roberto.hammerle@addaconsultoria.com.br
    """
)


df = pd.read_csv('pts.csv')

st.map(df, latitude="lat", longitude="lon",color="cor")
