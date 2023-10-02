import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"Date": "10.02.2001", "Your Comment": "test", "Comment Friend 1": "test 2"},
   ]
)


edited_df = st.data_editor(df)
