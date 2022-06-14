import streamlit as st
import pandas as pd
import numpy as np
import os
import requests
import joblib
from lime import lime_tabular
import streamlit.components.v1 as components

# Build app
title_text = 'LIME Explainer Dashboard'
subheader_text = '''Etude de solvabilité du client au prêt immobilier'''

st.markdown(f"<h2 style='text-align: center;'><b>{title_text}</b></h2>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center;'>{subheader_text}</h5>", unsafe_allow_html=True)
st.text("")

# SELECTION DU CUSTOMER_ID
customer_id_list = np.arange(500)
customer_id = st.selectbox('Please select the customer_ID to analyse?', customer_id_list)
st.write('You selected:', customer_id)
print("User selected the customer_id {}".format(customer_id))

# PREDICTION
# using model from api
if customer_id != None :
    url = 'https://rob128.pythonanywhere.com/api'
    r = requests.post(url=url, json={"customer_ID": str(customer_id)})
    response = r.json()
    st.write(response["probabilite"])
    print(response["probabilite"], response["solvabilite"])

    # INTERPRETABILITE
    path = r'C:\Users\vassalr\OneDrive - STMicroelectronics\Documents\Robin\DataScience\Projets\7_ImplémentezUnModèleDeScoring'
    name = "interpretability_list.joblib"
    interpretability_list = joblib.load(os.path.join(path, name))
    html = interpretability_list[customer_id].as_html()
    components.html(html, height=800)


