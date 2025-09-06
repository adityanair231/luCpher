'''
This project consist of building an AI voice assistant named luCpher, and it will be a voice chatbot and a web based A.I. assistant.
Basically, it will be the web app based AI model and. This is the backend program we are working in and for that will be using 
Flask framework for setting up the virtual environment for the application. We will also add some databases and backend server to 
the application.


wnfndfkjofoiuljdfsdpfikpshgo0wr-290eknf m  131p324-340-0t03249=04
5934i-53204-=1123-4o-239imlvogjodkp0-52-34=jjer2-3=2=4-2=-34=230448358/
324-2340==-234=234093--2-4=234830-=-=2340234/239409875784568430--234-sdmlsdjfljl
fksndkf=-1340=230dlmsdf=-2340-=2-323443mml4ml234kh=-23042323////2342340-39=-

'''
import tkinter as tk
from tkinter import PhotoImage
import threading
import os
import speech_recognition as sr
import pyttsx3
import sqlite3
import datetime
import webbrowser
import re
import pywhatkit as auto
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image, ImageTk, ImageDraw, ImageFilter


# === CONFIG ===
AI_NAME = "lucifer"
process_complete = False

# === INIT DB & SPEECH ENGINE ===
con = sqlite3.connect("luCpher.db")
cursor = con.cursor()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()

def inputCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        ask = r.recognize_google(audio, language="en-in")
        print(f"You said: {ask}")
    except Exception:
        speech("Anything else?")
        return "None"
    return ask

def openComm(ask):
    ask = ask.replace("hey " + AI_NAME, "").replace("open", "").lower().strip()
    if ask:
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (ask,))
            results = cursor.fetchall()
            if results:
                speech("Opening " + ask)
                os.startfile(results[0][0])
            else:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (ask,))
                results = cursor.fetchall()
                if results:
                    speech("Opening " + ask)
                    webbrowser.open(results[0][0])
                else:
                    speech("Opening " + ask)
                    os.system('start ' + ask)
        except:
            speech("Something went wrong")

def Youtube(ask):
    search = ex_yt(ask)
    if search:
        speech("Playing " + search + " on YouTube")
        auto.playonyt(search)

def ex_yt(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    check = re.search(pattern, command, re.IGNORECASE)
    return check.group(1) if check else None

def genZ(user_input):
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 500,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    history = []

    try:
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(user_input)
        model_response = response.text
        print(f'luCpher: {model_response}')
        speech(model_response.replace("*", ""))
    except Exception as e:
        print("Gemini error:", e)
        speech("Sorry, something went wrong with the API module.")

def run_voice_assistant():
    """This is the original greet() logic but in a thread-safe function."""
    global process_complete
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speech("Good morning, sir, Lucifer this side.")
    elif 12 <= hour < 16:
        speech("Good afternoon< sir, Lucifer this side.")
    else:
        speech("Good evening, sir, Lucifer this side.")
    speech("May I help you?")

    while True:
        ask = inputCommand().lower()

        if 'open' in ask:
            openComm(ask)
        elif 'on youtube' in ask:
            Youtube(ask)
        elif 'the time' in ask:
            string_time = datetime.datetime.now().strftime("%H:%M:%S")
            speech(string_time)
        elif 'search' in ask:
            auto.search(ask.replace('search', ''))
        elif 'who are you' in ask or "what's your name" in ask:
            speech("I am lucifer, your personal virtual assistant.")
        elif 'good job' in ask:
            speech("Thank you! Any more orders for me, sir?")
        elif 'nothing' in ask or 'you may leave' in ask or 'bye' in ask:
            speech("As you wish, sir. Feel free to call me again. Goodbye!")
            process_complete = True
            break
        else:
            genZ(ask)


# === TKINTER UI ===

root = tk.Tk()
root.title("Lucpher | Home Page")
root.configure(bg="black")
root.geometry("900x600")

# --- Top Bar ---
border_frame = tk.Frame(root, bg="black")
border_frame.pack(fill="x", pady=10)

logo_img = PhotoImage(file="lucpher.jpg3.png")
logo_img = logo_img.subsample(3, 3)

logo_label = tk.Label(border_frame, image=logo_img, bg="black")
logo_label.pack(side="left", padx=25)

lucpher_label = tk.Label(border_frame, text="LuCpher", font=("Poppins", 24, "bold"),
                         fg="#DE0909", bg="black")
lucpher_label.pack(side="left", padx=20)

guide_label = tk.Label(border_frame, text="Guide", font=("Poppins", 18, "bold"),
                       fg="#DE0909", bg="black", cursor="hand2")
guide_label.pack(side="right", padx=15)

# --- Center Canvas ---
canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(expand=True, fill="both")

# Load and crop image
original_img = Image.open("lucpher.jpg2.png")
bbox = original_img.getbbox()
cropped_img = original_img.crop(bbox)

def create_gradient(width, height):
    """Creates a smooth black -> dark red gradient image."""
    gradient = Image.new("RGB", (width, height), "#000000")
    draw = ImageDraw.Draw(gradient)
    for i in range(height):
        r = int(0 + (222 * (i / height)))  # Dark red towards bottom
        draw.line((0, i, width, i), fill=(r, 0, 0))
    return ImageTk.PhotoImage(gradient)

def draw_logo(event=None):
    canvas.delete("all")
    canvas_w = canvas.winfo_width()
    canvas_h = canvas.winfo_height()

    # Draw gradient background
    gradient_img = create_gradient(canvas_w, canvas_h)
    canvas.create_image(0, 0, image=gradient_img, anchor="nw")
    canvas.gradient = gradient_img

    # Choose smallest dimension so logo remains a circle
    size = min(canvas_w, canvas_h) - 80
    resized_img = cropped_img.resize((size, size), Image.LANCZOS)

    # Create glow effect
    glow_size = size + 40
    glow = Image.new("RGBA", (glow_size, glow_size), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse((0, 0, glow_size, glow_size), fill=(222, 9, 9, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(30))
    glow_tk = ImageTk.PhotoImage(glow)

    # Place glow + logo
    canvas.create_image(canvas_w//2, canvas_h//2, image=glow_tk, anchor="center")
    canvas.glow = glow_tk

    tk_img = ImageTk.PhotoImage(resized_img)
    canvas.create_image(canvas_w//2, canvas_h//2, image=tk_img, anchor="center")
    canvas.image = tk_img

canvas.bind("<Configure>", draw_logo)

# --- Bottom Microphone with Animation ---
mike_label = tk.Label(root, text="🎙️", font=("Arial", 40), fg="#EA4444", bg="black")
mike_label.pack(side="bottom", pady=15)

def animate_mic():
    """Makes mic glow for a moment."""
    for i in range(3):
        mike_label.config(fg="#FF5555")
        root.update()
        root.after(150)
        mike_label.config(fg="#EA4444")
        root.update()
        root.after(150)

def on_mic_click(event):
    animate_mic()
    threading.Thread(target=run_voice_assistant, daemon=True).start()

mike_label.bind("<Button-1>", on_mic_click)

root.mainloop()

