import pyttsx3
import os
import webbrowser

engine = pyttsx3.init()  # object creation

""" RATE"""
engine.setProperty('rate', 150)  # setting up new voice rate

"""VOLUME"""
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

"""******************************************************************************************************************"""
print()
print("Welcome, I am your personal assistant.")
pyttsx3.speak("Welcome, I am your personal assistant.")
print("I am here to help you.")
pyttsx3.speak("I am here to help you.")
print("You may instruct me by typing the request.")
pyttsx3.speak("You may instruct me by typing the request.")

"""******************************************************************************************************************"""
print()
"""******************************************************************************************************************"""

print("Here are some instruction for using me -")
pyttsx3.speak("Here are some instruction for using me -")

print()

print("   1. If you want to open external applications and it is not working, then make shore to mention it."
      " For example, 'I want to open an external application.'")
pyttsx3.speak("1, If you want to open external applications and it is not working, then make shore to mention it."
              " For example, 'I want to open an external application.'")

print()

print("   2. If you see the output as, "
      "'xyz is not recognized as an internal or external command,operable program or batch file.',"
      " where xyz is the name of application, then make shore that path of that application is set.")
pyttsx3.speak("2, If you see the output as, "
              "'xyz is not recognized as an internal or external command,operable program or batch file.',"
              " where xyz is the name of application, then make shore that path of that application is set.")

print()

print("If the above problem occur, then you can ask me 'How to set path?' when ever you want.")
pyttsx3.speak("If the above problem occur, then you can ask me, 'How to set path? when ever you want.")

"""******************************************************************************************************************"""
print()
"""******************************************************************************************************************"""

not_words = ["not", "don't", "doesn't", "never", "hadn't", "can't", "didn't"]
start_words = ["start", "open", "unfold", "begin", "increase", "decrease", "jump", "run", "execute", "do", "does",
               "show", "take", "play", "tell"]
off_words = ["exit", "quit", "leaving", "going", "withdraw", "leave", "close", "retreat"]

"""******************************************************************************************************************"""

"""******************************************************************************************************************"""

re_start = True

while re_start:
    print("Enter your request : ")
    pyttsx3.speak("Enter your request")
    request = list(input().split(" "))
    print()

    is_start_word = False

    for word in start_words:
        if word in request:
            is_start_word = True
            break

    is_not_word = False

    for word in not_words:
        if word in request:
            is_not_word = True
            break

    for word in off_words:
        if word in request and (not is_not_word):
            print("Thanks for using me.")
            pyttsx3.speak("Thanks for using me.")
            re_start = False
            break

    if "set" in request and "path" in request and not is_not_word:
        print("To set the path of application follow the following steps -\n"
              "Step 0: In Search, search the application, open file location and copy the path."
              "Step 1: In Search, search for Environment Variables.\n"
              "Step 2: Click Edit the system Environment Variables.\n"
              "For Step 2 you can request me to open 'System Properties'.\n"
              "Step 3: Click Environment Variables which is in Advanced section of System Properties.\n"
              "Step 4: In system variable, double click on 'path'.\n"
              "Step 5: Click 'New' and type the path of application.\n"
              "Step 6: Press ok then ok and then ok.")
        pyttsx3.speak("To set the path of application follow the following steps -\n"
                      "Step 0: In Search, search the application, open file location and copy it."
                      "Step 1: In Search, search for Environment Variables.\n"
                      "Step 2: Click Edit the system Environment Variables.\n"
                      "For Step 2 you can request me to open 'System Properties'.\n"
                      "Step 3: Click Environment Variables which is in Advanced section of System Properties.\n"
                      "Step 4: In system variable, double click on 'path'.\n"
                      "Step 5: Click 'New' and type the path of application.\n"
                      "Step 6: Press ok then ok and then ok.")

        print()

        print("For now, I am closing the terminal. You may set the path of application.\nThanks for using me.")
        re_start = False

    if not re_start:
        break

    if is_start_word and (not is_not_word):
        if "chrome" in request or "browser" in request:
            print("Do you want to open chrome with any website ? (y/n)")
            pyttsx3.speak("Do you want to open chrome with any website ? If yes, then press y, else n")
            temp = input().lower()
            if temp == "y":
                print("Enter URL eg- yahoo.com: ")
                pyttsx3.speak("Enter URL")
                url = f'http://{input()}/'
                # MacOS
                # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
                # Windows
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                # Linux
                # chrome_path = '/usr/bin/google-chrome %s'
                webbrowser.get(chrome_path).open(url)
            elif temp == "n":
                os.system("chrome")
        elif "wordpad" in request or ("text" in request and "editor" in request):
            os.system("write")
        elif "jupyter" in request or "notebook" in request:
            os.system("jupyter notebook")
        elif "oracle" in request or ("virtual" in request and "machine" in request):
            print("Do you want to open a pirticular virtual machine? (y/n)")
            pyttsx3.speak("Do you want to open a pirticular virtual machine? If yes, then press y, else n")
            temp = input().lower()
            if temp == "y":
                print("Enter the name of virtual machine that you have created in virtual machine : ")
                pyttsx3.speak("Enter the name of virtual machine that you have created in virtual machine")
                vm_name = input()
                os.system(f"VBOxManage startvm {vm_name}")
            elif temp == "n":
                os.system("VirtualBox")
        elif "ms" in request or "microsoft" in request or "office" in request:
            if "excel" in request:
                os.system("start excel")
            elif "word" in request:
                os.system("start winword")
            elif ("power" in request and "point" in request) or "ppt" in request or "powerpoint" in request:
                os.system("start powerpnt")
        elif "telegram" in request or "Telegram" in request:
            os.system("telegram")
        elif ("team" in request and "viewer" in request) or "teamviewer" in request:
            os.system("TeamViewer")
        elif ("utorrent" in request and "web" in request) or "utorrentweb" in request or\
            ("u" in request and ("torrent" in request or "Torrent" in request) and
             ("web" in request or "Web" in request)):
            os.system("utweb")
        elif "whatsapp" in request or "WhatsApp" in request or "whatsApp" in request:
            os.system("WhatsApp")
        elif "atom" in request:
            os.system("atom")
        elif "notepad" in request or "editor" in request:
            os.system("notepad")
        elif "calculator" in request or "calc" in request:
            os.system("calc")
        elif ("windows" in request and "media" in request and "player" in request) or \
                ("song" in request and "player" in request) or ("mp3" in request and "player" in request):
            os.system("wmplayer")  # or os.system("dvdplay")
        elif "vlc" in request or ("video" in request and "player" in request) or \
                ("mp4" in request and "player" in request):
            os.system("vlc")
        elif "character" in request and "map" in request:
            os.system("charmap")
        elif "cmd" in request or ("command" in request and "prompt" in request):
            os.system("cmd")
        elif "control" in request and "panel" in request:
            os.system("control")
        elif "displayswitch" in request or ("switch" in request and "display" in request):
            os.system("displayswitch")
        elif "fax" in request and "cover" in request and "page" in request and "editor" in request:
            os.system("FXSCOVER")
        elif "task" in request and "manager" in request:
            os.system("Taskmgr")  # or os.system("LaunchTM")
        elif "magnifier" in request:
            os.system("Magnify")
        elif ("Windows" in request and "mobility" in request and "center" in request) or \
                (("increase" in request or "decrease" in request or "change" in request) and "brightness" in request):
            os.system("mblctr")
        elif ("System" in request or "pc" in request) and "information" in request:
            os.system("msinfo32")
        elif "paint" in request:
            os.system("mspaint")
        elif "remote" in request and "desktop" in request and "connection" in request:
            os.system("mstsc")
        elif "narrator" in request:
            os.system("Narrator")
        elif ("user" in request and "accounts" in request) or (
                ("user" in request or "account" in request) and "list" in request):
            os.system("Netplwiz")
        elif ("windows" in request or "windows" in request) and "features" in request:
            os.system("OptionalFeatures")
        elif "on" in request and "screen" in request and "keyboard" in request:
            os.system("osk")
        elif ("performance" in request and "monitor" in request) or ("performance" in request and "system" in request):
            os.system("perfmon")
        elif "presentation" in request and "setting" in request:
            os.system("PresentationSettings")
        elif "steps" in request and "recorder" in request:
            os.system("psr")
        elif "quick" in request and "assist" in request:
            os.system("quickassist")
        elif "resource" in request and "monitor" in request:
            os.system("resmon")
        elif "system" in request and "restore" in request:
            os.system("rstrui")
        elif (("increase" in request or "decrease" in request or "change" in request) and "volume" in request) or \
                "volume" in request and "mixer" in request:
            os.system("SndVol")
        elif ("snipping" in request and "tool" in request) or ("screenshot" in request):
            os.system("SnippingTool")
        elif "system" in request and "properties" in request:
            os.system("SystemPropertiesComputerName")
        elif ("windows" in request and "defender" in request) or "firewall" in request or (
                "advanced" in request and "security" in request):
            os.system("WF")
        elif "work" in request and "folders" in request:
            os.system("WorkFolders")
        elif "authorization" in request and "manager" in request:
            os.system("azman")
        elif "color" in request or "colour" in request and "management" in request:
            os.system("colorcpl")
        elif "date" in request:
            os.system("Date")
        elif "external" in request and "application":
            print("Enter the name of application : ")
            pyttsx3.speak("Enter the name of application")
            temp = input()
            os.system(temp)
        else:
            print("Sorry, doesn't support :-( ")
            pyttsx3.speak("Sorry, doesn't support.")

"""******************************************************************************************************************"""
