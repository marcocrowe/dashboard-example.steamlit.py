import streamlit
import streamlit.components.v1 as components

query_params = streamlit.experimental_get_query_params()
filename = query_params['filename'][0] 

import json

obj = {"filename": filename, "result": 'flower'}

#streamlit.write(obj)

#streamlit.write(json.dumps(obj))

components.html(obj)