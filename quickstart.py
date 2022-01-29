import streamlit as st
import pandas as pd

def find_work(mem_name, mem_comm):
    data = pd.read_csv("Demo Assignments.csv")
    test_bool = []
    testCase = (data['Name'].str.lower() == mem_name.lower()) & (data['Community'].str.lower() == mem_comm.lower())
    for i in testCase:
        test_bool.append(i)

    if True in test_bool:
        st.write(data[testCase])

    if True not in test_bool:
        st.write("Please provide a valid name or choose correct community !")

st.header("Mattrab Work Status")
st.write("Check the status of your work here:")

form = st.form(key='my_form')
name = form.text_input(label='Your Name:')
community = form.selectbox('Select your Community', ['MC-SXC', 'MC-SXGJD', 'MC-Global', 'MC-NPS'], key=1)
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    if community=="MC-NPS":
        find_work(name, "NPS")
    if community=="MC-Global":
        find_work(name, "Global")
    if community=="MC-SXGJD":
        find_work(name, "SXG")
    if community=="MC-SXC":
        find_work(name, "SXC")