# This imports some necessary libraries.
import webbrowser
import tempfile
import urllib.request
from tkinter import *


class Browser:
    """This creates a relay that allows a user to directly view data sent from a web server."""
    def __init__(self, master):
        """Sets up a browsing session."""
        # Explicit global declarations are used to allow certain variable to be used in all methods.
        global e1

        # Here we create some temporary settings that allow us to create a client that ignores proxy settings.
        self.proxy_handler = urllib.request.ProxyHandler(proxies=None)
        self.opener = urllib.request.build_opener(self.proxy_handler)

        # This sets up components for the GUI.
        Label(master, text='Full Path').grid(row=0)
        e1 = Entry(master)
        e1.grid(row=0, column=1)
        Button(master, text='Go', command=self.browse).grid(row=0, column=2)

        # This binds the return key to self.browse as an alternative to clicking the button.
        root.bind('<Return>', self.browse)

    @staticmethod
    def parsed(data):
        """Cleans up the data so the file can be easily processed by the browser."""
        # This removes removes all python-added special characters such as b'' and '\\n' to create understandable HTML.
        initial = str(data)[2:-1]
        lines = initial.split('\\n')
        return lines

    def navigate(self, query):
        """Gets raw data from the queried server, ready to be processed."""
        # This gets the opener to query our request, and submit the response to be parsed.
        response = self.opener.open(query)
        html = response.read()
        return html

    def browse(self):
        """Wraps all functionality together for data reading and writing."""
        # This inputs and outputs the necessary website data from user-specified parameters.
        raw_data = self.navigate(e1.get())
        clean_data = self.parsed(raw_data)

        # This creates a temporary file in which we store our HTML data, and open it in the default browser.
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as cache:
            cache.writelines(line.encode('UTF-8') for line in clean_data)
            webbrowser.open_new_tab(cache.name)

# Creates a Tk() window that is always in front of all other windows.
root = Tk()
root.wm_attributes('-topmost', 1)

# Starts the program by initializing the Browser object and main-looping the Tk() window.
anon = Browser(root)
root.mainloop()
