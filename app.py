import streamlit as st

st.title("Welcome to Winstons Website")

st.header("Heading of Streamlit")

st.subheader("Subheading of Streamlit")

st.text("This is an Example Text")

st.success("Succees")
st.warning("Warning")
st.info("Information")
st.error("Error")


if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox!!!")
else:
    st.text("User has not selected the checkbox")

color = st.radio("What is your favorite color?", ("Red","Green","Blue"))

if color == "Green":
    st.success("Green")
elif color == "Red":
    st.error("Red")
else:
    st.info("Blue")

occupation = st.selectbox("What do you want?",["Student", "Dancer", "Engineer"])
st.text("I would like to become "+occupation)

if st.button("Submit"):
    st.success("Successfully submitted")

st.sidebar.header("Website's Sidebar")
st.sidebar.text("Course Contents")