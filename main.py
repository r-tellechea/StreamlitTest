import streamlit as st
from time import sleep

def click_function():
	st.balloons()
	st.toast('Clicked!', icon='🎉')

def cook_breakfast():
	"""This function comes from the documentation.
	https://docs.streamlit.io/library/api-reference/status/st.toast
	"""
	st.toast('Gathering ingredients...')
	sleep(1)
	st.toast('Cooking...')
	sleep(1)
	st.toast('Ready!', icon = "🥞")

column_1, column_2 = st.columns(2)

with column_1:
	st.button(
		label='Click me for party!',
		key='First Button',
		on_click=click_function
	)

with column_2:
	st.button(
		label='Click me for cook',
		key='Second Button',
		on_click=cook_breakfast
	)
