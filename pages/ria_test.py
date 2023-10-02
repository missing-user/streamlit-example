import streamlit as st
import pandas as pd
import datetime

# Sample data
df = pd.DataFrame(columns=["Date", "Your Comment"])

# Display the dataframe at the top
st.table(df)

# Get the current date
current_date = datetime.date.today()

# Display the current date without allowing user input (making it a static display)
st.write(f"Date: {current_date.strftime('%d.%m.%Y')}")

# Input fields for comments
your_comment = st.text_area("Your Comment", max_chars=1000, height=150)

# Button to add the entry to the dataframe
if st.button("Add Entry"):
    new_entry = {"Date": current_date.strftime("%d.%m.%Y"), "Your Comment": your_comment}
    df = df.append(new_entry, ignore_index=True)
    st.table(df)  # Update the displayed table with the new entry
