import fileinput
import streamlit as st
import pandas as pd
import string
import webvtt
from io import StringIO

st.set_page_config('Transcript Cleaner')
header = st.container()
file_upload = st.container()
dataoutput = st.container()

st.markdown(""" <style>
   footer {visibility: hidden;}
   </style> """, unsafe_allow_html=True)
  

with header:
    st.title('WebVTT Transcript File Cleaner')

with file_upload:
    st.subheader('Upload Web Transcript File Here')
    file = st.file_uploader("Choose a file", type='vtt')
    finalitem = ' '
    finallist = []
    if file is not None:
        file_details = {"FileName": file.name, "FileType": file.type,
        "FileSize": file.size}
        st.write(file_details)
        vtt = file.getvalue()
        vtt = vtt.decode("utf-8")
        # vttlist = []
        newvtt = []
        vttlist = vtt.split('\n')
        newvtt = [i for i in vttlist if i]
        # for i in vttlist:
        #     if i:
        #         newvtt.append(i)

        currentname = ' '
         
        for item in newvtt[1:]:
            if '"' in item:
               sp = item.split('"')
               name = sp[1]
               if name != currentname:
                  finallist.append(name)
                  currentname = name
            elif item[0] in list(string.ascii_letters):
                finallist.append(item)

        finalitem = '\n'.join(finallist)


with dataoutput:
    st.subheader('Download Clean Transcript Here')
    st.download_button('Download Cleaned Output', finalitem, 'clean.txt', 'Text')
