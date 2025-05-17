import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    select = option_menu(
        menu_title="RESUME",
        options=["Biodata","Summary","education","skills","project","languages known","certification"],
        icons=["file-earmark-person","balloon","file-person","eye-fill","cast","check-square","award"]
     )
if select=="Biodata":
    st.title("ARUNACHALAM N")
    st.write("Python programmer")
    st.write("madurai(Dt),Tamil nadu,India")
    st.write("email:arunachalam192004@gmail.com")
    st.write("mobile:6381823682")

elif select=="Summary":
    st.header("Highly motivated recent graduate with a strong foundation in python programming.")
             

elif select=="education":
    st.title("Bachelor of engineering(Electronics and communication engineering)")
    st.write("Sethu institute of Technology")
    st.write("CGPA:8.144")
    st.write("HSC:percentage:68.5% Srividyalayam Matric Hr.Sec.School")
    st.write("SSLC:percentage:61.6% Srividyalayam Matric Hr.Sec.School")
    
elif select=="skills":
    st.header("python programming")
    st.header("streamlit")

elif select=="project":
    st.header("**IOT BASED SMART MINING HELMET USING LORAWAN TECHNOLOGY**")

elif select=="languages known":
    st.header("_ENGLISH_")
    st.header("_TAMIL_")

elif select=="certification":
    st.header("1)NPTEL-INTERNET OF THINGS")
    st.header("2)NPTEL-INTRODUCTION TO INDUSTRY 4.0 AND INDUSTRIAL INTERNET OF THINGS")
    st.header("3)INFOSYS SPRING BOARD-BASICS OF PYTHON")


# st.title("ttt")
# st.title("vinsup infotech")
# st.header("vinsup infotech")
# st.subheader("vinsup infotech")
# st.text("vinsup infotech")
# st.write("**vinsup infotech**")
# st.badge("add",color="red")
# st.metric("python","20","20%")
# st.latex("a+b=a+b+2ab")
# st.code("""
# a=10
# b=15
# c=a+b
# print(c)
# """,

# language="python")

# a=st.text_input("enter the name")
# st.write(a)

# #14/05/25

# st.text_input("enter the nam")#only string
# st.number_input("age")#only integer
# st.selectbox("gender",["male","female"])
# st.multiselect("skills",["html","css","js","python"])
# st.radio("state",["tn","kl","ka"])
# st.checkbox("agree to terms and condition")
# st.button("submit")
# st.button("click")
# col1,col2=st.columns(2)
# with col1:
#     st.text_input("username")
#     st.image("https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?cs=srgb&dl=pexels-souvenirpixels-414612.jpg&fm=jpg")

# with col2:
#     st.text_input("password")

# with st.sidebar:
#     st.write("my side bar")



