# Leen Said 2220356194

import sys

# create empty lists
player1_shown = []
player2_shown = []

# read the textfiles
try:
    f0 = open(sys.argv[1], "r")
    read0 = f0.readlines()
    f1 = open(sys.argv[2], "r")
    read1 = f1.readlines()
    f2 = open(sys.argv[3], "r")
    readinput1 = f2.readlines()
    f3 = open(sys.argv[4], "r")
    readinput2 = f3.readlines()
    writeto = open(sys.argv[5], "w")
except IOError as e:
    print("IOError: input file(s)", e, "is/are not reachable.")


# create list of lists using the placements of the ships by players
values1_l = []
for s in read0:
    values1 = str(s).replace("\n", "").split(";")
    values1_l.append(values1)

values2_l = []
for k in read1:
    values2 = str(k).replace("\n", "").split(";")
    values2_l.append(values2)

# create 2 multidimensional lists as the "shown grids" in the game
for i in range(10):
    player1_shown.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
    player2_shown.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])


# turn the lines in the Player1/2.in.txt into one string
strr1 = ""
for cordinate1 in readinput1:
    cordinate1 = cordinate1.replace("\n", "")
    strr1 += cordinate1
    # separate the string by ";"
    list_of_coordinates1 = strr1.split(";")
# pop the last element of the list since it will be empty because the string was split by ; at the end
list_of_coordinates1.pop()

strr2 = ""
for cordinate2 in readinput2:
    cordinate2 = cordinate2.replace("\n", "")
    strr2 += cordinate2
    list_of_coordinates2 = strr2.split(";")
list_of_coordinates2.pop()

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# function to number Battleships and Patrol boats since there are more than 1
def identify_ships(lis):
    p = 1
    b = 1
    hidden = {}
    for i in lis:
        for k in i:
            if k == "P":
                indouter = lis.index(i)
                indinner = i.index(k)
                if lis[indouter][indinner + 1] == "P":
                    lis[indouter][indinner] = "P" + str(p)
                    lis[indouter][indinner + 1] = "P" + str(p)
                else:
                    lis[indouter][indinner] = "P" + str(p)
                    lis[indouter + 1][indinner] = "P" + str(p)
                p += 1

            if k == "B":
                indouter = lis.index(i)
                indinner = i.index(k)
                if lis[indouter][indinner + 2] == "B":
                    lis[indouter][indinner] = "B" + str(b)
                    lis[indouter][indinner + 1] = "B" + str(b)
                    lis[indouter][indinner + 2] = "B" + str(b)
                    lis[indouter][indinner + 3] = "B" + str(b)
                else:
                    lis[indouter][indinner] = "B" + str(b)
                    lis[indouter + 1][indinner] = "B" + str(b)
                    lis[indouter + 2][indinner] = "B" + str(b)
                    lis[indouter + 3][indinner] = "B" + str(b)

                b += 1

    for i in range(len(lis)):
        hidden[i] = lis[i]
    for i in hidden.values():
        if len(i) == 9:
            i.append("")
        elif len(i) == 8:
            i.append("", "")
    return hidden


# function to return a set of row and column to work with
def read_input(list_Cord, indexx):
    val = list_Cord[indexx]
    try:
        # find the index of "," separator
        ind = val.index(",")
        # try and except
        try:
            # locate the row, here -1 is added since the indexing of the grids in our program
            # starts from 0, however it starts from 1 in the input given by users
            row = int(val[0:ind])
            if int(val[0:ind]) == "":
                raise IndexError
            try:
                column_in_letter = val[ind + 1 :]
                try:
                    if val[ind + 1 :] == "":
                        raise IndexError
                    if len(column_in_letter) > 1:
                        raise Exception
                    # convert the letter into a number according to its alphabetical order
                    column_in_int = alpha.index(column_in_letter)
                    cords = (row, column_in_int, column_in_letter)
                    return cords
                except IndexError:
                    print("IndexError: column was not given.")
                    writeto.writelines("\nIndexError: column was not given.\n")
                    return False
                except Exception:
                    print("No semi-colon separator was given!")
                    writeto.writelines("\nNo semi-colon separator was given!\n")
                    return False
            except ValueError:
                print("ValueError: inappropriate value given for column.")
                writeto.writelines(
                    "\nValueError: inappropriate value given for column.\n"
                )
                return False
        except IndexError:
            print("IndexError: row was not given.")
            writeto.writelines("\nIndexError: row was not given.\n")
            return False
        except ValueError:
            print("ValueError: inappropriate value given for row.")
            writeto.writelines("\nValueError: inappropriate value given for row.\n")
            return False
    except IndexError:
        print("IndexError: No input was given.")
        writeto.writelines("\nIndexError: No input was given.\n")
        return False
    except ValueError:
        print("No comma separator was given!")
        writeto.writelines("\nNo comma separator was given!\n")
        return False
    except:
        print("kaBOOM: run for your life")
        writeto.writelines("\nkaBOOM: run for your life\n")
        return False


# function to update grids using the set of row and column given by user
def update_grid(cordinates, hidden, shown):
    try:
        row, column, col_letter = cordinates
        # if the cell in the hidden grid is empty turn the cell
        # with same coordinates in the hidden grid into O
        row = int(row) - 1
        if hidden[row][column] == "":
            shown[row][column] = "O"

        # if the cell in the hidden grid is NOT empty turn the cell with same
        # coordinates in the hidden grid into X as well as change the value in
        #  the hidden grid into "-" to indicate it's been emptied
        else:
            shown[row][column] = "X"
            hidden[row][column] = ""
    except:
        print("kaBOOM: run for your life")
        writeto.writelines("\nkaBOOM: run for your life\n")


# Dictionaries dict1 and dict2 are going to be printed under thr grid
lp = ["-", "-", "-", "-"]
lb = ["-", "-"]
dict1 = {
    "Carrier": ["-"],
    "Battleship": lb,
    "Destroyer": ["-"],
    "Submarine": ["-"],
    "Patrol Boat": lp,
}
dict2 = {
    "Carrier": ["-"],
    "Battleship": lb,
    "Destroyer": ["-"],
    "Submarine": ["-"],
    "Patrol Boat": lp,
}

# function counter() counts the number of each type of ship in the grid
def counter(hidden):
    c, b1, b2, d, s, p1, p2, p3, p4 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in hidden.values():
        c += i.count("C")
        b1 += i.count("B1")
        b2 += i.count("B2")
        d += i.count("D")
        s += i.count("S")
        p1 += i.count("P1")
        p2 += i.count("P2")
        p3 += i.count("P3")
        p4 += i.count("P4")
    return (c, b1, b2, d, s, p1, p2, p3, p4)


# function to update the dictionary using data from the list of ships
def update_dict(dict, hidden):
    c, b1, b2, d, s, p1, p2, p3, p4 = counter(hidden)
    if c == 0:
        dict["Carrier"] = ["X"]

    if b1 == 0:
        lb[1] = "X"
    if b2 == 0:
        lb[0] = "X"
    dict["Battleship"] = lb
    if d == 0:
        dict["Destroyer"] = ["X"]

    if s == 0:
        dict["Submarine"] = ["X"]

    if p1 == 0:
        lp[0] = "X"
    elif p2 == 0:
        lp[1] = "X"
    elif p3 == 0:
        lp[2] = "X"
    elif p4 == 0:
        lp[3] = "X"
    dict["Patrol Boat"] = lp


# function to terminate the game
def determine_game_end(hidden1, hidden2):
    # this function checks if either one or both lists are completely empty
    # and returns True
    if sum(counter(hidden1)) == 0 or sum(counter(hidden2)) == 0:
        if sum(counter(hidden1)) == 0:
            print("Player 2 wins!\n")
            writeto.writelines("\nPlayer 2 wins!\n\n")
            return True
        else:
            print("Player 1 wins!\n")
            writeto.writelines("\nPlayer 1 wins!\n\n")
            return True

    elif sum(counter(hidden1)) == 0 and sum(counter(hidden2)) == 0:
        print("It's a draw!\n")
        writeto.writelines("\nIt's a draw!\n\n")
        return True
    else:
        pass


# function to display grids and iteractive interface on the screen
def display(n, round, dict1, dict2, coordinates, writeto):
    try:
        lines = []
        lines.append("\nPlayer" + str(n) + "'s Move\n")
        if len(str(round)) == 1:
            lines.append(
                "\nRound : "
                + str(round)
                + "                     "
                + "Grid Size: 10x10\n"
            )
        elif len(str(round)) == 2:
            lines.append(
                "\nRound : "
                + str(round)
                + "                    "
                + "Grid Size: 10x10\n"
            )
        elif len(str(round)) == 3:
            lines.append(
                "\nRound : " + str(round) + "                   " + "Grid Size: 10x10\n"
            )
        lines.append("\nPlayer1's Hidden Board       Player2's Hidden Board\n")
        lines.append("  A B C D E F G H I J          A B C D E F G H I J\n")

        print("\nPlayer" + str(n) + "'s Move")
        print("\nRound :", round, end="")
        print("                 ", "Grid Size: 10x10")
        print("\nPlayer1’s Hidden Board       Player2’s Hidden Board")
        print("   A B C D E F G H I J         A B C D E F G H I J")
        for q in range(1, 10):
            print(q, "", *player1_shown[q - 1], "    ", q, "", *player2_shown[q - 1])
            lines.append(
                str(q)
                + " "
                + " ".join(player1_shown[q - 1])
                + "        "
                + str(q)
                + " "
                + " ".join(player2_shown[q - 1])
                + "\n"
            )
        print("10", *player1_shown[9], "    ", "10", *player2_shown[9], "\n")
        lines.append(
            "10"
            + " ".join(player1_shown[9])
            + "        "
            + "10"
            + " ".join(player2_shown[9])
            + " \n"
        )
        lines.append("\n")
        for i in dict1.keys():
            if i == "Carrier":
                print(i, *dict1[i], "                 ", i, *dict2[i])
                lines.append(
                    i
                    + "     "
                    + " ".join(dict1[i])
                    + "                "
                    + i
                    + "     "
                    + " ".join(dict2[i])
                    + "\n"
                )
            elif i == "Battleship":
                print(i, *dict1[i], "            ", i, *dict2[i])
                lines.append(
                    i
                    + "  "
                    + " ".join(dict1[i])
                    + "              "
                    + i
                    + "  "
                    + " ".join(dict2[i])
                    + "\n"
                )
            elif i == "Destroyer":
                print(i, *dict1[i], "               ", i, *dict2[i])
                lines.append(
                    i
                    + "   "
                    + " ".join(dict1[i])
                    + "                "
                    + i
                    + "   "
                    + " ".join(dict2[i])
                    + "\n"
                )
            elif i == "Submarine":
                print(i, *dict1[i], "               ", i, *dict2[i])
                lines.append(
                    i
                    + "   "
                    + " ".join(dict1[i])
                    + "                "
                    + i
                    + "   "
                    + " ".join(dict2[i])
                    + "\n"
                )
            else:
                print(i, *dict1[i], "       ", i, *dict2[i])
                lines.append(
                    i
                    + " "
                    + " ".join(dict1[i])
                    + "          "
                    + i
                    + " "
                    + " ".join(dict2[i])
                    + "\n"
                )

        r, c, cl = coordinates
        print("\nEnter your move:", str(r) + "," + str(cl), "\n")
        lines.append("\nEnter your move:" + str(r) + "," + str(cl) + "\n")
    except:
        pass
    writeto.writelines(lines)  # Write the entire list of lines to the file


print("Battle of Ships Game")
writeto.writelines("Battle of Ships Game\n")
# set round = 1
round_of_players = 1
p1 = 0
p2 = 0
# initiate the loop
while True:
    # utilize the functions for both player1 and player2 data
    player1_hidden = identify_ships(values1_l)
    player2_hidden = identify_ships(values2_l)

    # Player1:
    if read_input(list_of_coordinates1, p1):
        coordinates1 = read_input(list_of_coordinates1, p1)
    else:
        # in case an error was found in the input given by player, 
        # the program will read another of the player's input
        p1 += 1
        coordinates1 = read_input(list_of_coordinates1, p1)
    display(1, round_of_players, dict1, dict2, coordinates1, writeto)
    update_grid(coordinates1, player2_hidden, player2_shown)
    update_dict(dict1, player1_hidden)
    # increment by 1
    p1 += 1
    # check if the game terminates
    if determine_game_end(player1_hidden, player2_hidden):
        update_dict(dict1, player1_hidden)
        break
    else:
        pass

    # repeat the same for Player 2
    if read_input(list_of_coordinates2, p2):
        coordinates2 = read_input(list_of_coordinates2, p2)
    else:
        p2 += 1
        coordinates2 = read_input(list_of_coordinates2, p2)
    display(2, round_of_players, dict1, dict2, coordinates2, writeto)
    update_grid(coordinates2, player1_hidden, player1_shown)
    update_dict(dict2, player2_hidden)
    p2 += 1
    if determine_game_end(player1_hidden, player2_hidden):
        update_dict(dict2, player2_hidden)
        break
    else:
        pass
    
    # increment round by 1
    round_of_players += 1

# update the dictionaries once the game terminates before printing the final information
update_dict(dict1, player1_hidden)
update_dict(dict2, player2_hidden)

# when the game terminates and either of players win
print("Final Information\n")
writeto.writelines("Final Information\n\n")
print("Player1's Hidden Board       Player2's Hidden Board\n")
writeto.writelines("Player1's Hidden Board       Player2's Hidden Board\n")
print("   A B C D E F G H I J         A B C D E F G H I J")
writeto.writelines("  A B C D E F G H I J         A B C D E F G H I J\n")
lines = []
for q in range(1, 10):
    print(q, "", *player1_shown[q - 1], "    ", q, "", *player2_shown[q - 1])
    lines.append(
        str(q)
        + " "
        + " ".join(player1_shown[q - 1])
        + "        "
        + str(q)
        + " "
        + " ".join(player2_shown[q - 1])
        + "\n"
    )
print("10", *player1_shown[9], "    ", "10", *player2_shown[9], "\n")
lines.append(
    "10"
    + " ".join(player1_shown[9])
    + "        "
    + "10"
    + " ".join(player2_shown[9])
    + " \n"
)
lines.append("\n")
for i in dict1.keys():
    if i == "Carrier":
        print(i, *dict1[i], "                 ", i, *dict2[i])
        lines.append(
            i
            + "     "
            + " ".join(dict1[i])
            + "                "
            + i
            + "     "
            + " ".join(dict2[i])
            + "\n"
        )
    elif i == "Battleship":
        print(i, *dict1[i], "            ", i, *dict2[i])
        lines.append(
            i
            + "  "
            + " ".join(dict1[i])
            + "              "
            + i
            + "  "
            + " ".join(dict2[i])
            + "\n"
        )
    elif i == "Destroyer":
        print(i, *dict1[i], "               ", i, *dict2[i])
        lines.append(
            i
            + "   "
            + " ".join(dict1[i])
            + "                "
            + i
            + "   "
            + " ".join(dict2[i])
            + "\n"
        )
    elif i == "Submarine":
        print(i, *dict1[i], "               ", i, *dict2[i])
        lines.append(
            i
            + "   "
            + " ".join(dict1[i])
            + "                "
            + i
            + "   "
            + " ".join(dict2[i])
            + "\n"
        )
    else:
        print(i, *dict1[i], "       ", i, *dict2[i])
        lines.append(
            i
            + " "
            + " ".join(dict1[i])
            + "          "
            + i
            + " "
            + " ".join(dict2[i])
            + "\n"
        )

writeto.writelines(lines)
