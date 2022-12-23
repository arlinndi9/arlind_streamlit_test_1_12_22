import streamlit as st

def convert_list(utext):
    lista=utext.split()
    return lista

def convert_upper(text):

    lowercaselist=[]
    for i in text:
        i=i.lower()
        lowercaselist.append(i)
    return lowercaselist

def count(text_list):
    return len(text_list)

text=st.text_input('text:')
clist=convert_list(text)

if st.button('lista'):
    st.write(convert_list(text))
if st.button('lower'):
    st.write(convert_upper(clist))
if st.button('count'):
    st.write('count ',count(clist))


