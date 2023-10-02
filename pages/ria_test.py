import streamlit as st
import pandas as pd
import datetime

# Check if the user has added any entries
if 'user_has_added_entry' not in st.session_state:
    st.session_state.user_has_added_entry = False

# If the user hasn't added any entries, display a greyed-out example entry
if not st.session_state.user_has_added_entry:
    df = pd.DataFrame([{"Date": "Example Date", "Your Comment": "Lorem ipsum dolor sit amet..."}])
else:
    df = pd.DataFrame(columns=["Date", "Your Comment"])

# Create a placeholder for the dataframe at the top
table_placeholder = st.empty()

# Display the initial dataframe without the index and make it span the whole display size
table_placeholder.write(df.style.set_properties(**{'background-color': 'grey' if not st.session_state.user_has_added_entry else 'white', 'width': '100%'}).hide_index())

# Get the current date
current_date = datetime.date.today()

# Display the current date without allowing user input (making it a static display)
st.write(f"Date: {current_date.strftime('%d.%m.%Y')}")

# Input fields for comments
your_comment = st.text_area("Your Comment", max_chars=1000, height=150)

# Button to add the entry to the dataframe
if st.button("Add Entry"):
    new_entry = {"Date": current_date.strftime("%d.%m.%Y"), "Your Comment": your_comment}
    df.loc[len(df)] = new_entry  # Add the new entry to the DataFrame
    st.session_state.user_has_added_entry = True
    table_placeholder.write(df.style.set_properties(**{'width': '100%'}).hide_index())  # Update the displayed table in the placeholder
