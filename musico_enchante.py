from playsound import playsound 
import termcolor
# termcolor.cprint('This text is red!','red')

print('''The available songs are:
1. The Climb - Miley Cyrus
2. Silent Night - Sinach
3. O Holy Night - Hillsong Worship
4. It's Beginning To Look Like Christmas - Bing Crosby
5. The Christmas Song - Idina Mendzel
''')
type = input('''How do you want to listen to your songs? loop or single or random \n''')

if ((type == "loop")|(type == "l")|(type == "L")) :
    termcolor.cprint("The Climb by Miley Cyrus",'magenta', 'on_white')
    print('\n')
    playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\theClimb.mp3')
    
    termcolor.cprint("Silent Night by Sinach",'magenta', 'on_white')
    print('\n')
    playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\silentNight.mp3')

    termcolor.cprint("O Holy Night by Hillsong Worship",'magenta', 'on_white')
    print("\n")
    playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\oHolyNight.mp3')
    
    termcolor.cprint("It's Beginning To Look Like Christmas by Bing Crosby",'magenta', 'on_white')
    print("\n")
    playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\christmassy.mp3')

    termcolor.cprint("The Christmas Song by Idina Mendzel",'magenta', 'on_white')
    print("\n")
    playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\lovelyXmas.mp3')
    
elif((type == "single")|(type == "s")|(type == "S")) :
    song = input("Which song is on your mind? \n")
    
    if((song == 'the climb')|(song == 'The Climb')|(song == 'The climb')|(song == 'climb')|(song == 'Climb')|(song == str(1))) :
        termcolor.cprint("The Climb by Miley Cyrus",'magenta', 'on_white')
        print('\n')
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\theClimb.mp3')
        
    elif((song == 'silent night')|(song == 'Silent Night')|(song == 'Silent night')|(song == str(2))) :
        termcolor.cprint("Silent Night by Sinach",'magenta', 'on_white')
        print('\n')
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\silentNight.mp3')
        
    elif((song == 'o holy night')|(song == 'O Holy Night')|(song == 'O holy night')|(song == str(3))) :
        termcolor.cprint("O Holy Night by Hillsong Worship",'magenta', 'on_white')
        print("\n")
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\oHolyNight.mp3')
        
    elif((song == "it's beginning to look like christmas")|(song == "It's Beginning To Look Like Christmas")|(song == 'looks like christmas')|(song == str(4))) :
        termcolor.cprint("It's Beginning To Look Like Christmas by Bing Crosby",'magenta', 'on_white')
        print("\n")
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\christmassy.mp3')
        
    elif((song == 'the christmas song')|(song == 'The Christmas Song')|(song == 'Christmas Song')|(song == 'christmas song')|(song == str(5))) :
        termcolor.cprint("The Christmas Song by Idina Mendzel",'magenta', 'on_white')
        print("\n")
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\lovelyXmas.mp3')
       
    else :
        print("That's not in the list!")

elif((type == "random")|(type == "r")|(type == "R")) :
    import random
    song_number = [1,2,3,4,5]
    surprise = random.choice(song_number)
    if(surprise == 1) :
        termcolor.cprint("The Climb by Miley Cyrus",'magenta', 'on_white')
        print('\n')
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\theClimb.mp3')
        
    if(surprise == 2) :
        termcolor.cprint("Silent Night by Sinach",'magenta', 'on_white')
        print('\n')
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\silentNight.mp3')
        
    if(surprise == 3) :
        termcolor.cprint("O Holy Night by Hillsong Worship",'magenta', 'on_white')
        print("\n")
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\oHolyNight.mp3')
        
    if(surprise == 4) :
        termcolor.cprint("It's Beginning To Look Like Christmas by Bing Crosby",'magenta', 'on_white')
        print("\n") 
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\christmassy.mp3')
         
    if(surprise == 5) :
        termcolor.cprint("The Christmas Song by Idina Mendzel",'magenta', 'on_white')
        print("\n")
        playsound('C:\\Users\\Pooja Maria\\OneDrive\\Desktop\\my music player\\lovelyXmas.mp3')
      