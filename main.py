import streamlit as st

def click_function() -> None:
	st.balloons()
	st.toast('Clicked!', icon='🎉')

st.button(label='Click me for party!', on_click=click_function)
