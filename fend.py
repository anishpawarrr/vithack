import base64

import streamlit as st
import streamlit_option_menu as om
from PIL import Image

st.set_page_config(page_title='UltraRezNet', page_icon='bi bi-robot', layout='wide', initial_sidebar_state='expanded')

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """, unsafe_allow_html=True )

# add_bg_from_local('logo.png')
c1,c2 = st.columns([2,10])
img = Image.open('logo.png')
with c1:
    st.image(img)

with c2:
    st.write("<h1 style='font-size: 70px;'><b>UltraRezNet</b></h1>", unsafe_allow_html=True)
    st.write("""<h5><i>"Maximize, Accelerate and Simplify"</i></h1>""", unsafe_allow_html=True)
st.write('----')
# st.write("<h1><b>Neural Ninjas</b></h1>", unsafe_allow_html=True)
prompt = st.text_input("Enter product description")




