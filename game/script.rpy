# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("jill")
define p = Character("Patrick")

# The game starts here.

label start:

    scene intro room

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    j "Hi WA! This is the half draft!"

    j "This will be the software framework \for my TIP assignment"

    j "Everything happens next is just a \test for the framework..."

    j "...and the content have nothing to do with the assignment."

    j "So forgive me if something non-sense bumps up..."

    scene bg room

    # These display lines of dialogue.

    p "This will be another cold, windy day..."

    p "...with terrible Math 257 exams"

    p "The typhoon is coming, my mind is fading..."

    p "...and I can fell it!"


menu ifgetup:

    "Do I really need to get up?"

    "Yes...":
        
        $ getup = True
        jump corridor   
    
    "Not today!":

        $ getup = False
        jump badend
        

label corridor:

    scene mess corridor

    p "This place is filled with nasty smell \produced by dustbin..."

    p "...dustbin..bin..Now we have a excuteable binary file!"

    p "NOOOOOO!!! FOCUS!!!"

    p "Anyway, about the nasty smell..."


menu ifclean:

    "Do I need to care about all the mess?"

    "Well I can't left it there anyway...":

        $ clean = True
        jump afterclean

    "Damn it, I'm in a bad mood!":

        $ clean = False
        jump notclean


label afterclean:

    "No more nsaty semll..."

    "...You feel better"

    jump goodexam

    
label notclean:

    "Rubbish, you know what I mean?"

    "Will the toxic gas here affect your exam?"

    jump badend


label goodexam:

    scene math exam

    "You didn't suffer from toxic air in the corridor..."

    "...so basically you can handle the questions in your exam."

    jump goodend


label goodend:

    scene good end

    "Patrick passed his exam..."

    "...so he can focus on his project now."

    return


label badend:

    scene bad end

    "You either overslept..."

    "...or were affected by the toxic gas in the corridor."

    "Anyway you failed your exam!"

    "You are fired!..."

    "...In your cozy dreams"

    "Your mind is disintegrating in the center of a typhoon..."

    "...like your pouring tears in the pouring rain..."

    return
