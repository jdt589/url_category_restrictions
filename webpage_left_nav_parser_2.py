import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def extract_labels_from_html(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all elements with the attribute 'data-filter-name'
    elements_with_data_filter_name = soup.find_all(attrs={"data-filter-name": True})
    
    # Extract the values of 'data-filter-name' attribute
    data_filter_names = [element['data-filter-name'] for element in elements_with_data_filter_name]
    
    return data_filter_names

def fetch_and_extract():
    # Get the URL from the entry widget
    url = url_entry.get()
    if url:
        try:
            # Fetch the HTML content from the URL
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful

            # Get the HTML content
            html_content = response.text

            # Extract data-filter-name values
            data_filter_names = extract_labels_from_html(html_content)

            # Display the extracted values in the text box
            text_box.delete('1.0', tk.END)  # Clear previous content
            for name in data_filter_names:
                text_box.insert(tk.END, f"{name}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch or parse HTML: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL")

# Create the main window
root = tk.Tk()
root.title("HTML Content Extractor")

# Create a label for the URL entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)

# Create an entry widget for URL input
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create a button to fetch and extract data
fetch_button = tk.Button(root, text="Fetch and Extract", command=fetch_and_extract)
fetch_button.pack(pady=10)

# Create a text box to display the extracted data-filter-name values
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
