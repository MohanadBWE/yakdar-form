import streamlit as st
import base64
from pathlib import Path

# --- Function to encode image to base64 ---
def get_image_as_base64(path):
    """Reads an image file and returns its base64 encoded string."""
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None

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
# Set to "wide" layout to allow for custom centering and responsive control.
st.set_page_config(
    page_title="Yakdar form Hub",
    page_icon="icon.png", # Using your logo as the page icon
    layout="wide", # Changed to wide for better responsive control
    initial_sidebar_state="auto"
)

# --- Inject custom CSS for a professional and responsive UI ---
st.markdown(f"""
    <style>
        /* General Body Styling & Font */
        body {{
            background-color: {CUSTOM_THEME['backgroundColor']};
            font-family: sans-serif;
        }}

        /* Main container to control width and centering */
        .main-container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }}

        /* App Header: Logo and Title */
        .app-header {{
            display: flex;
            align-items: center;
            gap: 15px; /* Space between logo and text */
            margin-bottom: 2rem;
        }}
        .app-header img {{
            width: 120px; /* Control logo size */
            height: 120px;
        }}
        .app-header .title-text h1 {{
            margin: 0;
            font-size: 2.2em;
            color: {CUSTOM_THEME['textColor']};
        }}
        .app-header .title-text p {{
            margin: 0;
            font-size: 1.1em;
            color: #555;
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
            color: {CUSTOM_THEME['textColor']} !important;
            text-decoration: none !important;
            border-radius: 8px;
            margin-bottom: 0.75rem;
            font-weight: 500;
            transition: all 0.2s ease-in-out;
            border: 1px solid #E0E0E0;
        }}
        .form-link:hover {{
            background-color: {CUSTOM_THEME['primaryColor']};
            color: white !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transform: translateY(-2px);
            border-color: {CUSTOM_THEME['primaryColor']};
        }}
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
            .main-container {{
                padding: 1rem; /* Less padding on mobile */
            }}
            .app-header {{
                flex-direction: column; /* Stack logo and title on mobile */
                text-align: center;
                gap: 10px;
            }}
            .app-header .title-text h1 {{
                font-size: 1.8em;
            }}
             .app-header .title-text p {{
                font-size: 1em;
            }}
            .card {{
                padding: 15px;
                margin-bottom: 1.5rem;
            }}
            .card-title {{
                font-size: 1.25em;
            }}
            .form-link {{
                padding: 0.8rem;
                font-size: 0.95em;
            }}
        }}
    </style>
""", unsafe_allow_html=True)

# --- Main App Layout ---
# Using a custom div to wrap the content for better control
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# --- Header with Logo and Title ---
logo_base64 = get_image_as_base64("logo.png")
if logo_base64:
    st.markdown(f"""
        <div class="app-header">
            <img src="data:image/png;base64,{logo_base64}" alt="Yakdar Logo">
            <div class="title-text">
                <h1>رێکخراوا یەک دار بەشێ داتایان</h1>
                <p>پورتالا تومارکرنا فورمان بو پرۆژێ شکاندنا کونکریتی</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    # Fallback in case the logo is not found
    st.title("رێکخراوا یەک دار بەشێ داتایان")
    st.write("پورتالا تومارکرنا فورمان بو پرۆژێ شکاندنا کونکریتی")


# --- Form Links ---
CATEGORIZED_FORMS = {
    "General Surveys": {
        "بکارئینانا روژانە": "https://ee.kobotoolbox.org/x/ZaOX7d3f",
    
    },
    "Sumel - Mserik": {
        "12.2.2026": "https://ee.kobotoolbox.org/x/PFZBZKSB",

    },
    "forms": {
      
    }
}

# --- Search Functionality ---
st.header("Search Forms", divider='gray')
search_query = st.text_input("Type here to find a specific form...", placeholder="e.g., Beneficiary Registration", label_visibility="collapsed")

# --- Displaying the Form Links ---
found_match = False
# Using a copy of keys to avoid runtime error during dictionary modification in a loop
for category, forms in list(CATEGORIZED_FORMS.items()):
    # Skip empty categories
    if not forms:
        continue

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
st.info(
    """
    All rights reserved © Yakdar 2024.  
    Please do not share any links outside the Yakdar organization.
    """, 
    icon="ℹ️"
)

# Close the main container div
st.markdown("</div>", unsafe_allow_html=True)


















