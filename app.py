# Important: Remember that every time we change the widget value, 
# the whole app runs from top to bottom.

import streamlit as st
from bert import QA
import time
from bs4 import BeautifulSoup
import requests
from tika import parser
import glob
import os

def main():
    st.title('#TLDR')

    # Load bert model once and cache it
    with st.spinner("Loading deep learning model..."):
        @st.cache(allow_output_mutation=True, show_spinner=False)
        def load_model(_):
            
            model = QA('model')
            return model
        model = load_model(10)

    st.write("No time to read a whole chunk of text?")
    
    app_mode = st.selectbox("Choose the data source",
    ["", "Copy and Paste Here", "URL", "PDF"])

    if app_mode == "Copy and Paste Here":
        doc = st.text_area('Paste the text below')
        if doc!='':
            q = st.text_input('Question')
            answer = model.predict(doc,q)
            print_ans(answer,q)
    
    elif app_mode == "URL":
        page_link = st.text_input('URL')
        if page_link != '':
            try:
                doc = read_url(page_link)
                q = st.text_input('Question')
                answer = model.predict(doc,q)
                print_ans(answer,q)
            except:
                st.write("Please enter an existing URL.")

    elif app_mode == "PDF":
        st.text("\nEnsure that the PDF is in the PDF folder of working directory")
        pdf_dict = read_pdf()
        pdf_choice = st.selectbox("Choose the PDF", list(pdf_dict.keys()))
        doc = pdf_dict[pdf_choice]
        q = st.text_input('Question')
        answer = model.predict(doc,q)
        print_ans(answer,q)

def print_ans(answer, q):
    """
    Prints the answer and confidence as progress bar
    """
    if q != '':
        st.text(" ")
        st.text(" ")
        st.subheader("Answer:")
        st.write(answer['answer'])
        st.write("Confidence: ", int(answer['confidence']*100), "%")
        st.progress(int(answer['confidence']*100))    


def read_url(page_link):
    """
    Returns the scraped text from a given URL
    """
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    textContent = []
    for i in range(0, 20):
        paragraphs = page_content.find_all("p")[i].text
        textContent.append(paragraphs)

    return str(textContent)


def read_pdf():
    """
    Returns a dictionary of {<filename> : <text>}
    from stored PDFs
    """
    # pdf is stored in <working directory>/PDF
    PATH = os.getcwd()
    PDF_PATH = PATH + "/PDF"
    os.chdir(PDF_PATH)

    pdf_dict = {}

    for filename in glob.glob("*.pdf"):
        raw = parser.from_file(filename)
        doc = raw['content']
        pdf_dict[filename] = doc

    # return to <working directory> 
    os.chdir(PATH)

    # Note: if there multiple PDFs in the folder, it'll only return the last
    # To improve in future
    return pdf_dict
       

if __name__ == "__main__":
    main()

