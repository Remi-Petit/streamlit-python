import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def sidebar_page(page):
    st.session_state['page'] = page
    test = page
    print("page : " + page)

with st.sidebar:
    st.button('Accueil', on_click=lambda: sidebar_page("accueil"))
    st.button('Page 2', on_click=lambda: sidebar_page("page2"))

if 'page' not in st.session_state:
    st.session_state['page'] = "test"
if st.session_state['page'] == "accueil":
    st.write("Coucou, c'est la page acceuil")
if st.session_state['page'] == "page2":
    st.write("Coucou, c'est la page 2")
st.session_state

name = st.text_input("Ton nom", "Test")
print("ça fonctionne ?")
if name:
    st.write('Bonjour '+ name +' !')

@st.cache_data
def load_data():
    df = pd.read_csv('./houses.csv')
    #st.write(df)
    fig, ax = plt.subplots()
    ax.scatter(df['size'], df['price'], alpha=0.5)
    st.pyplot(fig)

load_data()



# Créer le DataFrame avec les coordonnées
data = {
    'lat': [48.8566, 45.7640, 43.5297],  # Latitude de Paris, Lyon, Aix-en-Provence
    'lon': [2.3522, 4.8357, 5.4540],    # Longitude de Paris, Lyon, Aix-en-
    'size': [100000, 100000, 100000],
    'color': ['red', 'blue', 'green']
}
df = pd.DataFrame(data)

# Afficher la carte avec st.map
st.map(df)





#temperature = pd.read_csv('./temperatures.csv')
#st.write(temperature)
#st.line_chart(temperature)
#st.line_chart(df)