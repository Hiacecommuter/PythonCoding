""" install
pip  install streamlit
streamlit hello

run code
streamlit run file_name.py
"""

import streamlit as st
""" display texts
st.write() -- function to add anything to a web app
st.title() -- add title of the app
st.markdown() -- set a markdown of a section
st.header() -- set header of a section
st.subheader() -- set sub-header of a section
st.caption() -- write caption
st.code() --  set a code
st.latex() -- diaply math expressions formatted as LaTeX
"""
st.write("Hello ,let's learn how to build a streamlit app together")
st.title ("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

""" display an image, video or audion file with streamlit
st.image()  -- dispaly an image
st.audio()  -- display an audio
st.video()  -- display a video
"""
st.image("kid.jpg")
st.audio("Audio.mp3")
st.video("video.mp4")

""" input widgets
st.checkbox() -- returns a boolean value. True if checked else False
st.button() -- display a button widget
st.radio()  -- display a radio button widget
st.multiselect()  -- display a multiselect widget
st.select_slider()  -- display a select slider widget
st.slider() -- display a slider widget
"""
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
"""
st.number_input() -- display a numeric input widget
st.text_input() -- display a text input widget
st.date_input() -- date input widget to choose a date
st.time_input() -- chose a time
st.text_area()  -- display a text input widget with more than a line text
st.file_uploader  -- display a file uploader widget
st.color_picker() -- display color picker widget to choose a color
"""
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

""" display progress and status with streamlit
st.balloons() -- dispaly balloons for celebration
st.progress() -- display a progress bar
st.spinner()  -- display a temporary waiting message during excuation
"""
st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):    
  time.sleep(10)
  
"""
st.success()  -- display a success message
st.error()  -- display an error message
st.warning()  -- display a warning message
st.info() -- display an informational message
st.exception() -- display an exception message
"""
st.success("You did it !")
st.error("Error")
st.warnig("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

"""sidebar and container
By organizing your content, you allow visitors to understand and navigate your site,\
sidebar
st.sidebar()  -- make this element pinned to the left, allowing users to focus on the content in your app
st.spinner() and st.echo() are not supported with st.sidebar()

container
st.container() -- invisible container where you can put elements in order to create a useful arrangement and hierarchy
"""
st.sidebar().title("This is written inside the sidebar")
st.sidebar().button("click")
st.sidebar().radio("Picl you gender", ["M", "F"])

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")

