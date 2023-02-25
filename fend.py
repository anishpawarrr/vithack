import base64
import requests
from streamlit_lottie import st_lottie
import streamlit as st
# import streamlit_option_menu as om
from PIL import Image
from img import giveimg
from pname import givename
from pcap import givecap
from pdesc import givead

st.set_page_config(page_title='UltraRezNet', page_icon='bi bi-robot', layout='wide', initial_sidebar_state='expanded')
def loadurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


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
imgage = Image.open('logo.png')
with c1:
    st.image(imgage)

with c2:
    st.write("<h1 style='font-size: 70px;'><b>UltraRezNet</b></h1>", unsafe_allow_html=True)
    st.write("""<h5><i>"Maximize, Accelerate and Simplify"</i></h1>""", unsafe_allow_html=True)
st.write('----')
# st.write("<h1><b>Neural Ninjas</b></h1>", unsafe_allow_html=True)
lot = loadurl('https://assets5.lottiefiles.com/private_files/lf30_8npirptd.json')
# prompt = st.text_input("Enter product description")
# pltfrm = st.selectbox("Select Platform",['Instagram', 'Facebook', 'Twitter', 'LinkedIn'])
# audi = st.selectbox("Select Audience", ['GenZ', 'Millennials', 'Boomers'])
try:
    with st.form("Query"):
        prompt = st.text_input("Enter Product description")
        pltfrm = st.selectbox("Select Platform", ['Instagram', 'Facebook', 'Twitter', 'LinkedIn'])
        audi = st.selectbox("Select Audience", ['GenZ', 'Millennials', 'Boomers'])
        fsb = st.form_submit_button("Generate Ad")
    if len(prompt)!=0:
        # image

        imgurl = giveimg(prompt)
        # st.write(imgurl)
        # st.write(prompt)
        # st.write(imgurl, unsafe_allow_html=True)
        response = requests.get(imgurl)
        with open('inpimg.jpg', 'wb') as f:
            f.write(response.content)
        imagee = Image.open('inpimg.jpg')
        c1, c2 = st.columns([1, 1])
        with c1:
            st.image(imagee)
            st.subheader("Before")
        with c2:
            st.image(imagee)
            st.subheader("After")


        #names
        # st.write("Starting namefunc")
        namelist = givename(prompt)
        # name = st.selectbox("Select name", namelist)
        st.subheader("Sugessted names ->")
        for i in namelist:
            st.write(i)
        # if 'pro' not in st.session_state:
        #     st.session_state['pro'] = False
        # b = st.button("Select Name")
        # if b:
        #     st.session_state['pro'] = True
        # if st.session_state['pro']:
            # caption

        caption = givecap(imgurl)
        st.subheader("Caption for post ->")
        st.write(caption)

        # ad
        st.subheader("Advertisement ->")
        ad = givead(prompt, pltfrm, audi)
        st.write(ad)



except:
    st.error("Enter product description first")


# c1,c2,c3 = st.columns([10,5,10])
# with c2:
#     st_lottie(lot)




