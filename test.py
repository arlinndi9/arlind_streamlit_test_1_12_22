import streamlit as st

def convert_list(utext):
    lista=utext.split()
    return lista

def convert_lower(text):

    lowercaselist=[]
    for i in text:
        i=i.lower()
        lowercaselist.append(i)
    return lowercaselist

def count(text_list):
    return len(text_list)

text=st.text_input('text:')
clist=convert_list(text)
'''
if st.button('lista'):
    st.write(convert_list(text))
if st.button('lower'):
    st.write(convert_lower(clist))
if st.button('count'):
    st.write('count ',count(clist))

chose = st.radio(
    "chose",
    ('lista', 'lower', 'count'))

if chose=='lista':
    st.write(convert_list(text))
if chose=='lower':
    st.write(convert_upper(clist))
if chose=='count':
    st.write('count ',count(clist))
'''
lista = st.checkbox('lista')
lowerl = st.checkbox('listalower')
if lista and lowerl:
    st.write(convert_list(text),convert_upper(clist))


