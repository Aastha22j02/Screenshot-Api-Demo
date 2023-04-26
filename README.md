# Website Screenshot

This project is a simple Streamlit app that takes in a URL and displays a screenshot of the website.

## Requirements

To run this project, you will need to install the following libraries:

- requests
- streamlit

You can install them by running the following command:

```bash
pip install requests streamlit
```

## Code

The code for this project is contained in a single Python file, `app.py`. Here's what the code looks like:

```python
import requests
import streamlit as st

# Get the screenshot API URL from Streamlit secrets
screenshot_url = st.secrets['screenshot-api-group']['screenshot-api']

# Set up the Streamlit app
st.title("Website Screenshot")

# Get the URL from the user
url = st.text_input("Enter a URL")

# If a URL was entered, retrieve the screenshot and display it
if url:
    response = requests.get(f"{screenshot_url}={url}")
    if response.status_code == 200:
        st.image(response.content)
    else:
        st.error("Failed to retrieve screenshot")
```

The code retrieves a URL from the user, then sends a request to a screenshot API to retrieve a screenshot of the website. If the screenshot is retrieved successfully, it is displayed in the Streamlit app. If there is an error retrieving the screenshot, an error message is displayed instead.

## How to Use

To use this app, simply run the `app.py` file using Streamlit:

```bash
streamlit run app.py
```

Then, enter a URL into the input field and press Enter. The screenshot of the website should be displayed in the app.

## Conclusion

This project demonstrates how to create a simple Streamlit app that retrieves a screenshot of a website using an API. With just a few lines of code, you can create a powerful tool for capturing website screenshots.