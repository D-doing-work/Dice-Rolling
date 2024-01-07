# import random
# define a function to roll the dice
# create a dictionary that will have teh drawings of the dice
# while loop

import random

def roll_dice():

    dice_drawing = {
        1: ("⚀",
            " ———————————",
            "|     ¹     |",
            "|     ●     |",
            "|           |",
            " ——————————— "
             ),

        2: ("⚁",
            " ———————————",
            "| ●         |",
            "|     ²     |",
            "|         ● |",
            " ——————————— "
            ),

        3: ("⚂",
            " ———————————",
            "| ●   ³     |",
            "|     ●     |",
            "|         ● |",
            " ——————————— "
            ),

        4: ("⚃",
            " ———————————",
            "| ●       ● |",
            "|     ⁴     |",
            "| ●       ● |",
            " ——————————— "
            ),

        5:("⚄",
           " ———————————",
           "| ●   ⁵   ● |",
           "|     ●     |",
           "| ●       ● |",
           " ——————————— "
           ),

        6:("⚅",
           " ———————————",
           "| ●       ● |",
           "| ●   ⁶   ● |",
           "| ●       ● |",
           " ——————————— "
           )

    }

    roll = input("Do you want to roll the dice? (Yes/No): ")
    print("                                           --..........................")
    print("                                      :-=:   =+=-.              -===:  :.")
    print("                                     :   .:  *####*.            +#####: ..")
    print("                                   .:      -  -+*##:            :=*##+  .:")
    print("                                  ..        -                             :")
    print("                                 :.          -.                            :")
    print("                                :             :.                            :")
    print("                              :               ::                            :.")
    print("                              :                 .:   -==-.             :==-:  ..")
    print("                             :                    -  *####*.           =#####- .:")
    print("                           .:          -:          -  :+*##=            .=*##*   :")
    print("                           :          ###=          *-.                         =:")
    print("                         .          :###*          =#*=:.....................:=+")
    print("                          :          *##-          +. .-==-            :===.   :")
    print("                           :          ..         .-  +#####          =#####: .:")
    print("                            :                   .-  :###+-           *##*=. ..")
    print("                            :                 ::                          :.")
    print("                              :.              -:         .=*###:          :")
    print("                            ..........        -.         :#####=          :")
    print("                       ....          ...    -            -=-:           :")
    print("                    ...                 ...=   :==-            :-=-   .:")
    print("               ....                        .-#####          =#####. ..")
    print("            ...                               :=+.         .###*=. :.")
    print("          :..                :===-.                ...            ..")
    print("        .+                  #######:                 -*:.........")
    print("       *=::.                :===-.                :::.-.")
    print("      .:    :::                               .::.     -")
    print("      .: .++:  .::.                        :::   =*#=  -")
    print("      .: =###*     :::                 .::.     *###+  -")
    print("       :  +###=       :::.          :::        -###+   -")
    print("       :   :=+.          .:::...:::.            :-.    -")
    print("       :                     =##-                      -")
    print("       :                      --                       -")
    print("       :                      .:          -**-         -")
    print("       :                      .:         *###+         -")
    print("       :                      .:        -###+          -")
    print("        :                      .:         --.           :")
    print("         :                       :                      :")
    print("          :                      :                     :")
    print("           ...            --.    :   :++:          ....")
    print("              ...        -###+   :  *###=       ...")
    print("                  ...     *###+  : =###*    ....")
    print("                     ...   -**=  : .==:  ...")
    print("                       ....     :    ...")
    print("                            ...:+*-:.")


    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)

        print("Rolling the dice: 🎲 ⇵")
        print("dice rolled: {} and {} \(⍤)> ".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Do you want to roll again? (Yes/No): ")

roll_dice()