import streamlit as st

st.write('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/1200x200/?nature,sunrise" class="d-block w-100" alt="...">''',unsafe_allow_html=True)

    

column1,column2 = st.columns(2)

with column1:
    st.title('Welcome to MohanClasses')
    st.markdown("[Watch Videos..........](https://www.youtube.com/channel/UCth-wWcoRoR-1wx4YO0O_Bw)") 
with column2:
    st.write('''
            MohanClasses is the coaching centre for CBSE,STATE and METRICULATION board students in 
            the areas of Kelambakkam,our commitment to providing a good academic education to our students. 
            
            MohanClasses give a more individualised experience with knowledgeable instructors who can explain concepts in more detail,
            answer questions,and provide new perspectives. Students benefit from this since they are better able to understand the material and use it correctly on 
            tests.
              
            Never force students to learn under pressure, and provides a planned way of 
            studying, along with quick tips and smart-study advice.Math tutoring gives your child exactly what they need to help supplement
            in-class learning.
             
            If you are looking for the best Maths coaching classes in Kelambakkam,MohanClasses is the top choice.  
            Customized study plans, and personalized attention, MohanClasseshelps students improve their Math skills quickly and effectively.''')    
    

