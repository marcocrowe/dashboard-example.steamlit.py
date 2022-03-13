import streamlit
from dashboards import ExportsPage

page = streamlit.sidebar.selectbox(
    "Choose Page", ["Summary Stats"])

if page == 'Summary Stats':
    query_params = streamlit.experimental_get_query_params()
    streamlit.header("QueryString")
    streamlit.write(query_params)
    query_option = query_params['filename'][0] 
    streamlit.write(query_option)

    ExportsPage.show_explore_page()
    
