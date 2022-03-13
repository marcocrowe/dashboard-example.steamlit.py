import streamlit
from dashboards import ExportsPage

page = streamlit.sidebar.selectbox(
    "Choose Page", ["Summary Stats"])

if page == 'Summary Stats':
    streamlit.header("QueryString")
    query_params = streamlit.experimental_get_query_params()
    streamlit.write(query_params)
    filename = query_params['filename'][0] 
    streamlit.write(filename)

    ExportsPage.show_explore_page()
    
