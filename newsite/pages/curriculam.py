import streamlit as st

st.write('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/1200x200/?nature,water" class="d-block w-100" alt="...">''',unsafe_allow_html=True)

column1,column2 = st.columns(2)
with column1:
    st.title('A Commitment to Excellence') 
with column2:  
    st.write('''
            At MohanClasses!!, we make great efforts to provide our students 
            with having a wide scope that offers engaging and 
            fulfilling experiences, preparing them for a rich social and cultural life. 


            At MohanClasses, we take pride in offering personalized 
            attention to each of our students, whether through our textbooks or 
            hands-on training. Our goal is to help every student to expose in their 
            subjects, achieve better scores.''')            
 
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
Manageapp{visibility:hidden}
deploy{visibility:hidden}

</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 