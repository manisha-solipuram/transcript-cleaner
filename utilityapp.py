import streamlit as st
import string
from io import StringIO

st.set_page_config('Transcript Cleaner')
header = st.container()
file_upload = st.container()
dataoutput = st.container()

st.markdown(""" <style>
   footer {visibility: hidden;}
   </style> """, unsafe_allow_html=True)


with header:
    st.title('Zoom Transcript File Cleaner')

with file_upload:
    st.subheader('Upload Web Transcript File Here')
    file = st.file_uploader("Choose a file", type='vtt')
    if file is not None:
        file_details = {"FileName": file.name, "FileType": file.type,
        "FileSize": file.size}

        vttlist = file.getvalue().decode("utf-8").split('\n')
        newvtt = [i for i in vttlist if i if i[0] in list(string.ascii_letters)][1:]
        print(newvtt)

        currentname = None
        currentstring = []
        finallist = []

        for item in newvtt[1:]:
            name, text = item.split(': ', 1)
            if name != currentname:
                if currentstring:
                    finallist.append(f"{' '.join(currentstring)}\n")
                currentname = name
                currentstring = [item]
            else:
                currentstring.append(text)

        if currentstring:
            finallist.append(' '.join(currentstring))
        finalitem = '\n'.join(finallist)


with dataoutput:
    st.subheader('Download Clean Transcript Here')

    try:
        if finalitem:
            st.download_button('Download Cleaned File', finalitem, f"{file.name[:-4]}_cleaned.txt", 'Text')
    except:
        st.write("")
