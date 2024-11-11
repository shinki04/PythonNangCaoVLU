import threading
from tkinter import Tk, Button, END, mainloop
from flask import Flask
import webbrowser

flask_app = Flask(__name__)


class TkApp:
    def __init__(self, master):
        self.button = Button(master, text="Show in webbrowser",command=self.btn_callback)
        self.button.pack()
    
    def btn_callback(self):
        global var
        var = 'Greetings from Tkinter'
        webbrowser.open("http://localhost:5001")


@flask_app.route('/', methods=['POST', 'GET'])
def flask_index():
    return var

def flask_main():
    flask_app.run(debug=False, host="localhost", port=5001)
    
def tk_main():
    root = Tk()
    TkApp(root)
    root.mainloop()


if __name__ == "__main__":
    flask_thread = threading.Thread(target=flask_main)
    flask_thread.daemon = True
    flask_thread.start()
    tk_main()