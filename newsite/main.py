import streamlit as st
from PIL import Image 
from streamlit_option_menu import option_menu


st.set_page_config("MohanClasses",
                   page_icon="")

st.markdown('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/1200x200/?nature,nature" class="d-block w-100" alt="...">''',unsafe_allow_html=True)

st.write('____________________________________________________________________________________________________________________')
st.write('____________________________________________________________________________________________________________________')
column1,column2,column3 = st.columns(3)


with column1:
        st.title('Welcome to MohanClasses')
with column3:
        st.write('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/400x300/?nature,students" class="d-block w-100" alt="...">''',unsafe_allow_html=True)
        
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
Manage app{visibility:hidden}
deploy{visibility:hidden}
Header{visibility:hidden}
footer{visibility:hidden}

</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)        
   








