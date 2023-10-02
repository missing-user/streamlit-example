import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"Date": "10.02.2001", "Your Comment": "test", "Comment Friend 1": "test 2"},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")