import pyttsx3
import os
import time
import pyjokes

engine = pyttsx3.init()
engine.setProperty('rate',150)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" # Use female voice 
engine.setProperty('voice', voice_id) 
engine.setProperty('volume', 3) 
engine.runAndWait() 
os.system("cls")
print("                                U^.^U - EL                            \n")
pyttsx3.speak("hello there! ........how are you?")
pyttsx3.speak("I'm El , I'm a python program that can help you with various things on your system")
time.sleep(1)
print("May i ask, who are you?? :", end = ' ')
pyttsx3.speak(" and May i ask, , , who are you??")
gar= ("my", "name", " Name", "is", "you", "can", "its", "it" ,"call" ,"me" ,"i" ,"am", "this","should","would","side")
nam = list(input().split())
name = [item for item in nam if item not in gar]
print("Hello! " + name[0])
pyttsx3.speak("hello " + name[0]+ " ?!." + " its nice to meet you") 
print( """ I can help u with the below programs. Feel free to tell me which programs you want to use.
    Google (User/private)                          --- Browser                                
    This PC                                        --- Windows File Explorer  
    Media player                                   --- Windows Media Player                             
    PAINT                                          --- Can be used to create/edit/paint new images
    Notepad                                        --- Windows Default Text Editor                              
    Command Prompt (user/admin)                    --- Windows defaul Terminal
    PowerShell (user/admin)                        --- MS framework for automating tasks using a command-line 
                                                       shell and an associated scripting language.
    Calculator                                     --- Can be used to perform simple/adv calculations                                          
    Task Manager                                   --- System monitor  
    Math input panel                               --- Convert handwritten notes into Text/No.s
    QuickAssist                                    --- Microsoft Quick Assist enables two people to share 
                                                       a computer over a remote connection so that one
                                                       person can help solve problems on the other 
                                                       person’s computer.
    Snipping Tool                                  --- It can take still screenshots of an open window,
                                                       rectangular areas, a free-form area, or the 
                                                       entire screen.
    Steps Recorder                                 --- A program that helps you troubleshoot a problem 
                                                       on your device by recording the exact steps you 
                                                       took when the problem occurred.              
    Wordpad                                        --- A more advance version of Notepad
    Search (type search)                           --- If you got stuck over anything, 
                                                       I can help u directly search it on web 
    
        !!         [NOTE]--- I'm still learning and always eager to learn new things,         !!
        !!                 so incase u wanna teach me some be sure to tell me,                !!
        !!                     i will let you play with my brain bit :D                       !!
        
        !!                  After teaching me u can reload me manually or 
                                just tell and i will do it for u U^_^U    
    
    
    """)
pyttsx3.speak(""" I can help u with the below programs. feel free to tell me which programs you want to use.""")


def program(ch):
    if (("run"in ch) or ("launch" in ch) or ("execute" in ch or "use" in ch ) or ("start" in ch) or ("open" in ch) ) and (("notepad" in ch) or ("editor" in ch) or ("text" in ch)): 
        print ("\nDo you want to open any specific file : ", end = ' ')
        temp = input()
        temp.lower()
        if temp == "no" or temp == "nope" or temp == "na": 
            os.system("start notepad")
        elif temp == "yes" :
            print("then Give me the name of that file :",end = ' ')
            temp = input()
            os.system("start notepad " + temp)
        else:
            os.system("start notepad " + temp)
    
    
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("chrome" in ch or "google"in ch or "browser"in ch) and ("private" in ch or "incognito" in ch)) : 
        # os.system("start chrome /incognito")
        print ("\nDo you want to open any specific webpage : ", end = ' ')
        temp = input()
        temp.lower()
        if temp == "no" or temp == "nope" or temp == "na": 
            os.system("start chrome /incognito")
        elif temp == "yes" :
            print("then Give me the link to that webpage :",end = ' ')
            temp = input()
            os.system("start chrome /incognito " + temp)
        else:
            os.system("start chrome /incognito " + temp)
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("chrome" in ch or "google"in ch or "browser"in ch)): 
        print ("\nDo you want to open any specific webpage : ", end = ' ')
        temp = input()
        temp.lower()
        if temp == "no" or temp == "nope" or temp == "na": 
            os.system("start chrome")
        elif temp == "yes" :
            print("then Give me the link to that webpage :",end = ' ')
            temp = input()
            os.system("start chrome " + temp)
        else:
            os.system("start chrome " + temp)


    elif (("run" in ch or "launch" in ch or "execute" in ch  or "use" in ch or "start" in ch or "open" in ch ) and ("wmp" in ch or "wmplayer" in ch or "media" in ch or "player" in ch)): 
        os.system("start wmplayer")
        
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("my computer" in ch or "this pc" in ch or "explorer" in ch)): 
        os.system("start explorer")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("calc" in ch or "calculator" in ch )): 
        os.system("start calc")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("paint" in ch or "mspaint" in ch )): 
        os.system("start mspaint")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("cmd" in ch or "prompt" in ch or "command" in ch or "terminal" in ch)): 
        print ("\nDo you want ADMIN privelages (Yes/No) : ", end = ' ')
        temp = input()
        temp.lower()
        if "n" in temp: 
            os.system("start cmd")
        elif "y" in temp :
            os.system(r"powershell -command start-process cmd -verb runas ")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("powershell" in ch )): 
        print ("\nDo you want ADMIN privelages (Yes/No) : ", end = ' ')
        temp = input()
        temp.lower()
        if "n" in temp: 
            os.system("start powershell")
        elif "y" in temp :
            os.system(r"powershell -command start-process powershell -verb runas ")
                    
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("taskmanager" in ch or "tast manager" in ch or "ram" in ch or "cpu" in ch)): 
        os.system("start taskmgr")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("math" in ch or "panel" in ch )): 
        os.system("start mip")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("quickassist" in ch or "quick" in ch or "assist" in ch or "remote" in ch)): 
        os.system("start quickassist")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("snip" in ch or "screenshot" in ch )): 
        os.system("start snippingtool")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("recorder" in ch or "step" in ch )): 
        os.system("start psr")
    elif("clear" in ch or "cls" in ch or "clean" in ch ):
        os.system("cls")
        print("                                U^.^U - EL                            \n")
    elif (("run" in ch or "launch" in ch or "execute" in ch or "use" in ch  or "start" in ch or "open" in ch ) and ("wordpad" in ch or "word" in ch )): 
        os.system("start wordpad")

    elif ("search" in ch or "about" in ch):
        print ("""\n
                  I'm still not smart enough to search more than 1 word,
                  so if you want to search more than 1 word then pls seperate 
                  them using an underscore: '_' instead of a space: ' ' """)
        print ("\nWhat do u want to Search about : ", end=' ')
        s = input()
        os.system("start chrome google.com/search?q=" + s)
        
    elif ("source" in ch or "teach" in ch or "update" in ch):
        os.system("start notepad EL.py")
        
    elif ("restart" in ch or "reexecute" in ch or "reload" in ch ) :
        os.system("start python EL.py")
        exit()
    elif "time" in ch:
        os.system("cd /")
        print(os.popen("time /t").read())
        pyttsx3.speak(os.popen("time /t").read())
    elif "date" in ch:
        os.system("cd /")
        print(os.popen("date /t").read())
        pyttsx3.speak("today's date is " + os.popen("date /t").read())
    elif ("joke" in ch or "funny"in ch ):
        joke = pyjokes.get_joke(language = 'en', category = 'all')
        print(joke)
        pyttsx3.speak(joke)
    elif ("exit" in ch or "close" in ch or "bye" in ch):
        print ("Gud-Byeeeeeee, hope we meeet again ")
        pyttsx3.speak("It was really nice meeting you, but i guess this is good bye, hope we meet again")
        
        exit()
    elif (not (ch and ch.strip())):
        print(end = "")
    else:
        print("pls "+ name[0] + " can u repeat!. i didn't quite get it.\n if you just wrote a name of a program then please \nalso tell what do u want me to do with it.")
        pyttsx3.speak("please "+ name[0] + " can u repeat that!. i didn't quite get it.if you just wrote a name of a program then please also tell what do u want me to do with it.")
        check()
    
    

def check():
    print("Chat with me with your requirements : " ,end=' ')
    ch = input()
    ch.lower()
    if ((ch and ch.strip())):
        pyttsx3.speak("Initiating request ")
    if ("dont" not in ch) and ("not " not in ch) and ("don't" not in ch):
        program(ch)
        if ((ch and ch.strip())):
            print("----------Hope i could be of help, feel free to ping me again------------")
            pyttsx3.speak("feel free to tell me if u want anything else")
    else:
        print ("Are u commanding me to !!NOT!! open some thing \nThen just don't command me \nIts pretty useless if you see!")
        pyttsx3.speak("Are u commanding me !to !!NOT!! open some thing. \nThen just don't command me .\nIts pretty useless if you see!" )


while True:
    check()

engine.runAndWait()
