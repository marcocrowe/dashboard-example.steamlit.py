import streamlit
from dashboards import ExportsPage
import json

page = streamlit.sidebar.selectbox(
    "Choose Page", ["Summary Stats"])

if page == 'Summary Stats':
    streamlit.header("QueryString")
    query_params = streamlit.experimental_get_query_params()
    streamlit.write(query_params)
    filename = query_params['filename'][0] 
    streamlit.write(filename)



    obj = {"filename": filename, "result": 'flower'}
    streamlit.write(obj)
    streamlit.write(json.dumps(obj))

    ExportsPage.show_explore_page()
    
