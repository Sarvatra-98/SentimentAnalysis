# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:28:42 2020

@author: sarva
"""
import pickle
import streamlit as st
#filename='Final_model.sav'
#loaded_model = pickle.load(open(filename, 'rb'))
st.title('Food Review')
#st.beta_set_page_config(page_title='sample', page_icon=':shark:', layout='wide', initial_sidebar_state='expanded')
st.subheader('Sentiment Analyzer')
message=st.text_input('Enter Your Review:')
if st.button('Check Sentiment'):
    #k=loaded_model.predict([message])
    #if(k[0]=='negative'):
    #    st.success("Negative, thank you for bringing this to our attention. We're sorry you had a bad experience.")
    #else:
    #    st.success('Thank you for your valuable feedback')
    #    st.balloons()
