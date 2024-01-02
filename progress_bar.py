import streamlit as st
import wget
progress_text = st.empty()
progress_bar = st.progress(0)
def streamlit_progress_bar(current,total,width):
    percent = int((current/total)*100)
    progress_text.subheader('Progress: {}%'.format(percent))
    progress_bar.progress(percent)
wget.download('https://github.com/datarootsio/tutorial-streamlit-demo/blob/master/slides.pdf', bar=streamlit_progress_bar)