import streamlit as st

text=input('text:')
def convert_list():
        '''
        a=text.split(' ')
        st.button('button',a)
        st.write(a)
        '''
        l=text.split(' ')
        return l
print(convert_list())

def conwert_lower():
    l=[]
    a=convert_list()
    for i in a:
        lovercase=i.lower()
        l.append(lovercase)
    return l

print(conwert_lower())

def count():
    a=convert_list()
    return len(a)

print(count())

