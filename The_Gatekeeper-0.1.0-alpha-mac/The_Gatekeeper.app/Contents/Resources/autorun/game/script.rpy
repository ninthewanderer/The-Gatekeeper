# The script of the game goes in this file.
  
# System which determines the ending you receive.
label friendPoints:
    default friendPoints = 0


# The game starts here.
label start:
    scene background
    with fade 

    show inase default at truecenter
    Inase "..."

    show inase talking
    Inase "Meow!"

    show inase nervous
    Inase "Sorry, that was an accident... I got a little too excited."

    show inase frustrated
    Inase "Anyway..."


label nameSelection:
    show inase talking
    Inase "What's your name?"
    show inase default

    $ name = renpy.input("Please enter your name.")
    $ name = name.strip()

    show inase talking
    Inase "%(name)s? That's what you said, right?"
    show inase default
    
    menu pickName:
        "Yes":
            show inase talking
            Inase "Okay, cool."
            Inase "Nice to meet you, %(name)s! I'm Inase."
            $ friendPoints = friendPoints + 1
            show inase default
            "By the way, Inase will remember that. Your actions will all have consequences."

        "No":
            $ name = renpy.input("Please enter your name.")
            $ name = name.strip()
            show inase nervous
            Inase "Oh. Sorry, %(name)s. I must've misheard."
            $ friendPoints = friendPoints - 1
            show inase default
            "By the way, Inase will remember that. Your actions will all have consequences."


label firstChoice:
    show inase talking
    Inase "So, you're probably wondering how you got here, right?"
    Inase "To put it simply, this is a place where similar souls can meet."
    
    show inase frustrated
    Inase "I know that probably sounds weird, but that's the most accurate description I can give you."

    show inase talking
    Inase "If you'd like, I can take you back to the real world."
    
    menu choice1:
        "Actually, I want to stay for a bit.":
            show inase talking
            Inase "Oh, I didn't expect that... Usually people want to leave immediately."
            Inase "Don't take this the wrong way, but that makes me a little happy."
            show inase nervous
            Inase "It gets a little lonely here sometimes."
            $ friendPoints = friendPoints + 1

        "I can figure it out myself.":
            show inase annoyed
            Inase "Um, okay then."
            show inase frustrated
            Inase "I'd let you learn a lesson and get lost, but unfortunately, it's my job to guide you."
            show inase annoyed
            Inase "I'm the gatekeeper of this place, so I'm going to take you to the exit anyway."
            $ friendPoints = friendPoints - 1

    scene black
    with fade


label secondChoice:
    "Some time later."

    scene background
    with fade

    show inase talking
    Inase "Whew, what a long walk. Let's take a break for a bit."

    menu choice2:
        "Okay, sure.":
            Inase "Thanks, my legs hurt from the exercise."
            show inase frustrated
            Inase "I can't remember the last time I left my room..."
            $ friendPoints = friendPoints + 1

        "I'm fine. Let's keep going.":
            show inase annoyed
            Inase "You might be fine, but I need to rest."
            show inase frustrated
            Inase "I won't take long. I know you want to leave."
            $ friendPoints = friendPoints - 1

    scene black
    with fade


label endings:
    scene background
    with fade

    if(friendPoints >= 1):
        show inase nervous
        Inase "Well, I guess this is it... Bye, %(name)s. This was actually fun."
        show inase talking
        Inase "Come back sometime, okay? It's boring here when I'm by myself."    
    elif(friendPoints <= 0):
        show inase frustrated
        Inase "Okay, this is it. You can leave now and go do your own thing."
        show inase annoyed
        Inase "Good riddance, jerk."


label endGame:
    # This ends the game.
    return