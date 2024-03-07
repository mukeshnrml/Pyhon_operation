import graphviz
import streamlit as st

a= graphviz.Graph(engine='neato')

a.node('Database')
a.edge('Source','Process') 
a.edge('Process','Source','Unit')   
a.edge('Output','Process')
a.node('Client')
st.graphviz_chart(a)