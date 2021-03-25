import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import math
import base64

st.title('SS')

files_coordenadas = st.file_uploader("File Uploader-Coordenadas", type='csv')
if files_coordenadas is not None:
  dfc = pd.read_csv(files_coordenadas, encoding = "ISO-8859-1", delimiter='|')
  if st.checkbox('Ver los datos-Coordenadas'):
    st.write(dfc)

files_esfuerzo = st.file_uploader("File Uploader-Esfuerzo", type='csv')
if files_esfuerzo is not None:
  dfe = pd.read_csv(files_esfuerzo, encoding = "ISO-8859-1", delimiter='|')
  if st.checkbox('Ver los datos-Esfuerzo'):
    st.write(dfe)

if files_coordenadas is not None and files_esfuerzo is not None:
  #Encontrar el punto que hace pareja
  ndfc = dfc.values #los arrays
  ndfe = dfe.values
  SS = []
  backup = []
  for i in range(0,ndfc.shape[0],1):
    for j in range(0,ndfe.shape[0],1):
      d = math.sqrt((ndfc[i,0]-ndfe[j,0])**2 + (ndfc[i,1]-ndfe[j,1])**2 + (ndfc[i,2]-ndfe[j,2])**2) #0=X, 1=Y, 2=Z
      ss = (abs(ndfc[i,3] - ndfe[j,3])/ndfc[i,3])*100 #3=Esfuerzo
      backup.append([d, ss]) 

    backup = np.array(backup)
    posicion = np.where(backup[:,0] == np.amin(backup[:,0])) #tuple
    SS.append([ndfc[i,0], ndfc[i,1], ndfc[i,2], backup[posicion[0][0],1]]) #4=Zona
    backup = []    

  SS = pd.DataFrame(SS, columns = ['X','Y','Z','SS'])
  st.write(SS)
