import streamlit as st
import pandas as pd
import datetime

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    # Check if the user has added any entries
    if 'user_has_added_entry' not in st.session_state:
        st.session_state.user_has_added_entry = False

    # If the user hasn't added any entries, display a greyed-out example entry
    if not st.session_state.user_has_added_entry:
        example_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum. "
                        "Donec in efficitur leo. Sed nec tempor nunc. Nulla facilisi. Suspendisse potenti. Aliquam erat volutpat. "
                        "Nunc fermentum tortor ac porta dapibus. In rutrum ac purus sit amet tempus. Vivamus lacinia odio vitae vestibulum. "
                        "Donec in efficitur leo. Sed nec tempor nunc. Nulla facilisi. Suspendisse potenti. Aliquam erat volutpat.")
        df = pd.DataFrame([{"Date": datetime.date.today().strftime('%d.%m.%Y'), "Journal Entry": example_text}])
    else:
        df = pd.DataFrame(columns=["Date", "Journal Entry"])

    # Use CSS to style the table and make it span the whole width
    st.markdown("""
    <style>
        table {
            width: 100%;
        }
        th:nth-child(1) {
            width: 15%;
        }
        th:nth-child(2) {
            width: 85%;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create a placeholder for the dataframe at the top
    table_placeholder = st.empty()

    # Display the initial dataframe using the specified method
    table_placeholder.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    # Input fields for comments at the bottom
    st.write("## Add a Journal Entry")
    your_comment = st.text_area("", max_chars=2000, height=200)

    # Button to add the entry to the dataframe
    if st.button("Add Entry"):
        new_entry = {"Date": datetime.date.today().strftime('%d.%m.%Y'), "Journal Entry": your_comment}
        df.loc[len(df)] = new_entry  # Add the new entry to the DataFrame
        st.session_state.user_has_added_entry = True
        table_placeholder.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)  # Update the displayed table with the new entry







