import streamlit as st

st.write('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/1200x200/?nature,students" class="d-block w-100" alt="...">''',unsafe_allow_html=True)

column1,column2 = st.columns(2)
with column1:
    st.title('Tutoring Begins With Us') 
with column2:  
    st.write('''
            Welcome to MohanClasses!!! We specialize in providing excellent coaching 
            for Mathematics to students from classes 8th to 10th. Additionally, 
            we offer coaching for CBSE,STATE BOARD and METRICULATION.
            Our coaching is designed to create a supportive and inspirational environment 
            for students.We are passionate about learning and drive to help our studentsto achieve outstanding results. 
 
            We provide personalized attention to each student to help them achieve their full potential. 
            Join us today and make on a journey of academic excellence''') 
    
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
Manage app{visibility:hidden}
Deploy{visibility:hidden}
Header{visibility:hidden}
footer{visibility:hidden}

</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  