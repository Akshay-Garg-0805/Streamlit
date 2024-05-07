import streamlit as st

# To run it open anaconda prompt and type streamlit run along with path of file

st.title("Title")
st.header("Header")
st.subheader("SubHeader")
st.text("Text")
st.markdown("# Markdown")
st.markdown("## Markdown")
st.markdown("### Markdown")
st.markdown("#### Markdown")
st.markdown("##### Markdown")
st.markdown("Markdown")                    

# Some colour coded texts display
st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error")

st.exception(ZeroDivisionError('Div X'))

st.help(ZeroDivisionError)

# Writing on the screen
st.write('1+2+3')
st.write(1+2+3)

# Display a code area
st.code('x=19\n'
        'for i in range(0,x):\n'
        '\tprint(x)')

# Checkbox
st.checkbox("Female")
if(st.checkbox("Male")): # Checking if checkbox is checked then do the following code
    st.write("Male")

# Radio button
radiobtn=st.radio("Select : ",('Check','Uncheck'))
if radiobtn=='Check': # If a particular option is choosen write the result
    st.write("Radio Checked")

# Select box(Drop down list)
selectbox=st.selectbox("Data Sceince : ",['Data Analysis','Web Scrapping','ML','NLP'])
st.write("You have selected ",selectbox)

# Multi select box
multi=st.multiselect("Data Sceince : ",['Data Analysis','Web Scrapping','ML','NLP'])
st.write("Selection : ",len(multi),'courses')

# Button
btn=st.button("Click")
if(btn):  # Functionality on clicking button
    st.write("Button Clicked")

# Slider
sld=st.slider("Slider value:",1,100,step=1)
st.write(sld)

# text input from user
inp=st.text_input("Name : ")
if(inp):
    st.write("Hii ",inp)
pswd=st.text_input("password : ",type='password')

# taking larger input from user
i=st.text_area("A : ",max_chars=200)
st.write(i)

# input number
n=st.number_input('AA: ',1,10,step=1)
st.write(n)

# input date
a=st.date_input("Date : ")
st.write(a)

# input time
t=st.time_input("Time : ")
st.write(t)