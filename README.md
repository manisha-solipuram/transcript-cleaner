# Streamlit Transcript (WebVTT File) Cleaner

### Overview

This code cleans up a webvtt format file transcript. This works for both zoom transcript file format. The repository contains a sample file to test the utility with (sample.vtt).

### Example

#### Sample File <br />
<img width="258" alt="Screenshot 2025-01-17 at 9 39 15 AM" src="https://github.com/user-attachments/assets/6414a23b-45ff-4523-bffd-aa23e7702c43" /> <br />

#### Sample File After Cleaning <br />
<img width="261" alt="Screenshot 2025-01-17 at 9 40 15 AM" src="https://github.com/user-attachments/assets/40856106-8f9b-46d3-ab02-b8faf57eaf0c" /><br />

### Instructions to Run
1. Clone this repository
   
2. Setup virtual environment
```
python3 -m venv venv
source venv/bin/activate
``` 
3. Install dependencies
```
pip3 install -r requirements.txt
``` 

4. Run App
```
streamlit run utilityapp.py
``` 

5. If you are getting import errors despite having all of the libraries installed, try running the app with this command instead:
```
python3 -m streamlit run main.py
``` 
