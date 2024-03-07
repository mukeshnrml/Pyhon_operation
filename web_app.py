import streamlit as st
import pandas as pd 
import time
import dateutil
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('pp.csv')
st.title('My Intrective DA Project')

flg= plt.figure(figsize=(5,5))
plt.bar(df['island'],df['body_mass_g'])
st.pyplot(flg)


















st.title('my first DS app')
st.header('My Database')
st.write('iris')
st.code('for x in a')
st.button('Click')



df = pd.read_csv('pp.csv')

st.title('Full Dataset ')


st.balloons()
st.progress(10)
with st.spinner('loading...'):time.sleep(2)
st.success('this look cool')






if st.button('clickto read dataset'):st.write(df)