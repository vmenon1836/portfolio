import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Vinu Pradeep Menon
##### *Data Analyst* 
''')

image = Image.open('Profile_image.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Ambitious and proactive Data analyst professional adept at Mathematics and Statistics with 5 years of experience with proven technical and leadership skills in solving business challenges. 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #59515E;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/vinupradeepmenon" target="_blank">Vinu Pradeep Menon</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5,2,2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Post Graduate** (Data Analytics for Business), *St. Clair College*, Windsor, Ontario',
    '2018-2020')
st.markdown('''
- Advanced Statistics
- Machine Learning
- Project Management
- Analytics related to healthcare, finance and marketing
''')

txt('**Bachelor of Science** (Mathematics and Statistics), *Mahatma Gandhi University*, Kochi',
    '2013-2016')
st.markdown('''
- Real and Complex analysis.
- Statistical Distributions.
- Graph Theory
- Abstract algebra
- Calculus
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Analyst**, Missing Link Technologies, Moncton,NB',
    '2021-Present')
st.markdown('''
- Data pipeline work for Fiber to the Home project using Python.
- Worked on telecom automation
- Created dashboards using Power BI.
- Did research on various visualization tools like Tableau, Qlik Sense, Redash.
- Did indepth study on Kubernetes and Docker.
''')

txt('**Billing Analyst**, Central Transport, Windsor, Ontario',
    '2019-2021')
st.markdown('''
- Maintained records by creating daily, weekly and monthly reports, and created charts based on various performance metrics like BPH, error ratio and idle time using Excel spread sheet and Tableau.
- Input client information into company database to provide leaders with quick access to essential client data using JRC software
- Identified errors in data entry and related issues.
''')

txt('**Junior Data Analyst**, Cyber Space, Kochi',
    '2016-2018')
st.markdown('''
- Collected and cleaned daily customer and sales data using Excel spreadsheet.
- Used various tools like Python for sales prediction and Tableau, SQL and PowerPoint to create weekly and monthly reports and visualization.
- Trained and recruited Interns.
''')

#####################
st.markdown('''
## Certifications
''')
txt2('Computer Science and Programming using Python', 'https://courses.edx.org/certificates/a65851fae56b4cce87139c8e88c5f512')
txt2('Introduction to Node-red', 'https://www.coursera.org/account/accomplishments/certificate/49R6FS6SQ9G6')
txt2('IBM Data Analyst Specialization', 'https://www.coursera.org/account/accomplishments/specialization/certificate/T94KXMP9LZRQ')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `C++`')
txt3('Data Wrangling', '`SQL`, `pandas`, `numpy`, `openpyxl`')
txt3('Data Visualization', '`Tableau`, `Power BI`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/vinupradeepmenon')
