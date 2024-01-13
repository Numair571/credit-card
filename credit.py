import streamlit as st
import pickle
import hydralit_components as hc
model=pickle.load(open('model.pkl','rb'))

menu_data = [
    {'label':"Left End"},
    {'label':"Book"},
    {'label':"Component"},
    {'label':"Dashboard"},
    {'label':"Right End"},
]
menu_id = hc.nav_bar(menu_definition=menu_data)
st.info(f"{menu_id=}")

st.title('credit card fraud detection')



Time=st.text_input('enter time:')
V1=st.text_input('enter v1:')
V2=st.text_input('enter v2:')
V3=st.text_input('enter v3:')
V4=st.text_input('enter v4:')
V5=st.text_input('enter v5:')
V6=st.text_input('enter v6:')
V7=st.text_input('enter v7:')
V8=st.text_input('enter v8:')
Amount=st.text_input('enter amount:')

if st.button('Detect'):
    Time=int(Time)
    V1=float(V1)
    V2=float(V2)
    V3=float(V3)
    V4=float(V4)
    V5=float(V5)
    V6=float(V6)
    V7=float(V7)
    V8=float(V8)
    Amount=float(Amount)

    data=[[Time,V1,V2,V3,V4,V5,V6,V7,V8,Amount]]
    result=model.predict(data)
    st.success(result)

    if result[0]==0:
        st.write("not fraud")

    else:
        st.write("fraud")


