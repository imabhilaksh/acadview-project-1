from termcolor import colored   #coloring text module
from steganography.steganography import Steganography
from spy_details import Spy,spy,friends,ChatMessage
import time
from datetime import datetime

statuslist=["hey there ","Whats up !!! "]

def send_a_message():   #function to send a message
    print "Choose which friend you want to send a message : "
    friendchoice=select_friends()
    print "You have selected " +colored(friends[friendchoice].name,'red')

    input_image=raw_input("Enter the name of input file : ")
    output_image='output2.jpg'
    text=raw_input("Enter the text : ")
    Steganography.encode(input_image,output_image,text)

    new_chat_message=ChatMessage(text,True)
    friends[friendchoice].chats.append(new_chat_message)

    print"Your message is ready to be sent "


def read_a_message():
    sender=select_friends()
    output_image=raw_input("Enter the name of the file : ")
    text=Steganography.decode(output_image)

    new_chat_message=ChatMessage(text,False)
    friends[sender].chats.append(new_chat_message)
    print"Message Saved "


def chat_history():
    read_for=select_friends()
    for chat in friends[read_for].chats:
        if  chat.sent_by_me:
            print "%s %s %s"%(colored(time.strftime("%I:%M:%S"),'blue'),colored('You said : ','red'),chat.message)
        else:
            print '%s %s said : %s' % (colored(time.strftime("%I:%M:%S"),'blue'),colored(friends[read_for].name,'red'), chat.message)



def select_friends():   #select friend function
    item_pos=0
    for friend in friends:
        print colored("%d. "%(item_pos+1)+friend.name,'red')
        item_pos+=1
    friend_choice=int(raw_input("Enter your choice : "))
    friend_choice_pos=friend_choice-1
    return friend_choice_pos
def add_friend():    #function to add a friend
    addfriends = Spy('','',0,0.0)
    addfriends.salutation=raw_input("Enter the salutation : ")
    addfriends.name=raw_input("Enter the friend's name : ")
    addfriends.age=int(raw_input("Enter the age of friend : "))
    addfriends.rating=float(raw_input("Enter the rating : "))
    if len(addfriends.name)>0 and addfriends.age>12 and addfriends.age<50 and addfriends.rating>=spy.rating:
        friends.append(addfriends)
        print"Friend added "
    else:
        print"Unable to add friend "
    return len(friends) #returns number of friends

def addstatus(currentstatus):   #function to add status

    updated_status=None
    if currentstatus!=None:
        print "Your current status is %s" %(currentstatus)
    else:
        print"You have no status "
    default = raw_input("Do you want to select from older (Y/N) ")
    if default.upper()=='N':
        print "Enter your new status \n "
        new_status=raw_input()
        if len(new_status)>0:
            statuslist.append(new_status)
            updated_status=new_status
    elif default.upper()=='Y':
        pos=1
        for message in statuslist:
            print "%d. %s"%(pos,message)
            pos+=1
        message_selection=int(raw_input("Select your status : "))
        if len(statuslist)>=message_selection:
            updated_status=statuslist[message_selection-1]

    if updated_status:
        print"Your status is : "+updated_status
    else:
        print "You dont have any updated status "
    return updated_status

def menu():
    currentstatus=None
    flag=1
    while flag:
        choice = int(raw_input("Enter choice \n 1. Status Update \n 2. Add friend \n 3. Select Friend \n 4. Send a secret message \n 5. Read a secret message \n 6. Read chat history  \n 7. Exit \n"))
        if(choice==1):
            currentstatus=addstatus(currentstatus)
        elif(choice==2):
            friends=add_friend()
            print "You have %d friends "%(friends)
        elif(choice==3):
            friendchoice=select_friends()
            print friendchoice
        elif choice==4:
            send_a_message()
        elif choice==5:
            read_a_message()
        elif choice==6:
            chat_history()
        elif choice==7:
            print"Exiting "
            flag=0
ques="Continue as %s %s (Y/N) "%(spy.salutation,spy.name)
existing=raw_input(ques)
if(existing.upper()=='Y'):
    print "Welcome back %s %s . Your age is %d and rating is %.2f "%(spy.salutation,spy.name,spy.age,spy.rating)
    menu()
elif(existing.upper()=='N'):
    print"Enter the details again \n"
    salutation=raw_input("Enter the salutation : ")
    name=raw_input("Enter spy name : ")
    age=int(raw_input("Enter the spy age : "))
    rating=float(raw_input("Enter the rating of spy : "))
    status=True
    if len(name)>0 and age>12 and age<50:
        print"Welcome %s %s . Your age is %d and rating is %.2f " % (salutation, name, age, rating)
        menu()
    else:
        print "Exiting "