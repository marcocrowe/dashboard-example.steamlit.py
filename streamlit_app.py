import streamlit
from dashboards import ExportsPage

page = streamlit.sidebar.selectbox(
    "Choose Page", ["Summary Stats"])

if page == 'Summary Stats':
    ExportsPage.show_explore_page()
    query_params = streamlit.experimental_get_query_params()
    streamlit.write(query_params)
    #query_option = query_params['option'][0] 
