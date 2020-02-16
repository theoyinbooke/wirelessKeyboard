'''
Made by Aayush Pokharel

Last modified on: Feb 16, 2020

https://github.com/Aayush9029

'''

from flask import Flask, render_template, request
import pyautogui

app = Flask(__name__)

@app.route("/")
def index():
    # query is key and the default value is None
    key = request.args.get("key", "None")

    render_template("index.html", key=key)

    # presses anything that is send to the link
    pyautogui.press(key)

    # adding custom if statement because js key layout doesn't work well with pyautogui
    if key == 'Space':
        pyautogui.press("space")
    if key == 'Backspace':
        pyautogui.press("backspace")
    if key == 'ArrowUp':
        pyautogui.press("up")
    elif key == 'ArrowDown':
        pyautogui.press("down")
    elif key == 'ArrowRight':
        pyautogui.press("right")
    elif key == 'ArrowLeft':
        pyautogui.press("left")
    elif key == 'Enter':
        pyautogui.press("enter")
    else:
        pass
    
    # this step is kinda reduntant
    return render_template("index.html", key=key)

# change the port to any number 8000 to 65535 
app.run(host="0.0.0.0", port=8000)
