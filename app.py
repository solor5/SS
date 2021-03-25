import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import math
import base64

st.title('SS')

files_coordenadas = st.file_uploader("File Uploader-Coordenadas", type=['csv'])
if files_coordenadas is not None:
  if st.checkbox('Ver los datos-Coordenadas'):
    dfc = pd.read_excel(files_coordenadas, encoding = "ISO-8859-1")
    st.write(dfc)

files_esfuerzo = st.file_uploader("File Uploader-Esfuerzo", type=['csv'])
if files_esfuerzo is not None:
  if st.checkbox('Ver los datos-Esfuerzo'):
    dfe = pd.read_csv(files_esfuerzo, encoding = "ISO-8859-1")
    st.write(dfe)

if files_coordenadas is not None and files_esfuerzo is not None:
  #Encontrar el punto que hace pareja
  ndfc = dfc.values() #los arrays
  ndfe = dfe.values()
  error = st.number_input("Error", format="%.3f")
  SS = []
  for i in range(0,ndfe.shape[0],1):
    for j in range(0,ndfc.shape[0],1):
      d = math.sqrt((ndfc[j,0]-ndfe[i,0])**2 + (ndfc[j,1]-ndfe[i,1])**2 + (ndfc[j,2]-ndfe[i,2])**2) #0=X, 1=Y, 2=Z
      if d <= error:
        ss = ((ndfc[j,3] - ndfe[i,3])/ndfc[j,3])*100 #3=Esfuerzo
        SS.append([ndfc[j,0], ndfc[j,1], ndfc[j,2], ss, ndfc[j,4]]) #4=Zona

  SS = pd.DataFrame(SS, columns = ['X','Y','Z','SS','Zona'])
  st.write(SS)
