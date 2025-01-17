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
    if file is not None:
        file_details = {"FileName": file.name, "FileType": file.type,
        "FileSize": file.size}
        st.write(file_details)

        vttlist = file.getvalue().decode("utf-8").split('\n')
        newvtt = [i for i in vttlist if i]

        currentname = ' '
        currentstring = []
        finallist = []
        for item in newvtt[1:]:
            if item[0] in list(string.ascii_letters):
                item_list = item.split(': ')
                name = item_list[0]
                if name != currentname:
                    finallist.append(f"{' '.join(currentstring)}\n")
                    currentname = name
                    currentstring = [item]
                else:
                    currentstring.append(f"{item_list[1]}")

        finallist.append(f"{' '.join(currentstring)}\n")
        finalitem = '\n'.join(finallist[1:])


with dataoutput:
    st.subheader('Download Clean Transcript Here')

    try:
        if finalitem:
            st.download_button('Download Cleaned File', finalitem, f"{file.name[:-4]}_cleaned.txt", 'Text')
    except:
        st.write("")
