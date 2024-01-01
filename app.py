#python  -m streamlit run app.py
import streamlit as st
st.title("Hello folks,  Welcome to Wonderland ")
st.header("Hello folks,  Welcome to Wonderland ")
st.subheader("Hello folks,  Welcome to Wonderland ")
st.text("Hello folks,  Welcome to Wonderland ")

st.markdown('# HI')

st.success('Data is Submitted') #if ithis in green color that means its a success 
st.info('Information')
st.warning('Warning')
st.error('Error')
st.exception(ZeroDivisionError('Division not possible with 0'))

st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write(1+2+3)
st.write('1+2+3')

st.code('x = 10\n'
        ' for i in range(x):\n'
        '\tprint(i)')

st.checkbox('Male')
st.checkbox('Female')

if(st.checkbox('Adult')):
    st.write('you are 18+')

radiobutton = st.radio('Select : ', ('Male','Female','Other'))

if(radiobutton == 'Male' ):
    st.write('you are a Male')
elif(radiobutton == 'Female' ):
    st.write('you are a Female')  
elif(radiobutton == 'Other' ):
    st.write('chakka hai tu ')
    
st.subheader('Select Box')
selectbox = st.selectbox("Data Science: ", ['Data Analysis' , 'Web Scrapping' ,
                                            'Machine Learning' , 'Deep Learning',
                                            ' Natural language processing','image processing'])
st.write("you ve selected: ",selectbox)

st.subheader('MultiSelect Box')
MultiSelectBox = st.multiselect("Data Science: ", ['Data Analysis' , 'Web Scrapping' ,
                                            'Machine Learning' , 'Deep Learning',
                                            ' Natural language processing','image processing'])

st.write('You have selected : ',len(MultiSelectBox),'courses' )

st.subheader("Button")
if(st.button('Click Me')):
    st.write("Thanku  for clicking me")
    
st.subheader("Slider")                                  # Slider
vol = st.slider('Select the volume',0,100,step = 1)
st.write('Volume is : ',vol)

st.subheader("Text Input")                              # Text-Input
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

st.subheader("Text Area ")
textarea = st.text_area("write something about yourself " )
st.write(textarea)

st.text_area('Write something interesting about yourself')

st.subheader("Input Number")                           # Input-Number
st.number_input('Select your age',18,110)

st.subheader("Input Date")                              # Input-Date
st.date_input('Date')

st.subheader("Input Time")                              # Input-Time
st.time_input('Time')




