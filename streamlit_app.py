import streamlit
from dashboards import ExportsPage

page = streamlit.sidebar.selectbox(
    "Choose Page", ["Summary Stats"])

if page == 'Summary Stats':
    ExportsPage.show_explore_page()
