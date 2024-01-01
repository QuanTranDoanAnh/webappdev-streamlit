import streamlit as st
from PIL import Image

icon = Image.open('helloworld.png')
st.set_page_config(
    page_title='Hello world',
    page_icon=icon,
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello world**'
    }
)
st.sidebar.title('Hello world')
st.title('Hello world')

hide_footer_style = """
<style>
.reportview-container .main footer {visibility: hidden;}
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.sidebar.markdown(f"""<div class="markdown-text-container stText"
style="width: 698px;">
<footer><p></p></footer><div style="font-size: 12px;">
Hello world v 0.1</div>
<div style="font-size: 12px;">Hello world LLC.</div>
</div>""", unsafe_allow_html=True)