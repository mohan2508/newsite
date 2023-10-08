import streamlit as st

st.write('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/1200x200/?nature,students" class="d-block w-100" alt="...">''',unsafe_allow_html=True)

st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)  
    
bio = st.radio('Jump to',('Online Classes','Contact'))

if bio == 'Online Classes':
    column1,column2,column3 =st.columns(3)
      
    with column1:
        st.title("There will be two sessions ")
        
    with column3:
        st.title('Morning')
        st.write('6.0 am  -  7.00 am')
        st.title('Evening')
        st.write('7.30 pm  -  8.30pm') 
        st.write('8.40 pm -   9.40pm')  
    
        st.write('Interested students can contact over phone or in whatsapp') 
        
else:
    st.write('______________________________________________________________________________________') 
    
    st.write("E-Mail: MohanClasses100@gmail.com")
    st.write("Mobile: 73581 12054")
    st.write("Whatsapp No. : 73581 12054") 
    
    st.write('______________________________________________________________________________________')
           
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
Manageapp{visibility:hidden}
deploy{visibility:hidden}

</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)     