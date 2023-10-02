import streamlit as st
import pandas as pd

# Sample data
df = pd.DataFrame(
    [
       {"Date": "10.02.2001", "Your Comment": "test", "Comment Friend 1": "test 2"},
   ]
)

# Create a sidebar for inputs
with st.sidebar:
    date = st.date_input("Date")
    your_comment = st.text_area("Your Comment", max_chars=1000)
    friend_comment = st.text_area("Comment Friend 1", max_chars=1000)

    # Button to add the entry to the dataframe
    if st.button("Add Entry"):
        new_entry = {"Date": date.strftime("%d.%m.%Y"), "Your Comment": your_comment, "Comment Friend 1": friend_comment}
        df = df.append(new_entry, ignore_index=True)

# Display the dataframe
st.table(df)
