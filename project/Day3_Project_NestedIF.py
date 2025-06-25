print(r'''
                                   ]=I==II==I=[
                                    \\__||__//                 ]=I==II==I=[
               ]=I==II==I=[          |.. ` *|                   \\__||__//
                \\__||__//           |. /\ #|                    |-_ []#|
                 | []   |            |  ## *|                    |      |
                 |    ..|            | . , #|                  ]=I==II==I=[
 ___   ____  ___ |   .. |         __ |..__.*| __                \\__||__//
 ] I---I  I--I [ |..    |        |  ||_|  |_|| |                 |    _*|
 ]_____________[ | .. []|         \--\-|-|--/-//                 |   _ #|
  \_\| |_| |/_/  |_   _ | _   _   _|      ' *|                   |`    *|
   |  .     |'-'-` '-` '-` '-` '-` | []     #|-|--|-_-_-_-_ _ _ _|_'   #|
   |     '  |=-=-=-=-=-=-=-=-=-=-=-|      []*|-----________` ` `   ]   *|
   |  ` ` []|      _-_-_-_-_  '    |-       #|      ,    ' ```````['  _#|
   | '  `  '|   [] | | | | |  []`  |  []    *|   `          . `   |'  I*|
   |      - |    ` | | | | | `     | ;  '   #|     .  |        '  |    #|
  /_'_-_-___-\__,__|_|_|_|_|_______|   `  , *|    _______+___,__,-/._.._.\
''')

print("Welcome to the Land of Dawn Castle")
print("Your mission is to find the right door to capture the traitor in this castle")
choice = input("You are standing in front of a Castle. Where do you want to go? \n Type Door or Above: ").capitalize()

if choice == "Above":
    choice2 = input("You are survived by Baldmon, who is hiding behind the door.\nIn the castle above, there is a loophole."
                    "Type WAIT or GO through the loophole ").capitalize()
    if choice2 == "Wait":
        choice3 = input("You have survived the traps! Now you can go through the loophole\nThere are three levers that need to be pulled.\nWhich one do you want to pull?"
                        "Type: Dragon, Titan, or Franco. ").capitalize()
        if choice3 == "Franco":
            print(" Congratulations! You pulled the right Lever....yep, that's right, the FRANCO Lever!"
                  "Boom! 🎉 And guess what?\nYou just uncovered... THE TRAITOR 😱")
        elif choice3 == "Dragon":
            print("Burned by Breath of Dragon\nGame Over HAHAHAHHAHA ")
        else:
            print("Eaten by the Titan\nGame Over😨😨😨")
    else:
        print("You are died by the traps")
else:
    print("Game Over.\n You are killed by Baldmon in front of a Castle Door")

