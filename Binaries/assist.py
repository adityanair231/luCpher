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
from flask import Flask
import os # We can gain access to the system using this module
import google.generativeai as genai # for using gemini's api
from dotenv import load_dotenv # for creating a .env file and store there our API key
import speech_recognition as sr  # For recognizing voice input
import pyttsx3  # For text-to-speech output
import sqlite3  # For accessing the database
import datetime  # For getting the current time
import webbrowser  # For opening URLs
import pywhatkit as auto  # For automating WhatsApp and playing YouTube videos
import re  # For regular expressions used in YouTube search

AI_NAME = "lucifer"  # NAME OF OUR ASSISTANT :-D 

# Initialize database connection for system commands and web commands
con = sqlite3.connect("luCpher.db")
cursor = con.cursor()
'''
Basically the following code will be used to declare the type of voice and 
from where the the voices will be considered. For example, the sapi5 module in the following code is used 
for defining the type of voice used in the code. Sapi5 is the microsoft's speech API which will be using in the project for the 
speech output...

1312-039-120=-34-=234-23nk32n4kn234-=340=-//??
??234093=-2=34023=0234=3ml4m23l4m3-=4 =324=-324=-o4-=230c
23=49023o4c-]23-40=-3 4=-23=-4=-234  jojjfgjgjdfg9gi-34-02-=3//....

'''

# Setting up the engine through speech API by Microsoft (sapi5)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  # Set to male voice (0th index)
engine.setProperty('rate', 174)  # Set speech speed

# Speech function for the assistant's voice output
def speech(audio):
    engine.say(audio)
    engine.runAndWait()

#This following function will be used to greet the user as the program or application starts. It will wish according to the time of the day
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speech("Good morning, Lucifer this side.")
    elif hour >= 12 and hour < 16:
        speech("Good afternoon, Lucifer this side.")
    else:
        speech("Good evening, Lucifer this side.")
    speech("May I help you?")

'''
This following function is the main source of our command for the voice assistant project. This is the base of our operation 
for the voice assistant. From here we can decide the time duration of our speech, the listening of our audio from the given source
and initializng what the user said after recognizing the audio as an input.

eyr9894234=-23=4-02=3-04=-2304-=m.vm.cmx.v4-23-=40///
??@@@0230-32390239023--032%%*&^*&*(())00900--0-=09-(()(&^%R))
&*)*)&(^&(&)&)(----()*@(*)98029800*(@^ksdjkhdkfhsdi_(-9-01293-923-4)))

'''
# Recognize user command through speech
def inputCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try: #try and catch method is applied for exception handling for the given function
        print("Initializing...")
        ask = r.recognize_google(audio, language="en-in")
        print(f"You said: {ask}\n")
    except Exception as e:
        print("Anything else?")
        speech("Anything else?")
        return "None"
    return ask

'''
The following commands in the function are the ones by which we can open our exisisting application inside the computer operating system or 
web applications by accessing their URL's and Paths. The given function is used to open the application present in the system like Notepad, 
Spotify, command prompt, powershell, google, youtube, instagram, etc., when the user's ask variable satisfies the condition.

2342342=34-=04=23-4=234234-23=4-23=-4=32==2-x=340=230c==fc32=d0=x=
sdf9sd-f-=s0f-=s0df04-20344=0sdd0v=0v=sv=s0=0fs=0f=we0f=ffgh0=ty0u=
%%^*(@*&*(@_+)+@_+)+)+_)+@)#*)@*#)@-==0=0=@#)_#_kxkvcdsk@_+)+_0=-0+_

'''
# Open system apps or URLs from the database
def openComm(ask):
    ask = ask.replace("hey " + AI_NAME, "").replace("open", "").lower().strip()
    if ask != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (ask,))
            results = cursor.fetchall()
            if len(results) != 0:
                print("Opening " + ask)
                speech("Opening " + ask)
                os.startfile(results[0][0])
            else:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (ask,))
                results = cursor.fetchall()
                if len(results) != 0:
                    print("Opening " + ask)
                    speech("Opening " + ask)
                    webbrowser.open(results[0][0])
                else:
                    print("Opening " + ask)
                    speech("Opening " + ask)
                    os.system('start ' + ask)
        except:
            speech("Something went wrong")

'''
The following two functions are used here to automate youtube videos and play them according to the instructions given by the user. The first
function is used here to call the second function which helps in responding to the user's input an gives output accordingly. The second function
searches the video on youtube which the user has demanded accordingly.

1hn341hn34ojkhn13324ok14234-1-12312-312-31-231-2o3-1o3o49o-=140=-2304
1=934-=019o4-=0o04=-3904=9o2-23mrp23mr-23o -=r59o=24-rof-=-=w9f=s9o=3=
492-0kclm$^)()_)_+(_+)*( (=90=-9=-9=80 7)_)(_*)@&(&@)_#*I()_@U)EWJM@KOL

'''
# Automating YouTube search
def Youtube(ask):
    search = ex_yt(ask)
    print("Playing " + search + " on YouTube")
    speech("Playing " + search + " on YouTube")
    auto.playonyt(search)

def ex_yt(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    check = re.search(pattern, command, re.IGNORECASE)
    return check.group(1) if check else None

'''
The following function is used to import and process the functions of the gemini API, google's own personal A.I. and it automates the input search
given by the user. This Python code defines a function genZ that interacts with the Gemini AI model to generate text responses to user input. 
It loads environment variables, configures the Gemini AI API, starts a chat session, sends user input, processes the model's response, and then 
both prints and speaks the response. Error handling is implemented to gracefully handle potential exceptions.
'''

# Call generative AI for responses
def genZ(user_input):# defining a function with an argument...
    load_dotenv()# This line loads environment variables from a .env file, i.e., API key.

    genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # configuration of API with its key...
    # It creates a dictionary...
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 500,
        "response_mime_type": "text/plain",
    }

 # specifying the generative A.I. model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    history = [] # To store the chat in this empty list.

    try:
        chat_session = model.start_chat(history=history) # This will start a new chat session with the model, providing the existing chat history.
        response = chat_session.send_message(user_input)# Sends user_input and receive response
        model_response = response.text # This extracts text content from model_response
        print(f'luCpher: {model_response}\n')# Printing model_response to the console...

        history.append({"role": "user", "parts": [user_input]})# To append user input to the chat history
        history.append({"role": "model", "parts": [model_response]})# To append the model response to the chat history
        engine.say(model_response)
        engine.runAndWait()
    except Exception as e:
        print(f"Error calling Gemini AI: {e}")# prints an error message
        speech("Sorry, something went wrong with the API module.")# speaks the apology for error.

# Main control function
if __name__ == "__main__":  
    greet()  # Greet the user based on time of the day
    while True:
        ask = inputCommand().lower()

        # Predefined commands
        if 'open' in ask:  # For opening system or web applications
            openComm(ask)

        elif 'on youtube' in ask:  # To play youtube videos
            Youtube(ask)

        # For asking the time
        elif 'the time' in ask:
            string_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(string_time)
            speech(string_time)

        # Some common hot word responses
        elif 'who are you' in ask or "what's your name" in ask or "what is your name" in ask or "tell me about yourself" in ask:
            print("I am luCpher, your personal virtual assistant and am here to make your tasks easy.")
            speech("I am lucifer, your personal virtual assistant and am here to make your tasks easy. Anything I can help you with?")

        elif 'good job' in ask or 'good job lucifer' in ask or 'lucifer good job' in ask or 'good job lucy' in ask:
            print('Thank You. Any more orders for me to get more such compliments?')
            speech('Thank You! Any more orders for me to get more such compliments?')

        elif 'nothing' in ask or 'you can go' in ask or 'you may leave' in ask: # To ask our assistant to leave the task....
            print('As you wish. Feel free to call me again. Goodbye!')
            speech('As you wish. Feel free to call me again. Goodbye.')
            break

        elif 'search' in ask:
            auto.search(ask.replace('search', '')) # To search the given queries in google search engine...

        else:
            # If no predefined command matches, go through the gemini_api....
            genZ(ask)
