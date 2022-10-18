#this is the script where I will try to build this utility
import fileinput
import streamlit as st
import pandas as pd
import webvtt
from io import StringIO

#base = "light"
#primaryColor="#001BFF"
#backgroundColor="#FFFFFF"
#secondaryBackgroundColor="#F0F2F6"
#textColor="#000B62"
#font="monospace"

st.set_page_config('Transcript Cleaner')
header = st.container()
file_upload = st.container()
dataoutput = st.container()

st.markdown(""" <style>
    #MainMenu {visbility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
  

with header:
    st.title('IBM Client Engineering - Web Transcript File Cleaner')
    #st.subheader('IBM Client Engineering')

with file_upload:
    st.subheader('Upload Web Transcript File Here')
    file = st.file_uploader("Choose a file", type='vtt')
    transcript = ""
    finalitem = ' '
    finallist = []
    if file is not None:
        file_details = {"FileName": file.name, "FileType": file.type,
        "FileSize": file.size}
        st.write(file_details)
        vtt = file.getvalue()
        vtt = vtt.decode("utf-8")
        vttlist = []
        newvtt = []
        vttlist = vtt.split('\n')
        for i in vttlist:
            if i:
                newvtt.append(i)
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z','A','B',
        'C','D','E','F','G','H', 'I', 'J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z']
        for item in newvtt:
            if item[0] in alphabet:
                finallist.append(item)

        finalitem = '\n'.join(finallist)

        #vtt = webvtt.read(file)

        #check and see if webvtt works if user inputs file path instead of file directly
        #rd = webvtt.read_buffer(uploaded_file)
        #vtt = uploaded_file.getvalue
        #st.write(vtt)

        #removes blank lines and lines that start with numbers



        #previous = None
        #for line in lines:
            #if line == previous:
                #continue
            #transcript += line + "\n"
            #previous = line


with dataoutput:
    st.subheader('Download Clean Transcript Here')
    st.download_button('Download Cleaned Output', finalitem, 'clean.txt', 'Text')
