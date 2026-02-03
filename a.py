import streamlit as st
#header
st.header("this is header")
#title
st.title("this is title")
#subheader
st.subheader("this is subheader")
#text
st.text("this is text")
#horizontal line
st.markdown("-------------")
#write method to provide additional details
st.write("this is write")
st.write(1,2,3)
#italic text
st.markdown("*aishu*")
#bold text
st.markdown("**aishu**")
st.markdown("- item1 \n- item2")
st.markdown("<h1 style='color: red;'>Red text</h1>", unsafe_allow_html=True)
#to add caption
st.caption("this is caption")
#to write code
st.code("print('Hello, Streamlit')", language="python")
#to add mathematical  equations
st.latex(r''' a^2+b^2=c^2 ''')
st.latex(r''' a^2+b^2-2ab ''')
#to divide the section
st.divider()
#success message
st.success("this is success")
#Button
if st.button("click me"):
    st.write("button clicked")
    st.balloons()#balloons will popup
else:
    st.write("button not clicked yet")
    st.error("connection error") 
#text input method to get user input
name = st.text_input("enter your name:")
if name == " ": 
   st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("invalid, enter alphabets only")
else:
    st.success(f"hello, {name}")
    st.balloons()
#text_area
review= st.text_area("give your feedback")
st.write(review)
#checkbox
if st.checkbox("i agree"):
   st.write("thankyou")
#to create radio buttons
gender = st.radio("gender:",("male", "female", "other"))
st.write(f"your selected gender:{gender}")
#selectbox 
country = st.selectbox("select your country:",["indiAA","UK"])
skills = st.multiselect("select your country:",["indiAA","UK", "nigeria"])
#slider method to create a slider
age = st.slider("select your age:",0,100,25)
st.write(f"your age is:{age}")
#to upload files
file = st.file_uploader("upload your file:")
if file is not None:
    st.write("uploaded successfully")
else:
    st.write("upload file")
#form
with st.form("my_form"):
    name = st.text_input("name:")
    age = st.number_input("age:", 0, 100)
    email= st.text_input("email:")
    password=st.text_input("password:", type="password")
    submit = st.form_submit_button("submit")
    if submit:
        st.write("form submitted")
        st.write(f"name:{name}, age:{age}")
with st.form("registration form"):
    name= st.text_area("name:")
    email= st.text_input("email:")
    password= st.text_input("password:", type="password")
    submit= st.form_submit_button("register")
#columns method to create multiple columns
col1, col2, col3= st.columns(3)
with col1:
    st.header("column 1")
    st.text("this is column 1")
with col2:
    st.header("column 2")
    st.text("this is column 2")
with col3:
    st.header("column 3")
    st.text("this is column 3")
    st.divider()
#container method to group elements
container= st.container()
with container:
    st.header("container header")
    st.text("this is inside container")
#table method to display data in tabular format
data= {
    'Name': ['Anurag', 'rahul', 'neha'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
#sidebar method to create sidebar
st.sidebar.header("file")
st.sidebar.radio("new file", ("python file", "text file", "word file"))
st.sidebar.text("edit")
st.sidebar.text("view")
st.sidebar.text("rename")
st.sidebar.text("help")



from mysql import connector

conn = connector.connect(
    host="localhost",
    user="root",
    password="Aishu@123",
)

print("Connection successful")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS streamlit_db")
print("Database created successfully")

# connect to the newly created database

conn = connector.connect(
    host="localhost",
    user="root",
    password="Aishu@123",
    database="streamlit_db" 
)

print("Connected to streamlit_db database")

# create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY), name VARCHAR(255), age INT, email VARCHAR(255))")

print("Table created successfully")


# insert data into the table
cursor.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", ("Anurag", 21, "anurag@example.com"))

conn.commit()
print("Data inserted successfully")

# close the connection
cursor.close()