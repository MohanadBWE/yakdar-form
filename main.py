import streamlit as st

# --- Custom Theme Configuration ---
# This dictionary defines your custom theme colors based on your logo.
CUSTOM_THEME = {
    "primaryColor": "#85A36A",  # A soft green from your leaves
    "backgroundColor": "#F0F2F6", # A lighter, cleaner background
    "secondaryBackgroundColor": "#FFFFFF", # White for card backgrounds
    "textColor": "#31333F",     # A darker, more readable text color
    "font": "sans serif"
}

# --- Page Configuration ---
# IMPORTANT: Make sure your logo file (e.g., 'icon.png') is in the same directory as this script.
st.set_page_config(
    page_title="Yakdar form Hub",
    page_icon="icon.png", # Using your logo as the page icon
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Inject custom CSS for a professional UI ---
st.markdown(f"""
    <style>
        /* General Body Styling */
        body {{
            background-color: {CUSTOM_THEME['backgroundColor']};
        }}

        /* Main Title and Header */
        h1, h2, h3, h4, h5, h6 {{
            color: {CUSTOM_THEME['textColor']};
        }}
        
        /* Card layout for categories */
        .card {{
            background-color: {CUSTOM_THEME['secondaryBackgroundColor']};
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid #E0E0E0;
        }}
        .card-title {{
            font-size: 1.5em;
            font-weight: bold;
            color: {CUSTOM_THEME['textColor']};
            margin-bottom: 1rem;
            border-bottom: 2px solid {CUSTOM_THEME['primaryColor']};
            padding-bottom: 0.5rem;
        }}

        /* Styling for the form links */
        .form-link {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem;
            background-color: #F9F9F9;
            color: {CUSTOM_THEME['textColor']} !important; /* Forcing text color to black */
            text-decoration: none !important; /* Forcing removal of underline */
            border-radius: 8px;
            margin-bottom: 0.75rem;
            font-weight: 500;
            transition: all 0.2s ease-in-out;
            border: 1px solid #E0E0E0;
        }}
        .form-link:hover {{
            background-color: {CUSTOM_THEME['primaryColor']};
            color: white !important; /* Ensuring hover text color is white */
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transform: translateY(-2px);
            border-color: {CUSTOM_THEME['primaryColor']};
        }}
        /* Arrow icon for the link */
        .form-link::after {{
            content: '→';
            font-size: 1.5em;
            line-height: 1;
            transition: transform 0.2s ease-in-out;
        }}
        .form-link:hover::after {{
            transform: translateX(5px);
        }}

        /* Search input styling */
        .stTextInput > div > div > input {{
            border-radius: 8px;
            border: 1px solid #E0E0E0;
            background-color: {CUSTOM_THEME['secondaryBackgroundColor']};
        }}

        /* --- Responsive Design for Mobile and Tablet --- */
        @media (max-width: 768px) {{
            .card {{
                padding: 15px; /* Reduce padding on smaller screens */
                margin-bottom: 1.5rem;
            }}
            .card-title {{
                font-size: 1.25em; /* Make title slightly smaller */
            }}
            .form-link {{
                padding: 0.8rem;
                font-size: 0.95em; /* Adjust font size for readability */
            }}
            h1 {{
                font-size: 1.8em; /* Adjust main title size */
            }}
        }}
    </style>
""", unsafe_allow_html=True)


# --- Header with Logo and Title ---
st.image("logo.png", width=120) # Made the logo slightly larger
st.title("رێکخراوا یەک دار بەشێ داتایان")
st.write("پورتالا تومارکرنا فورمان بو پرۆژێ شکاندنا کونکریتی")


# --- Form Links ---
CATEGORIZED_FORMS = {
    "General Surveys": {
        "بکارئینانا روژانە": "https://ee.kobotoolbox.org/x/7SEYhAdM",
    
    },
    "forms": {

    },
    "forms": {
      
    }
}

# --- Search Functionality ---
st.header("Search Forms", divider='gray')
search_query = st.text_input("Type here to find a specific form...", placeholder="e.g., Beneficiary Registration", label_visibility="collapsed")

# --- Displaying the Form Links ---
found_match = False
for category, forms in CATEGORIZED_FORMS.items():
    filtered_forms = {
        name: url for name, url in forms.items()
        if search_query.lower() in name.lower()
    }

    if filtered_forms:
        found_match = True
        # Create a card for each category
        st.markdown(f"<div class='card'><div class='card-title'>{category}</div>", unsafe_allow_html=True)
        for form_name, form_url in filtered_forms.items():
            st.markdown(f'<a href="{form_url}" target="_blank" class="form-link">{form_name}</a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


if not found_match and search_query:
    st.warning(f"No forms found matching '{search_query}'. Please try another search term.")


# --- Footer ---
st.markdown("---")
# Corrected the st.info block to handle multiple lines of text correctly.
st.info(
    """
    All rights reserved © Yakdar 2024.  
    Please do not share any links outside the Yakdar organization.
    """, 
    icon="ℹ️"
)




