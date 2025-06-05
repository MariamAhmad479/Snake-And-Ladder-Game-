from tkinter import *
from PIL import ImageTk,Image
import random
from tkinter import messagebox as mbox
from tkinter import ttk 
import re
current_player=True
player1_pos = 0
player2_pos = 0

#positions dictionary
Index={0:(0,720),1:(0,670), 2:(75,670), 3:(150,670), 4:(225,670), 5:(300,670), 6:(375,670), 7:(450,670), 8:(525,670), 9:(600,670), 10:(675,670),
11:(675,600), 12:(600,600), 13:(525,600), 14:(450,600), 15:(375,600), 16:(300,600), 17:(225,600), 18:(150,600), 19:(75,600),
20:(0,600), 21:(0,530), 22:(75,530), 23:(150,530), 24:(225,530), 25:(300,530), 26:(375,530), 27:(450,530), 28:(525,530),
29:(600,530), 30:(675,530), 31:(675,460), 32:(600,460), 33:(525,460), 34:(450,460), 35:(375,460), 36:(300,460), 37:(225,460),
38:(150,460), 39:(75,460), 40:(0,460), 41:(0,390), 42:(75,390), 43:(150,390), 44:(225,390), 45:(300,390), 46:(375,390), 47:(450,390),
48:(525,390), 49:(600,390), 50:(675,390), 51:(675,320), 52:(600,320), 53:(525,320), 54:(450,320), 55:(375,320), 56:(300,320),
57:(225,320), 58:(150,320), 59:(75,320), 60:(0,320),61: (0, 240), 62: (75, 240), 63: (150, 240), 64: (225, 240), 65: (300, 240),
66: (375, 240), 67: (450, 240), 68: (525, 240), 69: (600, 240), 70: (675, 240), 71: (675, 170), 72: (600, 170), 73: (525, 170), 
74: (450, 170), 75: (375, 170), 76: (300, 170), 77: (225, 170), 78: (150, 170), 79: (75, 170), 80: (0, 170), 81: (0, 100), 
82: (75, 100), 83: (150, 100), 84: (225, 100), 85: (300, 100), 86: (375, 100), 87: (450, 100), 88: (525, 100), 89: (600, 100),
90: (675, 100), 91: (675, 10), 92: (600, 10), 93: (525, 10), 94: (450, 10), 95: (375, 10), 96: (300, 10), 97: (225, 10), 
98: (150, 10), 99: (75, 10), 100: (0, 10)}
ladders={4:25,21:39,29:74,43:76,63:80,71:89}
snakes={30:7,47:15,56:19,73:51,82:42,92:75,98:55}

#Window of instruction button
def instructions_maker():
    instructions_window= Toplevel()
    instructions_window.geometry("860x513")
    instructions_window.title("Snake and ladder game")
    Frame1= Frame(instructions_window,width=400,height=400,relief="raised")
    Frame1.place(x=0,y=0)
    instructions_image= PhotoImage(file="instructions.png")
    label= Label(Frame1,image=instructions_image)
    label.place(x=0,y=0)
    label.pack()
    instructions_window.mainloop()
#function to show pop up message to ask the user to exit or not
def exit_quest(e):
        ans=mbox.askyesno("EXIT" ,"Do you want to exit the game?")
        if ans:
                e.destroy()
#window to choose the playing mode
def decision_maker():
    welcome_window.withdraw()
    global decision_window
    #initialize the decision_window 
    decision_window= Toplevel()
    decision_window.geometry("600x400")
    decision_window.title("Snake and ladder game")
    #frame for background image 
    Frame1= Frame(decision_window,width=400,height=400,relief="raised")
    Frame1.place(x=0,y=0)
    #import the background image 
    decision_image= PhotoImage(file="background.png")
    label1= Label(Frame1,image=decision_image)
    label1.place(x=0,y=0)
    label1.pack()
    #label to ask the user to choose mode 
    decision_label= Label(decision_window, text="Do you want to play in Single Player Mode \n or Multiplayer Mode?",font=("Helvetica",18,"bold"),width=35, fg="#ffffff", bg="#3cb043").place(x=50,y=50)
    #buttons to choose mode
    oneplayer_button=Button(decision_window, text= "Single Player Mode",padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=computer_and_player_window, fg="#FFFFFF", bg="#1699EE").place(x=30,y=200)
    twoplayers_button=Button(decision_window, text= "Multiplayer Mode",padx=40 ,pady=20,font=("Helvetica",12,"bold"),command =player_vs_player_window,fg="#FFFFFF", bg="#EE168F").place(x=350,y=200)
    decision_window.mainloop()
def decision_maker_saved():
    welcome_window.withdraw()
    #initialize the decision_window 
    global decision1_window
    decision1_window= Toplevel()
    decision1_window.geometry("600x400")
    decision1_window.title("Snake and ladder game")
    #frame for background image 
    Frame1= Frame(decision1_window,width=400,height=400,relief="raised")
    Frame1.place(x=0,y=0)
    #import the background image 
    decision1_image= PhotoImage(file="background.png")
    label1= Label(Frame1,image=decision1_image)
    label1.place(x=0,y=0)
    label1.pack()
    #label to ask the user to choose mode 
    decision_label= Label(decision1_window, text="Was your game in Single Player Mode \n or Multiplayer Mode?",font=("Helvetica",18,"bold"),width=35, fg="#ffffff", bg="#3cb043").place(x=50,y=50)
    #buttons to choose mode
    oneplayer_button=Button(decision1_window, text= "Single Player Mode",padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=saved_games_singleplayer, fg="#FFFFFF", bg="#1699EE").place(x=30,y=200)
    twoplayers_button=Button(decision1_window, text= "Multiplayer Mode",padx=40 ,pady=20,font=("Helvetica",12,"bold"),command = saved_games_multiplayer,fg="#FFFFFF", bg="#EE168F").place(x=350,y=200)
    decision1_window.mainloop()

#multiplayer mode 
def player_vs_player_window():
#Splash window (the entry window)
        def entry_players_window():
                decision_window.withdraw()
                #Initialize the splash entry window
                Splash_window = Tk()
                Splash_window.geometry("400x400")
                Splash_window.config(bg="#fbb0a9")
                Splash_window.title("Snake and ladder game")
                def ok_button_click():
                                #Get user input from entries
                                player1_name = entry1.get()
                                player2_name = entry2.get()
                                #Destroying window after taking info
                                if player1_name == "":
                                        player1_name= "player1"
                                if player2_name=="":
                                        player2_name='player2'
                                Splash_window.destroy()
                                welcome_window.destroy()
                                #Open the new window with user names
                                main_window(player1_name, player2_name)
                #Create entry widgets for user names
                entry1 = Entry(Splash_window, borderwidth=5,width=50, fg="black", bg="#ffffff")
                entry1.place(x=50,y=150)
                entry2 = Entry(Splash_window, borderwidth=5,width=50, fg="black", bg="#ffffff")
                entry2.place(x=50,y=250) 
                #Create labels for user input
                mylabel1 = Label(Splash_window, text="Player 1 please enter your name:",font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=70,y=100)
                mylabel2 = Label(Splash_window, text="Player 2 please enter your name:",font=("Helvetica",12,"bold"),fg="#1188A3", bg="#89E0E7").place(x=70,y=200)
                #Create OK button with command to call separate function
                okbutton = Button(Splash_window, text="OK",padx=70 ,pady=10, font=("Helvetica",12,"bold"), command=ok_button_click,fg="#fbb0a9", bg="#ffffff").place(x=120,y=300) 
                #Start the main window's main loop
                Splash_window.mainloop()

        #Board window ( the main window)
        def main_window(player1_name, player2_name):
                #initialize the board window
                global board_window
                board_window = Tk()
                board_window.geometry("1200x723")
                board_window.title("Snake and Ladder Game")
                board_window.config(bg="#fbb0a9")
                board_window.configure()
                #frame for photo
                Frame1= Frame(board_window, width=1200,height=723,relief="raised")
                Frame1.place(x=0,y=0)
                #board image import
                board_image= PhotoImage(file="board.png")
                label1= Label(Frame1,image=board_image)
                label1.place(x=0,y=0)
                label1.pack()
                #coins making
                player_1=Canvas(board_window,width=40,height=40)
                player_1.create_oval(10,10,40,40,fill="#B5338A")
                player_1.place(x=0,y=720)
                player_2=Canvas(board_window,width=40,height=40)
                player_2.create_oval(10,10,40,40,fill="#89E0E7")
                player_2.place(x=0,y=720)
                board_window.bind('<Escape>',lambda e:exit_quest(board_window))       

                #label for different messages during game
                
                message_label= Label(board_window, text="",font=("Helvetica",18,"bold"),width=20, bg="#fbb0a9").place(x=800,y=400)

                turn_label= Label(board_window, text=f"{player1_name}'s Turn",font=("Helvetica",18,"bold"),width=12,fg="#F0A3F1" ,bg="#B5338A").place(x=860,y=350)
                #Create buttons with user names
                def switch_player():
                        global current_player
                        current_player= not current_player
                        change_button_state()
                #function to disable button of the second player when its first player's turn
                def change_button_state():
                        button_player1 = Button(board_window,state=NORMAL if current_player else DISABLED, text=player1_name,command=lambda:[roll_dice(),move_player1(player1_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=500)
                        button_player2 = Button(board_window,state=NORMAL if not current_player else DISABLED, text=player2_name,command=lambda:[roll_dice(),move_player1(player2_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#1188A3", bg="#89E0E7").place(x=895,y=590)
                        if current_player== True:
                                turn_label= Label(board_window, text=f"{player1_name}'s Turn",font=("Helvetica",18,"bold"),width=12, fg="#F0A3F1", bg="#B5338A").place(x=860,y=350)
                        else:
                                turn_label= Label(board_window, text=f"{player2_name}'s Turn",font=("Helvetica",18,"bold"),width=12, fg="#1188A3", bg="#89E0E7").place(x=860,y=350)
                #buttons with players'names to call functions
                button_player1 = Button(board_window, text=player1_name,command=lambda:[roll_dice(),move_player1(player1_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=500)
                button_player2 = Button(board_window, text=player2_name,command=lambda:[roll_dice(),move_player1(player2_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#1188A3", bg="#89E0E7").place(x=895,y=590)
                save_button=Button(board_window, text="SAVE",command=lambda:[save_multiplayer(player1_name,player2_name,player1_pos,player2_pos),board_window.destroy()],padx=40 ,pady=10, font=("Helvetica",12,"bold"), fg="#fbb0a9", bg="#ffffff").place(x=1050,y=10)
                change_button_state()
                #getting the universal dice image and putting diffent conditions

                def get_number(x):
                        if x == '\u2680':
                                return(1)
                        elif x == '\u2681':
                                        return(2)
                        elif x == '\u2682':
                                        return(3)
                        elif x == '\u2683':
                                        return(4)
                        elif x == '\u2684':
                                        return(5)
                        elif x == '\u2685':
                                        return(6)
                #what happens when we roll the dice
                def roll_dice():
                        global dice
                        dice = random.choice(my_dice)    
                        numdice = get_number(dice)
                        dice_label.config(text=dice)
                        total = numdice
                        total_label.config(text=f"You Rolled: {total}!")
                        return total

                #moving player one 
                def move_player1(player_name):
                        global player1_pos
                        global player2_pos
                        global message_label
                        if player_name==player1_name:
                                counter1=get_number(dice)
                                if player1_pos+counter1 <=100:
                                        player1_pos += counter1
                                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                #if it lands on a ladder the coin will go up to the right position
                                        if player1_pos in ladders:
                                                player1_pos=ladders[player1_pos]
                                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                                message_label= Label(board_window, text=f"Congartulations {player_name}! \n You got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                #if it lands on a snakes the coin will go down to the right position
                                        elif player1_pos in snakes:
                                                player1_pos=snakes[player1_pos]
                                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                                message_label= Label(board_window, text=f"Bad Luck {player_name}\n It's A Snake :(",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                #if it lands on a normal box 
                                        elif player1_pos not in snakes or ladders:
                                                message_label= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=400)     

                        if player_name==player2_name:
                                counter2=get_number(dice)
                                if player2_pos+counter2<=100:
                                        player2_pos += counter2
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                #if it lands on a ladder the coin will go up to the right position
                                if player2_pos in ladders:
                                        player2_pos=ladders[player2_pos]
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        message_label= Label(board_window, text=f"Congartulations {player2_name}! \n You got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                #if it lands on a snakes the coin will go down to the right position
                                elif player2_pos in snakes:
                                        player2_pos=snakes[player2_pos]
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        message_label= Label(board_window, text=f"Bad Luck {player2_name}\n It's A Snake :(",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                
                                elif player2_pos not in snakes or ladders:
                                        message_label= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=400)       
                        #knock out player 2 if player 1 is on same position
                        if player1_pos==player2_pos:
                                player2_pos=1
                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                        #knock out player 1 if player 2 is on same position
                        if player2_pos==player1_pos:
                                player1_pos=1
                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                        #show menu window when player 1 wins
                        if player1_pos==100:
                                options_window(player1_name)
                        #show menu window when player 2 wins
                        if player2_pos==100:
                                options_window(player2_name) 
                #function to start new game when replay button is clicked
                def start_new_game():
                        menu_window.withdraw()
                        global player1_pos
                        global player2_pos
                        player1_pos=0
                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                        player2_pos=0
                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                #function to exit game when exit button is clicked
                def exit():
                        menu_window.destroy()
                        board_window.destroy()
                #window shown when a player wins
                def options_window(player_name):
                        # initialize menu_window
                        global menu_window
                        menu_window=Toplevel()
                        menu_window.geometry("600x400")
                        menu_window.title("Snake and ladder game")
                        #frame for photo
                        Frame1= Frame(menu_window,width=400,height=400,relief="raised")
                        Frame1.place(x=0,y=0)
                        #import background image 
                        menu_image= PhotoImage(file="background.png")
                        label1= Label(Frame1,image=menu_image)
                        label1.place(x=0,y=0)
                        label1.pack()
                        #label to show winner
                        label_menu=Label(menu_window,text=f'{player_name} won this game',font=("Helvetica",22,"bold"),width=27, fg="#ffffff", bg="#3cb043").place(x=50,y=100)
                        #show the two buttons that call functions
                        replay_button=Button(menu_window,text='Replay',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=start_new_game,fg="#FFFFFF", bg="#1699EE").place(x=390,y=200)
                        exit_button=Button(menu_window,text='Exit',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=exit , fg="#FFFFFF", bg="#ff0000").place(x=50,y=200)
                        options_window.mainloop()
                my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]
                frame3 = Frame(board_window,width=145,height=145,relief="sunken")
                frame3.place(x=875, y=40)
                        
                #dice
                dice_label = Label(frame3, text='', font=("Helvetica",150), fg="#ffffff",bg="#fbb0a9")
                dice_label.grid(row=0, column=0)



                total_label = Label(board_window, text="",font=("Helvetica", 20,"bold"),fg="#FFFFFF", bg="#fbb0a9")
                total_label.place(x=860,y=250)
                roll_dice()
                board_window.mainloop()
        entry_players_window()
#the oneplayer mode
def computer_and_player_window():
        def entry_players_window():
                decision_window.withdraw()
                #Initialize the splash entry window
                Splash_window = Tk()
                Splash_window.geometry("400x300")
                Splash_window.config(bg="#fbb0a9")
                Splash_window.title("Snake and ladder game")
                def ok_button_click():
                                #Get user input from entries
                                player1_name = entry1.get()
                                #Destroying window after taking info
                                Splash_window.destroy()
                                welcome_window.destroy()
                                #Open the new window with user names
                                main_window(player1_name)
                #Create entry widgets for user names
                entry1 = Entry(Splash_window, borderwidth=5,width=50, fg="black", bg="#ffffff")
                entry1.place(x=50,y=150)
                #Create labels for user input
                mylabel1 = Label(Splash_window, text="Please enter your name:",font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=100,y=100)
                okbutton = Button(Splash_window, text="OK",padx=70 ,pady=10, font=("Helvetica",12,"bold"), command=ok_button_click,fg="#fbb0a9", bg="#ffffff").place(x=120,y=200) 
                #Start the main window's main loop
                Splash_window.mainloop()

        #Board window ( the main window)
        def main_window(player1_name):
                #initialize board window 
                board_window = Tk()
                board_window.geometry("1200x723")
                board_window.title("Snake and Ladder Game")
                board_window.config(bg="#fbb0a9")
                board_window.configure()
                #frame for photo
                Frame1= Frame(board_window, width=1200,height=723,relief="raised")
                Frame1.place(x=0,y=0)
                #board image import
                board_image= PhotoImage(file="board.png")
                label1= Label(Frame1,image=board_image)
                label1.place(x=0,y=0)
                label1.pack()
                #coins making
                player_1=Canvas(board_window,width=40,height=40)
                player_1.create_oval(10,10,40,40,fill="#B5338A")
                player_1.place(x=0,y=720)
                player_2=Canvas(board_window,width=40,height=40)
                player_2.create_oval(10,10,40,40,fill="#89E0E7")
                player_2.place(x=0,y=720)
                board_window.bind('<Escape>',lambda e:exit_quest(board_window))

                #label for diffent messages during game
                message_label= Label(board_window, text="",font=("Helvetica",18,"bold"),width=20, bg="#fbb0a9").place(x=800,y=450)
                message_label_computer= Label(board_window, text="",font=("Helvetica",18,"bold"),width=20, bg="#fbb0a9").place(x=800,y=370)
                #Create buttons with user names
                def enable_button():
                         button_player1 = Button(board_window,state=NORMAL, text=player1_name,command=lambda:[roll_dice_and_move()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=570)
                def roll_dice_and_move():
                        global current_player
                
                        button_player1 = Button(board_window,state=DISABLED, text=player1_name,command=lambda:[roll_dice_and_move()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=570)
                        roll_dice()
                        if current_player:
                                move_player1()
                                board_window.after(1000,lambda:[computer_play(),enable_button()])  # Delay for 2 seconds before computer's turn
                        else:
                                computer_play()
                button_player1 = Button(board_window, text=player1_name,command=lambda:[roll_dice_and_move()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=570)
                save_button=Button(board_window, text="SAVE",command=lambda:[save_singleplayer(player1_name,'Computer',player1_pos,player2_pos),board_window.destroy()],padx=40 ,pady=10, font=("Helvetica",12,"bold"), fg="#fbb0a9", bg="#ffffff").place(x=1050,y=10)
                #getting the universal dice image and putting diffent conditions
                def get_number(x):
                        if x == '\u2680':
                                return(1)
                        elif x == '\u2681':
                                        return(2)
                        elif x == '\u2682':
                                        return(3)
                        elif x == '\u2683':
                                        return(4)
                        elif x == '\u2684':
                                        return(5)
                        elif x == '\u2685':
                                        return(6)
                #what happens when we roll the dice
                def roll_dice():
                        global dice
                        dice = random.choice(my_dice)    
                        numdice = get_number(dice)
                        dice_label.config(text=dice)
                        total = numdice
                        total_label.config(text=f"You Rolled: {total}!")
                        return total
                def roll_dice_computer():
                        global dice
                        dice = random.choice(my_dice)    
                        numdice = get_number(dice)
                        dice_label.config(text=dice)
                        total = numdice
                        total_label_computer.config(text=f"The computer Rolled: {total}")
                        return total

                #moving player one
                def move_player1():
                        global player1_pos
                        global player2_pos
                        global message_label
                        counter1=get_number(dice)
                        if player1_pos+counter1 <=100:
                                player1_pos += counter1
                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                #if coins lands on a ladder it will move up to the right position
                                if player1_pos in ladders:
                                        player1_pos=ladders[player1_pos]
                                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                        message_label= Label(board_window, text=f"Congartulations {player1_name}! \n You got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=450)
                                #if coin lands on a snake it will move down to the right position        
                                elif player1_pos in snakes:
                                        player1_pos=snakes[player1_pos]
                                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                        message_label= Label(board_window, text=f"Bad Luck {player1_name}\n It's A Snake :(",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=450)
                                
                                elif player1_pos not in snakes or ladders:
                                        message_label= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=450)       
                        #knock out player 2(computer) if player 1 is on same position
                        if player1_pos==player2_pos:
                                player2_pos=1
                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                        #show menu window when a player wins
                        if player1_pos==100:
                                options_window(player1_name)
                #function to make the computer play with the user
                def computer_play():
                        roll_dice_computer()
                        global computer_turn
                        global player2_pos
                        global player1_pos
                        global message_label
                        player2_name='Computer'
                        counter2=get_number(dice)
                        if player2_pos+counter2<=100:
                                player2_pos+= counter2
                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                #if coin lands on a ladder it will go up to the right position 
                                if player2_pos in ladders:
                                        player2_pos=ladders[player2_pos]
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        message_label_computer= Label(board_window, text=f"The computer got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=370)
                                elif player2_pos in snakes:
                                        player2_pos=snakes[player2_pos]
                                        message_label_computer= Label(board_window, text=f"The computer got a Snake ",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=370)
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                elif player1_pos not in snakes or ladders:
                                        message_label_computer= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=370)       
                        #knock out player 1 if player 2(computer) is on same position
                        if player2_pos==player1_pos:
                                player1_pos=1
                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                        #show menu window when player2 (computer) wins
                        if player2_pos==100:
                                options_window(player2_name)   
                #function to start new game when replay button is clicked         
                def start_new_game():
                        menu_window.withdraw()
                        global player1_pos
                        global player2_pos
                        player1_pos=0
                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                        player2_pos=0
                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                        enable_button()
                #function to exit game when exit button is clicked
                def exit():
                        menu_window.destroy()
                        board_window.destroy()
                #window shown when a player wins
                def options_window(player_name):
                        global menu_window
                        menu_window=Toplevel()
                        menu_window.geometry("600x400")
                        menu_window.title("Snake and ladder game")
                        #frame to show background image
                        Frame1= Frame(menu_window,width=400,height=400,relief="raised")
                        Frame1.place(x=0,y=0)
                        #import background image
                        menu_image= PhotoImage(file="background.png")
                        label1= Label(Frame1,image=menu_image)
                        label1.place(x=0,y=0)
                        label1.pack()
                        #label to show the winner
                        label_menu=Label(menu_window,text=f'{player_name} won this game',font=("Helvetica",22,"bold"),width=27, fg="#ffffff", bg="#3cb043").place(x=50,y=100)
                        #buttons to call functions
                        replay_button=Button(menu_window,text='Replay',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=start_new_game,fg="#FFFFFF", bg="#1699EE").place(x=390,y=200)
                        exit_button=Button(menu_window,text='Exit',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=exit , fg="#FFFFFF", bg="#ff0000").place(x=50,y=200)
                        options_window.mainloop()
                my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]
                frame3 = Frame(board_window,width=145,height=145,relief="sunken")
                frame3.place(x=875, y=40)
                #dice
                dice_label = Label(frame3, text='', font=("Helvetica",150), fg="#ffffff",bg="#fbb0a9")
                dice_label.grid(row=0, column=0)

                total_label = Label(board_window, text="",font=("Helvetica", 20,"bold"),fg="#FFFFFF", bg="#fbb0a9")
                total_label.place(x=860,y=250)
                total_label_computer = Label(board_window, text="",font=("Helvetica", 20,"bold"),fg="#FFFFFF", bg="#fbb0a9")
                total_label_computer.place(x=800,y=300)
                roll_dice()
                board_window.mainloop()
        entry_players_window() 

 
#function to save file with two players names
def save_multiplayer(x,y,z,f):
        name1_file=open(f'{x} and {y}.txt','w')
        name1_file.write(f"{str(z)},{x},{str(f)},{y}")
        name_file=open('multiplayers.txt','a')
        name_file.write(x + ' and ' + y + '\n')
        name_file.close()
        name1_file.close()

#function to save file with one player name
def save_singleplayer(x,y,z,f):
        name2_file=open(f'{x}.txt','w')
        name2_file.write(f"{str(z)},{x},{str(f)},{y}")
        name_file=open('singleplayers.txt','a')
        name_file.write(x + '\n')
        name2_file.close()
def allplayers_names():
        global players
        global playerssingle
        name_file=open('multiplayers.txt', 'r')
        players=[]
        for i in name_file:              
                        players.append(i)
        name_filesingle=open('singleplayers.txt', 'r')
        playerssingle=[]
        for i in name_filesingle:              
                playerssingle.append(i)    
allplayers_names()   
#function to search saved game in multiplayer mode
def saved_games_multiplayer():
        decision1_window.withdraw()
        
        def play_saved():
  
                global player1_pos
                global player2_pos
                player_file=clicked.get()
                new=player_file.rstrip("\n")
                saved_file=open(f"{new}.txt","r")
                line = saved_file.readline()
                my_list=re.split(",", line)
                my_list = [item.strip("''") for item in my_list]
                player1_list= my_list[0:2]
                player2_list=my_list[2:4]
                player1_name=player1_list[1]
                player2_name=player2_list[1]
                player1_pos=int(player1_list[0])
                player2_pos=int(player2_list[0])
                main_window(player1_name,player2_name)
                
        #Board window ( the main window)
        def main_window(player1_name, player2_name):
         
                #initialize the board window
                saved_window.withdraw()
                board_window = Toplevel()
                board_window.geometry("1200x723")
                board_window.title("Snake and Ladder Game")
                board_window.config(bg="#fbb0a9")
                board_window.configure()
                #frame for photo
                Frame1= Frame(board_window, width=1200,height=723,relief="raised")
                Frame1.place(x=0,y=0)
                #board image import
                board_image= PhotoImage(file="board.png")
                label1= Label(Frame1,image=board_image)
                label1.place(x=0,y=0)
                label1.pack()
                #coins making
                player_1=Canvas(board_window,width=40,height=40)
                player_1.create_oval(10,10,40,40,fill="#B5338A")
                player_1.place(x=0,y=720)
                player_2=Canvas(board_window,width=40,height=40)
                player_2.create_oval(10,10,40,40,fill="#89E0E7")
                player_2.place(x=0,y=720)
                board_window.bind('<Escape>',lambda e:exit_quest(board_window))       

                #label for different messages during game
                
                message_label= Label(board_window, text="",font=("Helvetica",18,"bold"),width=20, bg="#fbb0a9").place(x=800,y=400)

                turn_label= Label(board_window, text=f"{player1_name}'s Turn",font=("Helvetica",18,"bold"),width=12,fg="#F0A3F1" ,bg="#B5338A").place(x=860,y=350)
                #Create buttons with user names
                def switch_player():
                        global current_player
                        current_player= not current_player
                        change_button_state()
                #function to disable button of the second player when its first player's turn
                def change_button_state():
                        button_player1 = Button(board_window,state=NORMAL if current_player else DISABLED, text=player1_name,command=lambda:[roll_dice(),move_player1(player1_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=500)
                        button_player2 = Button(board_window,state=NORMAL if not current_player else DISABLED, text=player2_name,command=lambda:[roll_dice(),move_player1(player2_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#1188A3", bg="#89E0E7").place(x=895,y=590)
                        if current_player== True:
                                turn_label= Label(board_window, text=f"{player1_name}'s Turn",font=("Helvetica",18,"bold"),width=12, fg="#F0A3F1", bg="#B5338A").place(x=860,y=350)
                        else:
                                turn_label= Label(board_window, text=f"{player2_name}'s Turn",font=("Helvetica",18,"bold"),width=12, fg="#1188A3", bg="#89E0E7").place(x=860,y=350)
                #buttons with players'names to call functions
                button_player1 = Button(board_window, text=player1_name,command=lambda:[roll_dice(),move_player1(player1_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=500)
                button_player2 = Button(board_window, text=player2_name,command=lambda:[roll_dice(),move_player1(player2_name),switch_player()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#1188A3", bg="#89E0E7").place(x=895,y=590)
                save_button=Button(board_window, text="SAVE",command=lambda:[save_multiplayer(player1_name,player2_name,player1_pos,player2_pos),board_window.withdraw()],padx=40 ,pady=10, font=("Helvetica",12,"bold"), fg="#fbb0a9", bg="#ffffff").place(x=1050,y=10)
                #getting the universal dice image and putting diffent conditions

                def get_number(x):
                        if x == '\u2680':
                                return(1)
                        elif x == '\u2681':
                                        return(2)
                        elif x == '\u2682':
                                        return(3)
                        elif x == '\u2683':
                                        return(4)
                        elif x == '\u2684':
                                        return(5)
                        elif x == '\u2685':
                                        return(6)
                #what happens when we roll the dice
                def roll_dice():
                        global dice
                        dice = random.choice(my_dice)    
                        numdice = get_number(dice)
                        dice_label.config(text=dice)
                        total = numdice
                        total_label.config(text=f"You Rolled: {total}!")
                        return total

                #moving player one 
                def move_player1(player_name):
                        global player1_pos
                        global player2_pos
                        global message_label
                        if player_name==player1_name:
                                counter1=get_number(dice)
                                if player1_pos+counter1 <=100:
                                        player1_pos += counter1
                                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                #if it lands on a ladder the coin will go up to the right position
                                        if player1_pos in ladders:
                                                player1_pos=ladders[player1_pos]
                                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                                message_label= Label(board_window, text=f"Congartulations {player_name}! \n You got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                #if it lands on a snakes the coin will go down to the right position
                                        elif player1_pos in snakes:
                                                player1_pos=snakes[player1_pos]
                                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                                message_label= Label(board_window, text=f"Bad Luck {player_name}\n It's A Snake :(",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                #if it lands on a normal box 
                                        elif player1_pos not in snakes or ladders:
                                                message_label= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=400)     

                        if player_name==player2_name:
                                counter2=get_number(dice)
                                if player2_pos+counter2<=100:
                                        player2_pos += counter2
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                #if it lands on a ladder the coin will go up to the right position
                                if player2_pos in ladders:
                                        player2_pos=ladders[player2_pos]
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        message_label= Label(board_window, text=f"Congartulations {player2_name}! \n You got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                #if it lands on a snakes the coin will go down to the right position
                                elif player2_pos in snakes:
                                        player2_pos=snakes[player2_pos]
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        message_label= Label(board_window, text=f"Bad Luck {player2_name}\n It's A Snake :(",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=400)
                                
                                elif player2_pos not in snakes or ladders:
                                        message_label= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=400)       
                        #knock out player 2 if player 1 is on same position
                        if player1_pos==player2_pos:
                                player2_pos=1
                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                        #knock out player 1 if player 2 is on same position
                        if player2_pos==player1_pos:
                                player1_pos=1
                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                        #show menu window when player 1 wins
                        if player1_pos==100:
                                options_window(player1_name)
                        #show menu window when player 2 wins
                        if player2_pos==100:
                                options_window(player2_name) 
                #function to start new game when replay button is clicked
                def start_new_game():
                        menu_window.withdraw()
                        global player1_pos
                        global player2_pos
                        player1_pos=0
                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                        player2_pos=0
                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                #function to exit game when exit button is clicked
                def exit():
                        menu_window.destroy()
                        board_window.destroy()
                #window shown when a player wins
                def options_window(player_name):
                        # initialize menu_window
                        global menu_window
                        menu_window=Toplevel()
                        menu_window.geometry("600x400")
                        menu_window.title("Snake and ladder game")
                        #frame for photo
                        Frame1= Frame(menu_window,width=400,height=400,relief="raised")
                        Frame1.place(x=0,y=0)
                        #import background image 
                        menu_image= PhotoImage(file="background.png")
                        label1= Label(Frame1,image=menu_image)
                        label1.place(x=0,y=0)
                        label1.pack()
                        #label to show winner
                        label_menu=Label(menu_window,text=f'{player_name} won this game',font=("Helvetica",22,"bold"),width=27, fg="#ffffff", bg="#3cb043").place(x=50,y=100)
                        #show the two buttons that call functions
                        replay_button=Button(menu_window,text='Replay',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=start_new_game,fg="#FFFFFF", bg="#1699EE").place(x=390,y=200)
                        exit_button=Button(menu_window,text='Exit',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=exit , fg="#FFFFFF", bg="#ff0000").place(x=50,y=200)
                        options_window.mainloop()
                my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]
                frame3 = Frame(board_window,width=145,height=145,relief="sunken")
                frame3.place(x=875, y=40)
                        
                #dice
                dice_label = Label(frame3, text='', font=("Helvetica",150), fg="#ffffff",bg="#fbb0a9")
                dice_label.grid(row=0, column=0)



                total_label = Label(board_window, text="",font=("Helvetica", 20,"bold"),fg="#FFFFFF", bg="#fbb0a9")
                total_label.place(x=860,y=250)
                roll_dice()
                board_window.mainloop()
        global saved_window
        #initialize saved_window
        saved_window=Toplevel()
        saved_window.geometry("600x400")
        saved_window.title("Snake and ladder game")
        #frame for background image 
        Frame1= Frame(saved_window,width=400,height=400,relief="raised")
        Frame1.place(x=0,y=0)
        #import the background image 
        saved_image= PhotoImage(file="background.png")
        label1= Label(Frame1,image=saved_image)
        label1.place(x=0,y=0)
        label1.pack()
        clicked=StringVar()
        clicked.set(players[0])
        saved_button=OptionMenu(saved_window,clicked,*players)
        saved_button.config(width=20,font=("Helvetica",12,"bold"),bg="#fbb0a9",fg="#ffffff")
        saved_button.place(x=200,y=200)
      

   
        label_saved=Label(saved_window, text="Please choose the game\n you would like to resume",font=("Helvetica",18,"bold"),width=35, fg="#ffffff", bg="#3cb043").place(x=50,y=100)
        button_saved=Button(saved_window,text="Play!",padx=70 ,pady=10, font=("Helvetica",18,"bold"),command=lambda:[play_saved(),welcome_window.withdraw()],fg="#fbb0a9", bg="#ffffff").place(x=210,y=300)
        saved_window.mainloop()
#function to search saved game in singleplayer mode
def saved_games_singleplayer():
        decision1_window.withdraw()
                
        def play_saved():
                global player1_pos
                global player2_pos
                player_file=clicked.get()
                new=player_file.rstrip("\n")
                saved_file=open(f"{new}.txt","r")
                line = saved_file.readline()
                my_list=re.split(",", line)
                my_list = [item.strip("''") for item in my_list]
                player1_list= my_list[0:2]
                player2_list=my_list[2:4]
                player1_name=player1_list[1]
                player2_name=player2_list[1]
                player1_pos=int(player1_list[0])
                player2_pos=int(player2_list[0])
                main_window(player1_name)
        def main_window(player1_name):
                        saved1_window.withdraw()
                        #initialize board window 
                        board_window = Toplevel()
                        board_window.geometry("1200x723")
                        board_window.title("Snake and Ladder Game")
                        board_window.config(bg="#fbb0a9")
                        board_window.configure()
                        #frame for photo
                        Frame1= Frame(board_window, width=1200,height=723,relief="raised")
                        Frame1.place(x=0,y=0)
                        #board image import
                        board_image= PhotoImage(file="board.png")
                        label1= Label(Frame1,image=board_image)
                        label1.place(x=0,y=0)
                        label1.pack()
                        #coins making
                        player_1=Canvas(board_window,width=40,height=40)
                        player_1.create_oval(10,10,40,40,fill="#B5338A")
                        player_1.place(x=0,y=720)
                        player_2=Canvas(board_window,width=40,height=40)
                        player_2.create_oval(10,10,40,40,fill="#89E0E7")
                        player_2.place(x=0,y=720)
                        board_window.bind('<Escape>',lambda e:exit_quest(board_window))

                        #label for diffent messages during game
                        message_label= Label(board_window, text="",font=("Helvetica",18,"bold"),width=20, bg="#fbb0a9").place(x=800,y=450)
                        message_label_computer= Label(board_window, text="",font=("Helvetica",18,"bold"),width=20, bg="#fbb0a9").place(x=800,y=370)
                        #Create buttons with user names
                        def enable_button():
                                button_player1 = Button(board_window,state=NORMAL, text=player1_name,command=lambda:[roll_dice_and_move()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=570)
                        def roll_dice_and_move():
                                global current_player
                        
                                button_player1 = Button(board_window,state=DISABLED, text=player1_name,command=lambda:[roll_dice_and_move()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=570)
                                roll_dice()
                                if current_player:
                                        move_player1()
                                        board_window.after(1000,lambda:[computer_play(),enable_button()])  # Delay for 2 seconds before computer's turn
                                else:
                                        computer_play()
                        button_player1 = Button(board_window, text=player1_name,command=lambda:[roll_dice_and_move()],padx=40 ,pady=20,font=("Helvetica",12,"bold"),fg="#F0A3F1", bg="#B5338A").place(x=895,y=570)
                        save_button=Button(board_window, text="SAVE",command=lambda:[save_singleplayer(player1_name,'Computer',player1_pos,player2_pos),board_window.destroy()],padx=40 ,pady=10, font=("Helvetica",12,"bold"), fg="#fbb0a9", bg="#ffffff").place(x=1050,y=10)
                                #getting the universal dice image and putting diffent conditions
                        def get_number(x):
                                if x == '\u2680':
                                        return(1)
                                elif x == '\u2681':
                                                return(2)
                                elif x == '\u2682':
                                                return(3)
                                elif x == '\u2683':
                                                return(4)
                                elif x == '\u2684':
                                                return(5)
                                elif x == '\u2685':
                                                return(6)
                        #what happens when we roll the dice
                        def roll_dice():
                                global dice
                                dice = random.choice(my_dice)    
                                numdice = get_number(dice)
                                dice_label.config(text=dice)
                                total = numdice
                                total_label.config(text=f"You Rolled: {total}!")
                                return total
                        def roll_dice_computer():
                                global dice
                                dice = random.choice(my_dice)    
                                numdice = get_number(dice)
                                dice_label.config(text=dice)
                                total = numdice
                                total_label_computer.config(text=f"The computer Rolled: {total}")
                                return total

                        #moving player one
                        def move_player1():
                                global player1_pos
                                global player2_pos
                                global message_label
                                counter1=get_number(dice)
                                if player1_pos+counter1 <=100:
                                        player1_pos += counter1
                                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                        #if coins lands on a ladder it will move up to the right position
                                        if player1_pos in ladders:
                                                player1_pos=ladders[player1_pos]
                                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                                message_label= Label(board_window, text=f"Congartulations {player1_name}! \n You got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=450)
                                        #if coin lands on a snake it will move down to the right position        
                                        elif player1_pos in snakes:
                                                player1_pos=snakes[player1_pos]
                                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                                message_label= Label(board_window, text=f"Bad Luck {player1_name}\n It's A Snake :(",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=450)
                                        
                                        elif player1_pos not in snakes or ladders:
                                                message_label= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=450)       
                                #knock out player 2(computer) if player 1 is on same position
                                if player1_pos==player2_pos:
                                        player2_pos=1
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                #show menu window when a player wins
                                if player1_pos==100:
                                        options_window(player1_name)
                        #function to make the computer play with the user
                        def computer_play():
                                roll_dice_computer()
                                global computer_turn
                                global player2_pos
                                global player1_pos
                                global message_label
                                player2_name='Computer'
                                counter2=get_number(dice)
                                if player2_pos+counter2<=100:
                                        player2_pos+= counter2
                                        player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        #if coin lands on a ladder it will go up to the right position 
                                        if player2_pos in ladders:
                                                player2_pos=ladders[player2_pos]
                                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                                message_label_computer= Label(board_window, text=f"The computer got a ladder",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=370)
                                        elif player2_pos in snakes:
                                                player2_pos=snakes[player2_pos]
                                                message_label_computer= Label(board_window, text=f"The computer got a Snake ",font=("Helvetica",18,"bold"),width=20, fg="#0A5D47", bg="#1FB890").place(x=800,y=370)
                                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                        elif player1_pos not in snakes or ladders:
                                                message_label_computer= Label(board_window, text="\n",font=("Helvetica",18,"bold"),width=20, fg="#fbb0a9", bg="#fbb0a9").place(x=800,y=370)       
                                #knock out player 1 if player 2(computer) is on same position
                                if player2_pos==player1_pos:
                                        player1_pos=1
                                        player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                #show menu window when player2 (computer) wins
                                if player2_pos==100:
                                        options_window(player2_name)   
                        #function to start new game when replay button is clicked         
                        def start_new_game():
                                menu_window.withdraw()
                                global player1_pos
                                global player2_pos
                                player1_pos=0
                                player_1.place(x=Index[player1_pos][0],y=Index[player1_pos][1])
                                player2_pos=0
                                player_2.place(x=Index[player2_pos][0],y=Index[player2_pos][1])
                                enable_button()
                        #function to exit game when exit button is clicked
                        def exit():
                                menu_window.destroy()
                                board_window.destroy()
                        #window shown when a player wins
                        def options_window(player_name):
                                global menu_window
                                menu_window=Toplevel()
                                menu_window.geometry("600x400")
                                menu_window.title("Snake and ladder game")
                                #frame to show background image
                                Frame1= Frame(menu_window,width=400,height=400,relief="raised")
                                Frame1.place(x=0,y=0)
                                #import background image
                                menu_image= PhotoImage(file="background.png")
                                label1= Label(Frame1,image=menu_image)
                                label1.place(x=0,y=0)
                                label1.pack()
                                #label to show the winner
                                label_menu=Label(menu_window,text=f'{player_name} won this game',font=("Helvetica",22,"bold"),width=27, fg="#ffffff", bg="#3cb043").place(x=50,y=100)
                                #buttons to call functions
                                replay_button=Button(menu_window,text='Replay',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=start_new_game,fg="#FFFFFF", bg="#1699EE").place(x=390,y=200)
                                exit_button=Button(menu_window,text='Exit',padx=40 ,pady=20,font=("Helvetica",12,"bold"),command=exit , fg="#FFFFFF", bg="#ff0000").place(x=50,y=200)
                                options_window.mainloop()
                        my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]
                        frame3 = Frame(board_window,width=145,height=145,relief="sunken")
                        frame3.place(x=875, y=40)
                        #dice
                        dice_label = Label(frame3, text='', font=("Helvetica",150), fg="#ffffff",bg="#fbb0a9")
                        dice_label.grid(row=0, column=0)

                        total_label = Label(board_window, text="",font=("Helvetica", 20,"bold"),fg="#FFFFFF", bg="#fbb0a9")
                        total_label.place(x=860,y=250)
                        total_label_computer = Label(board_window, text="",font=("Helvetica", 20,"bold"),fg="#FFFFFF", bg="#fbb0a9")
                        total_label_computer.place(x=800,y=300)
                        roll_dice()
                        board_window.mainloop()

        global saved1_window
        #initialize saved_window
        saved1_window=Toplevel()
        saved1_window.geometry("600x400")
        saved1_window.title("Snake and ladder game")
        #frame for background image 
        Frame1= Frame(saved1_window,width=400,height=400,relief="raised")
        Frame1.place(x=0,y=0)
        #import the background image 
        saved_image= PhotoImage(file="background.png")
        label1= Label(Frame1,image=saved_image)
        label1.place(x=0,y=0)
        label1.pack()
        clicked=StringVar()
        clicked.set(playerssingle[0])
        saved_button=OptionMenu(saved1_window,clicked,*playerssingle)
        saved_button.config(width=20,font=("Helvetica",12,"bold"),bg="#fbb0a9",fg="#ffffff")
        saved_button.place(x=200,y=200)
        

   
        label_saved=Label(saved1_window, text="Please Choose the game\n you would like to resume",font=("Helvetica",18,"bold"),width=35, fg="#ffffff", bg="#3cb043").place(x=50,y=100)
        button_saved=Button(saved1_window,text="Play!",padx=70 ,pady=10, font=("Helvetica",18,"bold"),command=lambda:[play_saved()],fg="#fbb0a9", bg="#ffffff").place(x=210,y=300)
        saved1_window.mainloop()
     

#The Welcome Window
welcome_window= Tk()
welcome_window.geometry("1200x720")
welcome_window.title("Snake and ladder game")
#frame for welcome image
Frame1= Frame(welcome_window,width=1280,height=720,relief="raised")
Frame1.place(x=0,y=0)
#import welcome image
welcomeimage= PhotoImage(file="welcome.png")
label1= Label(Frame1,image=welcomeimage)
label1.place(x=0,y=0)
label1.pack()
#play button that calls decision_maker function
play_button=Button(welcome_window, text="Play!",padx=70 , pady=25,bg="#3cb043", fg="#ffffff", command= decision_maker )
play_button.place(x=375,y=450)
play_button.config(font=("Helvetica",22,"bold"))
#instructions button to call instructions_maker function
instructions_button=Button(welcome_window, text="Instructions" ,padx=35 ,pady=30,bg="#02ccfe", fg="#ffffff", command= instructions_maker )
instructions_button.pack()
instructions_button.config(font=("Helvetica",18,"bold"))
instructions_button.place(x=675,y=450)
saved_button=Button(welcome_window,text='Saved Games',command=decision_maker_saved,width=10,font=("Helvetica",22,"bold"),padx=35,pady=25,bg="#B5338A", fg="#ffffff").place(x=500,y=600)
welcome_window.mainloop() 
