import streamlit as st

def click_function():
	st.balloons()
	st.toast('Clicked!', icon='🎉')

def cook_breakfast():
	"""This function comes from the documentation.
	https://docs.streamlit.io/library/api-reference/status/st.toast
	"""
	msg = st.toast('Gathering ingredients...')
	time.sleep(1)
	msg.toast('Cooking...')
	time.sleep(1)
	msg.toast('Ready!', icon = "🥞")

column_1, column_2 = st.columns(2)

with column_1:
	st.button(
		label='Click me for party!',
		key='First Button',
		on_click=click_function
	)

with column_2:
	st.button(
		label='',
		key='Second Button',
		on_click=cook_breakfast
	)
