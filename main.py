import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    select = option_menu(
        menu_title="internship",
        options=["internship","about","contact"],
        icons=["book","file-person","telephone"]
     )
if select=="internship":
    st.title("internship")
    st.write("hii....how are you .....what about your tdy plan")

elif select=="about":
    st.title("about")
    st.balloons()
    st.header("arun")

elif select=="contact":
    st.title("contact")
    st.button("submit")
    st.button("click")

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



