# Streamlit Transcript (WebVTT File) Cleaner

### Overview

This utility automatically cleans up raw meeting transcript data, organizing the text by speaker for a more readable and polished output. This utility works specifically for the zoom meeting file transcript format and outputs a .txt file. Whether you’re working with meeting notes, catching up on a missed meeting, or preparing a presentation, this tool streamlines the process, saving you time and effort. The repository also includes a sample file (sample.vtt) for easy testing and quick setup.

### Example

#### Sample File <br />
<img width="645" alt="Screenshot 2025-01-17 at 12 44 44 PM" src="https://github.com/user-attachments/assets/0ff99397-4530-4bd9-a78c-32c75820b9e3" />
<br />

#### Sample Cleaned Output File <br />
<img width="645" alt="Screenshot 2025-01-17 at 12 45 11 PM" src="https://github.com/user-attachments/assets/e6ce92ee-b4d1-454e-bb1a-6cce7b2f01cb" />
<br />

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
