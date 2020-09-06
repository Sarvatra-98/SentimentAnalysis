# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:28:42 2020

@author: sarva
"""
import pickle
import streamlit as st
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('image.jpg')
filename='Final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
st.title('Food Review')
#st.beta_set_page_config(page_title='sample', page_icon=':shark:', layout='wide', initial_sidebar_state='expanded')
st.subheader('Sentiment Analyzer')
message=st.text_input('Enter Your Review:')
if st.button('Check Sentiment'):
    k=loaded_model.predict([message])
    if(k[0]=='negative'):
        st.success("Negative, thank you for bringing this to our attention. We're sorry you had a bad experience.")
    else:
        st.success('Positive,Thank you for your valuable feedback')