#Please add your wolfram and weather api keys

#Pronunciation of User's name:
Username = 'Fyke'

# modules:
import comtypes.client, time, datetime, wikipedia, os, subprocess, speech_recognition as sr, webbrowser, wolframalpha, json, requests

try:
    from ecapture import ecapture as ec
except:
    time.sleep(0)

#text to speech engines: gtts (unofficial google text to speech engine using Google Translate's text-to-speech API (therefore needs an internet connection) ), pyttsx3 (tts library with multiple engines)
try:
    import gtts
    from playsound import playsound
except:
    import pyttsx3

#-----------------------------------------------------------------------------

def StartGideon():
    #Code for using pyttsx3
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    #-------------------------------------

    def speak(text):
        #try:
        tts = gtts.gTTS(text)
        tts.save("speech.mp3")
        playsound("speech.mp3")
        #except:
         #   engine.say(text)
          #  engine.runAndWait()

    #-------------------------------------

    def wishMe():
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            speak('Hello, good morning '+ Username)
            speak("How can I help you?")
            print('Hello, good morning '+ Username)
        elif hour>=12 and hour<18:
            speak('Hello, good afternoon ' + Username)
            speak("How can I help you?")
            print('Hello, good afternoon ' + Username)
        else:
            speak('Hello, good evening ' + Username)
            speak("How can I help you?")
            print('Hello, good evening ' + Username)

    #-------------------------------------

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)

            try:
                statement=r.recognize_google(audio,language='en-in')
                print("user said:{ ", str(statement), "}\n")

            except Exception as e:
                print("Not catching anything")
                return "None"
            return statement

    print("Loading Gideon resources")
    speak("Loading Gideon's resources")
    wishMe()

    #---------------------------------------------------------

    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "bye" in statement in statement:
            speak('Gideon is shutting down, Good bye')
            print('Gideon is shutting down, Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://https://www.bbc.co.uk//news")
            speak('Here are some headlines from the BBC')
            time.sleep(6)
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            #gets working directory
            directory = os.getcwd()
            f = open(directory + "Computer-Resources\PortableApps\Gideon\WolframAlphaID.txt", "r")
            app_id = f.read()
            #client = wolframalpha.Client('')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Gideon, your automated personal assistant. I am programmed to help with tasks like opening certain applications, getting top headline news from around the world and you can ask me computational or geographical questions too!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by " + Username)
            print("I was built by " + Username)
        elif "weather" in statement:
            api_key = ""
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        elif "restart" in statement or "reboot" in statement:
            speak("Ok , your pc will reboot in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/r"])
        elif "shutdown" in statement or "turn off" in statement or "power off" in statement:
            speak("Ok , your pc will power off in 10 sec. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/s"])
        time.sleep(3)

#---------------------------------------------------------

TRAY_TOOLTIP = 'Gideon'
TRAY_ICON = directory+'Computer-Resources\\PortableApps\\Gideon\\microphone.ico'

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item

class TrApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    TrayApp = TrApp(False)
    TrayApp.MainLoop()

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        app = StartGideon()
        app.mainloop()

    def on_exit(self, event):
        sys.exit(0)

#--------------------------------------running program---------------------------------------#

if __name__ == "__main__":
    main()
