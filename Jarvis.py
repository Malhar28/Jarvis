from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import random

from pywikihow import search_wikihow
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import pyjokes
import json
import pyautogui
import time
from email.mime.multipart import MIMEMultipart
from playsound import playsound
import PyPDF2
import operator
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search
import speedtest
from tkinter.colorchooser import *
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def command():
    m = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . . . .")
        m.pause_threshold = 1
        audio = m.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing . . . .")
        query = m.recognize_google(audio, language="en-in")
        print(f"User said {query}")

    except Exception as e:
        speak("Say that again")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 <= hour <= 18:
        speak("Good Afternoon ")
    else:
        speak("good evening")


def news():
    speak("Today's news")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1da02791a84846038d16a71d3e670170"
    page = get(url).json()
    art = page["articles"]
    head = []
    num = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for articles in art:
        head.append(articles["title"])
    for i in range(len(num)):
        print(f"{num[i]} news is: {head[i]}")
        speak(f"{num[i]} news is {head[i]}")
    speak("That's all for to today")


def taskExecution():
    while True:

        query = command().lower()

        if "open notepad" in query:
            notepad_path = "C:\\Windows\\system32\\notepad.exe"
            speak("Opening notepad")
            os.startfile(notepad_path)

        elif "open command prompt" in query:
            speak("Opening Command Prompt")
            os.system("start cmd")

        elif "play music" in query:
            music_path = ""
            songs = os.listdir(music_path)
            random_song = random.choice(songs)
            for song in songs:
                if song.endswith('mp3'):
                    os.startfile(os.path.join(music_path, random_song))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
            print(result)

        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com")

        elif "open instagram" in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com")

        elif "open google" in query:
            speak("sir, what should I search in google")
            search_google = command().lower()
            speak(f"ok sir searching {search_google} in google")
            webbrowser.open(f"{search_google}")

        elif "message" in query:
            speak("Ok sir, what should I send")
            msg = command().lower()
            pywhatkit.sendwhatmsg("NUMBER", f"{msg}", 22, 24)

        elif "open youtube" in query:
            speak("Ok sir. what should I search")
            s = command().lower()
            pywhatkit.playonyt(f"{s}")

        elif "open gmail" in query:
            speak("ok sir,  but whose account should I open")
            query3 = command().lower()
            webbrowser.open('www.gmail.com')

        elif "open python tutorials" in query:
            speak("Ok sir, opening python tutorials")
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

        elif "open documentation of modules of python" in query:
            speak("Ok sir, opening the official documentation of python")
            webbrowser.open("https://docs.python.org/3/py-modindex.html")

        elif "send a mail" in query:
            speak("Sir what should I say. Or should I send a file")
            query = command().lower()
            if "send a file" in query:
                email = ""
                password = ""
                send_email = ""
                speak("Ok sir, what should I keep the subject for this mail")
                query = command().lower()
                subject = query
                speak("Sir, what is the message ")
                query2 = command().lower()
                message = query2
                speak("sir, please enter below the path of the file want to send")
                file_location = input(f"Enter the path here :- ")

                speak("Ok sir, please wait the mail is sending")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'Plain'))

                file_name = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders = encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s " % file_name)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_email, text)
                server.quit()
                speak("Message has been sent successfully")

            else:
                email = ""
                password = ""
                send_email = ""
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_email, message)
                server.quit()
                speak("Message has been sent successfully")

        elif "close notepad" in query:
            speak("Ok sir, closing  notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query:
            speak("Ok sir, closing command prompt")
            os.system("taskkill /f /im command prompt.exe")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            speak("Please type the time below in the terminal for alarm")
            inp = int(input(""))
            if nn == inp:
                speak(f"Sir wake, up its already {inp}")

        elif "tell a joke" in query:
            joke = pyjokes.get_jokes()
            speak(joke)
            print(joke)

        elif "shut down the system" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("restarting the system")
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetupSuspendState 0,1,0 ")

        elif "tell me the news" in query:
            speak("Ok sir, please wait, I am fetching today's news")
            news()

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell my location" in query or "where am i" in query:
            try:
                speak("Ok sir, please wait I am checking your location")
                ip_add = get("https://api.ipify.org").text
                print(ip_add)
                url = 'https://get.geojs.io/v1/ip/geo/your ip address.json'
                geo_requests = get(url)
                geo_data = geo_requests.json
                # print(geo_data)
                state = geo_data['region']
                country = geo_data['country']

                speak(f"sir, i am  not sure but think we are in {state}in {country}")
            except Exception as e:
                print(e)
                speak("Sorry sir but I am not able to find your location ")
                pass

        elif "open pinterest" in query:
            speak("Ok sir, but as per my opinion you should search about new fashionable dresses, would you like to "
                  "do that")
            query_op = command().lower()
            if "yes" in query_op or "yeah" in query_op:
                speak("ok sir, thanks for giving me a chance for my opinion")
                webbrowser.open("https://in.pinterest.com/search/pins/?q=latest%20dress&rs=typed&term_meta["
                                "]=latest%7Ctyped&term_meta[]=dress%7Ctyped")
            else:
                speak("ok sir, opening pinterest")
                webbrowser.open("https://in.pinterest.com/")

        elif "i want to purchase" in query or "i want to buy" in query or "i want to do shopping" in query:
            speak("Ok sir, what can i do")
            query = command().lower()
            if "open th best website" in query:
                speak("ok sir, for electronics, amazon and flipcart are best. for clothes, no competition of meesho. "
                      "for ")
                webbrowser.open('www.amazon.com')

        elif "take screenshot" in query:
            speak("ok sir, what name should I give to this screenshot file")
            name = command().lower()
            speak("ok sir, please don't change the screen, I am taking the screenshot")
            time.sleep(2)
            pic = pyautogui.screenshot()
            pic.save(f"{name}.png")
            speak("Sir, I took the screenshot of this screen now you can change")

        elif "read pdf" in query:
            def pdf_reader():
                try:
                    book = open(".pdf", 'rb')
                    pdf_read = PyPDF2.PdfFileReader(book)
                    pages = pdf_read.numPages
                    speak(f"Total number of pages in this book are {pages}")
                    speak("sor, please enter below the page number from which you want to start")
                    p_number_to_start = int(input(":-"))
                    page = pdf_read.getPage(p_number_to_start)
                    text = page.extractText()
                    speak(text)
                except Exception as e:
                    speak("Sir, please whether you have entered the name of the pdf correctly")
                    print(e)

        elif "miss" in query:
            speak("sir, i missed you too")

        elif "calculation" in query:
            m = sr.Recognizer()
            with sr.Microphone() as source:
                speak("sir, please tell me what you want to calculate")
                print("Listening . . . . .")
                m.adjust_for_ambient_noise(source)
                audio = m.listen(source, timeout=1, phrase_time_limit=5)
            myString = m.recognize_google(audio)
            print(myString)
            try:
                def get_operator(op):
                    return {
                        "+": operator.add,  # plus
                        "-": operator.sub,  # minus
                        "x": operator.mul,  # multiply
                        "divided": operator.__truediv__,  # division
                    }[op]

                def eval_binary_expr(op1, oper, op2):  # example:- 5 plus 10
                    op1, op2 = int(op1), int(op2)
                    return get_operator(oper)(op1, op2)

                speak("sir, the answer is")
                speak(eval_binary_expr(*(myString.split())))

            except Exception as e:
                print(e)

        elif "sleep" in query:
            speak("ok sir, I am going in sleep mode, if you have some work wake me")
            break

        elif "hello" in query:
            speak("hello sir, is there something in which can I help")

        elif "yahoo" in query:
            speak("ok sir, opening yahoo mails")
            webbrowser.open("https://mail.yahoo.com/")

        elif "bored" in query or "board" in query:
            speak("sir, i think you should watch videos on youtube")
            speak("sir, should i open youtube")
            q1 = command().lower()
            if "yes" in q1:
                webbrowser.open('www.youtube.com')
            elif "no" in q1:
                speak("ok sir")

        elif "jarvis" in query:
            speak("yes,sir")

        elif "what can you do" in query:
            speak("sir I am opening a pdf, all detail are there about me")
            pdf_path = 'Documents\\Jarvis_details'
            webbrowser.open_new(pdf_path)

        elif "increase volume" in query:
            pyautogui.press("volumeup")

        elif "decrease volume" in query:
            pyautogui.press("volumedown")

        elif "mute" in query or "unmute" in query:
            pyautogui.press("volumemute")

        elif "jarvis" in query:
            speak("yes,sir")

        elif "check net speed" in query or "internet" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif "check battery" in query or "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            p = battery.percent
            speak(f"sir remaining battery is {p} percent")

        elif "coding" in query:
            speak("ok sir, but what should i open, jetbrains or vs code")
            ask = command().lower()
            if "jetbrains" in ask or "jetbrain" in ask or "pycharm" in ask:
                speak("ok, sir opening jetbrains")
                file_path = "ENTER THE PATH OF PYCHARM"
                os.startfile(file_path)
            elif "vs code" in ask or "visual studio code" in ask or "vscode" in ask:
                speak("ok sir, opening visual studio code")
                file_path = "PATH OF VS CODE"
                os.startfile(file_path)

        elif "painter" in query:
            speak("ok sir, opening painter")

            def painter():

                win_width = 900
                win_height = 450

                class Application(Frame):

                    def __init__(self, master=None, bgcolor='#000000'):
                        super().__init__(master)
                        self.master = master
                        self.bgcolor = bgcolor
                        self.fgcolor = '#ff0000'
                        self.lastDraw = 0
                        self.startDrawFlag = False
                        self.x = 0
                        self.y = 0
                        self.pack()
                        self.create_widget()

                    def create_widget(self):
                        self.drawpad = Canvas(self.master, width=win_width, height=win_height * 0.9, bg=self.bgcolor)
                        btn_start = Button(self.master, text='START', name='start')
                        btn_pen = Button(self.master, text='PEN', name='pen')
                        btn_rect = Button(self.master, text='SQUARE', name='rect')
                        btn_clear = Button(self.master, text='CLEAR', name='clear')
                        btn_erasor = Button(self.master, text='ERASER', name='eraser')
                        btn_line = Button(self.master, text='LINE', name='line')
                        btn_lineArrow = Button(self.master, text='LINE ARROW', name='lineArrow')
                        btn_color = Button(self.master, text='COLOR', name='color')
                        self.drawpad.pack()
                        btn_start.pack(side='left', padx='10')
                        btn_pen.pack(side='left', padx='10')
                        btn_rect.pack(side='left', padx='10')
                        btn_clear.pack(side='left', padx='10')
                        btn_erasor.pack(side='left', padx='10')
                        btn_line.pack(side='left', padx='10')
                        btn_lineArrow.pack(side='left', padx='10')
                        btn_color.pack(side='left', padx='10')
                        btn_pen.bind_class('Button', '<1>', self.eventManager)
                        self.drawpad.bind('<ButtonRelease-1>', self.stopDraw)

                        self.master.bind('<KeyPress-r>', self.my_short_cut)
                        self.master.bind('<KeyPress-y>', self.my_short_cut)
                        self.master.bind('<KeyPress-g>', self.my_short_cut)

                    def my_short_cut(self, event):
                        if event.char == 'r':
                            self.fgcolor = "#ff0000"
                        elif event.char == 'g':
                            self.fgcolor = "#00ff00"
                        elif event.char == 'y':
                            self.fgcolor = "#ffff00"

                    def stopDraw(self, event):
                        self.startDrawFlag = False
                        self.lastDraw = 0

                    def eventManager(self, event):
                        name = event.widget.winfo_name()
                        print(name)
                        if name == 'line':
                            self.drawpad.bind('<B1-Motion>', self.myline)
                        elif name == 'lineArrow':
                            self.drawpad.bind('<B1-Motion>', self.mylineArrow)
                        elif name == 'rect':
                            self.drawpad.bind('<B1-Motion>', self.myRect)
                        elif name == 'pen':
                            self.drawpad.bind('<B1-Motion>', self.myPen)
                        elif name == 'eraser':
                            self.drawpad.bind('<B1-Motion>', self.myEraser)
                        elif name == 'clear':
                            self.drawpad.delete('all')
                        elif name == 'color':
                            c = askcolor(color=self.fgcolor, title='color')
                            self.fgcolor = c[1]

                    def startDraw(self, event):
                        self.drawpad.delete(self.lastDraw)
                        if not self.startDrawFlag:
                            self.startDrawFlag = True
                            self.x = event.x
                            self.y = event.y

                    def myEraser(self, event):
                        self.startDraw(event)
                        self.drawpad.create_rectangle(event.x - 4, event.y - 4, event.x + 4, event.y + 4,
                                                      fill=self.bgcolor)
                        self.x = event.x
                        self.y = event.y

                    def myPen(self, event):
                        self.startDraw(event)
                        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
                        self.x = event.x
                        self.y = event.y

                    def myRect(self, event):
                        self.startDraw(event)
                        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y,
                                                                      outline=self.fgcolor)

                    def mylineArrow(self, event):
                        self.startDraw(event)
                        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST,
                                                                 fill=self.fgcolor)

                    def myline(self, event):
                        self.startDraw(event)
                        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

                if __name__ == '__main__':
                    root = Tk()
                    root.geometry(str(win_width) + 'x' + str(win_height) + '+200+300')
                    root.title('Painter')
                    app = Application(master=root)
                    root.mainloop()

            painter()

        elif "game" in query:
            speak("ok sir, starting the game")

            def game():
                def drawBoard(board):
                    # This function prints out the board that it was passed

                    # "board" is a list of 10 strings representing the board (ignore index 0)
                    print('   |   |')
                    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
                    print('   |   |')
                    print('-----------')
                    print('   |   |')
                    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
                    print('   |   |')
                    print('-----------')
                    print('   |   |')
                    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
                    print('   |   |')

                def inputPlayerLetter():
                    # Lets the player type which letter they want to be.
                    # Returns a list with the player's letter as the first item, and the computer's letter as second.
                    letter = ''
                    while not (letter == 'X' or letter == 'O'):
                        print('Do you want to be X or O?')
                        letter = input().upper()

                    # The first element in the tuple is the player's letter, the second is the computer's letter.
                    if letter == 'X':
                        return ['X', 'O']
                    else:
                        return ['O', 'X']

                def whoGoesFirst():
                    # Randomly chose the player who goes first.
                    if random.randint(0, 1) == 0:
                        return 'computer'
                    else:
                        return 'player'

                def playAgain():
                    # This function returns True if the player wants to play again, otherwise it returns False.
                    print('Do you want to play again? (yes or no)')
                    return input().lower().startswith('y')

                def makeMove(board, letter, move):
                    board[move] = letter

                def isWinner(bo, le):
                    # Given a board and a player's letter, this function returns True if the player has won.
                    # We use bo instead of board and le instead of letter so we don't have to type so much.
                    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

                def getBoardCopy(board):
                    # Make a duplicate of the board list and return it the duplicate.
                    dupeBoard = []

                    for i in board:
                        dupeBoard.append(i)
                    return dupeBoard

                def isSpaceFree(board, move):
                    # Return true if the passed move is free on the passed board.
                    return board[move] == ' '

                def getPlayerMove(board):
                    # Let the player type in this move.
                    move = ' '
                    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
                        print('What is your next move? (1-9)')
                        move = input()
                    return int(move)

                def chooseRandomMoveFromList(board, movesList):
                    # Returns a valid move from the passed list on the passed board.
                    # Returns None if there is no valid move.
                    possibleMoves = []
                    for i in movesList:
                        if isSpaceFree(board, i):
                            possibleMoves.append(i)

                    if len(possibleMoves) != 0:
                        return random.choice(possibleMoves)
                    else:
                        return None

                def getComputerMove(board, computerLetter):
                    # Given a board and the computer's letter, determine where to move and return that move.
                    if computerLetter == 'X':
                        playerLetter = 'O'
                    else:
                        playerLetter = 'X'

                    # Here is our algorithm for our Tic Tac Toe AI:
                    # First, check if we can win in the next move
                    for i in range(1, 10):
                        copy = getBoardCopy(board)
                        if isSpaceFree(copy, i):
                            makeMove(copy, computerLetter, i)
                            if isWinner(copy, computerLetter):
                                return i

                    # Check if the player could win on his next move, and block them.
                    for i in range(1, 10):
                        copy = getBoardCopy(board)
                        if isSpaceFree(copy, i):
                            makeMove(copy, playerLetter, i)
                            if isWinner(copy, playerLetter):
                                return i

                    # Try to take one of the corners, if they are free.
                    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
                    if move != None:
                        return move

                    # Try to take the center, if it is free.
                    if isSpaceFree(board, 5):
                        return 5

                    # Move on one if the sides.
                    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

                def isBoardFull(board):
                    # Return True if every space on the board has been taken. Otherwise return False.
                    for i in range(1, 10):
                        if isSpaceFree(board, i):
                            return False
                    return True

                print('Wecome to Tic Tac Toe!')

                while True:
                    # Reset the board
                    theBoard = [' '] * 10
                    playerLetter, computerLetter = inputPlayerLetter()
                    turn = whoGoesFirst()
                    print('The ' + turn + ' will go first.')
                    gameIsPlaying = True

                    while gameIsPlaying:
                        if turn == 'player':
                            # Player's turn.
                            drawBoard(theBoard)
                            move = getPlayerMove(theBoard)
                            makeMove(theBoard, playerLetter, move)

                            if isWinner(theBoard, playerLetter):
                                drawBoard(theBoard)
                                print('Hooray! You have won the game!')
                                gameIsPlaying = False
                            else:
                                if isBoardFull(theBoard):
                                    drawBoard(theBoard)
                                    print('The game is a tie!')
                                    break
                                else:
                                    turn = 'computer'

                        else:
                            # Computer's turn.
                            move = getComputerMove(theBoard, computerLetter)
                            makeMove(theBoard, computerLetter, move)

                            if isWinner(theBoard, computerLetter):
                                drawBoard(theBoard)
                                print('The computer has beaten you! You lose.')
                                gameIsPlaying = False
                            else:
                                if isBoardFull(theBoard):
                                    drawBoard(theBoard)
                                    print('The game is a tie!')
                                    break
                                else:
                                    turn = 'player'

                    if not playAgain():
                        break
            game()

        elif "terminate" in query:
            speak("goodbye sir, and have a nice day")
            sys.exit()

        elif "how was your day" in query or "tell me about your day" in query:
            wisher = ["I was having a wonderfull day", "It was a day full of pleasure", "Very nice"]
            speech = random.choice(wisher)
            speak(speech)
            speak("what about you")
            a = command().lower()
            speak("oh that's good")

        elif "git" in query or "github" in query:
            speak("ok sir, opening git hub")
            webbrowser.open('https://github.com/')

        elif "I wanna know about" in query or "tell me" in query:
            import pywikihow
            speak("sir, what you want to know")
            q = command().lower()
            max_results = 1
            know = search_wikihow(q, max_results)
            assert len(know) == 1
            know[0].print()
            speak(know[0].summary)


if __name__ == "__main__":
    while True:
        permission = command().lower()
        if "wake up" in permission or "are you there" in permission or "jarvis are you there" in permission:
            speak("sir, I am always there with you")
            speak("should i start the system")
            q = command()
            if 'yes' in q:
                speak("ok sir starting the system")
                taskExecution()
            elif 'no' in q:
                speak("ok sir")

        elif "terminate" in permission:
            speak("goodbye sir, and have a nice day")
            sys.exit()

        elif "start" in permission:
            speak("ok sir starting the system")
            taskExecution()

        elif "wake up" in permission:
            speak("yes sir")
            speak("should i start the system")
            q = command()
            if 'yes' in q:
                speak("ok sir starting the system")
                taskExecution()
            elif 'no' in q:
                speak("ok sir")

        elif "jarvis" in permission:
            speak("yes, sir")
            taskExecution()
