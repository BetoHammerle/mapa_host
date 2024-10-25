import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")

st.title("Progresso de Campo")

st.sidebar.image('adda-principal-azul.svg',None,110)

st.sidebar.title("Projeto Altos Ventos - RN")

st.sidebar.info(
   
    """
    - ADDA Consultoria: <https://addaconsultoria.com.br/>
    - SR Energia: <http://www.srenergia.com/>
    """
)

st.sidebar.title("Registros de Campo")

file = open ('D:\streamlit\README.md',"r",-1)
      
content = file.read()

st.sidebar.info(
content)


st.sidebar.title("Contato")
st.sidebar.info(
    """
    roberto.hammerle@addaconsultoria.com.br
    """
)


df = pd.read_excel('pts.xlsx')

st.map(df)
