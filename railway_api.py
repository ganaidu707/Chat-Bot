import urllib.request
import json

# make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

railway_api = '94cv0xtk2j'
url = 'https://api.railwayapi.com/v2/'

print('Hi mate!')
print('How can I help you?')
selection = input('Do you wanna know train details: "yes" or "no":) ')

if selection in ('no','No', 'NO', 'nO', 'n0', 'N0', 'noo'):

    # start the conversation
    print("Hi, Ok Let's, Chat!!!!!")  # greeting
    speak.speak("Hi, Ok Let's, Chat")

    # keep going the conversation
    print('Whats your name?')  # ask
    speak.speak('Whats your name?')
    Name = input()  # save answer
    print('Im glad to meet you, ' + Name + '!!')  # reply
    speak.speak('Im glad to meet you, ' + Name + '!!')
    print('The number of letters of your name is:' + str(len(Name)))
    speak.speak('The number of letters of your name is: ' + str(len(Name)))

    print('How old are you?')  # ask
    speak.speak('How old are you?')
    Reply = input()  # save answer
    print('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')  # reply
    speak.speak('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')

    print('By the way, are you enjoying this conversation?')  # ask
    speak.speak('By the way, are you enjoying this conversation?')
    Reply = input()  # save answer
    if Reply in ('Yes', 'yes', 'yeah', 'of course','always'):
        print('Oh nice, me too '+ Name + '!!')  # reply
        speak.speak('Oh nice, me too' + Name + '!!')
        print('Can you lend me your new car?')  # ask
        speak.speak('Can you lend me your new car?')
        Reply = input()  # save answer
        if Reply in ('Yes', 'yes', 'yeah', 'of course', 'always'):
            print('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye ' + Name)  # reply
            speak.speak('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye' + Name)
        else:
            print("Okay, no problem I will take public transportation")
            speak.speak('Okay, no problem I will take public transportation')
        exit()
    else:
        print('Oh, its ok, I can fully help in checking trains')
        exit()

if selection in ('yes', 'yeah', 'Yes', 'Yeah', 'YES', 'YEAH'):
    choice = input('Please Enter What you want check "train_status" or "seat_availability": ')
    train_numebr = input("Please Enter Train Number: ")
    date = input("Please Enter Date of Journey in the format DD-MM-YYYY: ")

#train_live_status
if choice == "train_status":
    def train_status(train_number, date):
        status_url = url+"live/train/"+str(train_number)+"/date/"+str(date)+"/apikey/"+railway_api
        json_status = urllib.request.urlopen(status_url)
        status_data = json.load(json_status)
        for status_item in status_data['route']:
            print("station: " + str(status_item['station']), "Schedule Departure: " + str(status_item['schdep']),
                  "Actaul Departure: " + str(status_item['actdep']),"Actaul Arrival: " + str(status_item['actarr']),
                  "Train late by " + str(status_item['latemin']))
    train_status(train_numebr, date)

#train_seat_availability
if choice == "seat_availability":
    Class = input("Please Enter Class: ")
    def seat_availability(train_number, date, Class):
        seat_url = url+"check-seat/train/"+str(train_number)+"/source/BPL/dest/NDLS/date/"+str(date)+"/pref/"+Class+"/quota/GN/apikey/"+railway_api
        json_seat = urllib.request.urlopen(seat_url)
        seat_data = json.load(json_seat)
        for seat_item in seat_data['availability']:
            print("on date: " + seat_item['date'], seat_item['status'])
    seat_availability(train_numebr, date, Class)




