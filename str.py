import streamlit as st 
import pandas as pd 
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


a = {
    'name':['Nrml','Mks'],
    'marks':[20,40]
}
st.write(a)


df = pd.read_csv('pp.csv')
st.dataframe(df, height=350, width=800)
st.write("This is Dataset of Student")

#if st.button('read dataset'):st.write(df)

# df1= df.drop(['sex','island'], axis='columns')
# df1
# st.write("Droped Two Column")

fig = plt.figure(figsize=(10,8))
plt.bar(df['species'],df['body_mass_g'])
st.pyplot(fig)

if st.sidebar.button('Side'):
    st.write(df)


    date = st.date_input('Pick a date')

    

