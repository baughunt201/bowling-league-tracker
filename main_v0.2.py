# Bowling League Tracker version 0.2.0
# Hunter Baughman
# 9/24/2026
#
# Version 0.2 focuses on restructuring the program into functions
# and beginning the league -> teams -> bowlers data structure.
#
# CURRENT STRUCTURE:
# Main Program
#     -> create_league()
#         -> returns a league dictionary
#     -> create_teams(league)
#         -> calls create_bowlers(league, team_name)
#         -> returns a list of team dictionaries
#
# NOTE:
# The math module is not currently being used in v0.2, but it will
# eventually be needed again for handicap calculations.
import math

# Project name
project_name = "Bowling League Tracker"
print(f"\nWelcome to {project_name} version 0.2.0")


# -------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------

# A function is a named section of code that performs a specific job.
#
# "def" means DEFINE a function.
#
# show_help() does not need any parameters because it does not need
# information from another part of the program.
#
# It also does not need to return anything because its only job is
# to display information to the user.
def show_help():
    print("\nWelcome to the Bowling League Tracker Help Section.")
    print("\nHere are some frequently asked questions and answers:")
    print("\nQ: How do I create a new bowling league?")
    print("A: From the main menu, select 'Start' and then 'New League'.")
    print("\nQ: How do I view an existing bowling league?")
    print("A: From the main menu, select 'Start' and then 'Existing League'.")


# Creates a new league and returns the finished league dictionary.
#
# Unlike show_help(), this function produces data that the rest of
# the program needs, so it uses "return league" at the end.
def create_league():

    # Gather the league information from the user.
    #
    # input() always returns a string.
    #
    # int() converts input into a whole number.
    # float() converts input into a decimal number.
    bowling_league = input("\nEnter the name of the bowling league: ")
    bowling_alley = input("Enter the name of the bowling alley: ")
    city_state = input(
        "Enter the city and state of the bowling alley (e.g., New York, NY): "
    )
    number_of_teams = int(input("Enter the number of teams in the league: "))
    bowlers_per_team = int(input("Enter the number of bowlers per team: "))
    games_per_bowler = int(input("Enter the number of games per bowler: "))
    handicap_base = int(input("Enter the handicap base (e.g., 200): "))
    handicap_percentage = float(
        input("Enter the handicap percentage (e.g., .8 for 80%): ")
    )
    bowling_weeks = int(
        input("Enter the number of weeks in the bowling season: ")
    )
    first_week = input(
        "Enter the date of the first week of bowling (e.g., 09/01/2026): "
    )

    # A dictionary groups related information together using
    # KEY : VALUE pairs.
    #
    # Example:
    # "name" is the key
    # bowling_league is the value stored under that key
    #
    # Later we can access the information with:
    # league["name"]
    league = {
        "name": bowling_league,
        "alley": bowling_alley,
        "location": city_state,
        "number_of_teams": number_of_teams,
        "bowlers_per_team": bowlers_per_team,
        "games_per_bowler": games_per_bowler,
        "handicap_base": handicap_base,
        "handicap_percentage": handicap_percentage,
        "number_of_weeks": bowling_weeks,
        "first_week": first_week,
    }

    # A Boolean can only be True or False.
    #
    # While editing is True, this loop continues running.
    # When editing becomes False, the loop ends.
    editing = True

    while editing:

        # Display the information currently stored in the dictionary.
        print("\nLeague Details:")
        print("\nName:", league["name"])
        print("Alley:", league["alley"])
        print("Location:", league["location"])
        print("Number of Teams:", league["number_of_teams"])
        print("Bowlers per Team:", league["bowlers_per_team"])
        print("Games per Bowler:", league["games_per_bowler"])
        print("Handicap Base:", league["handicap_base"])
        print("Handicap Percentage:", league["handicap_percentage"])
        print("Number of Weeks:", league["number_of_weeks"])
        print("First Week:", league["first_week"])

        # .strip() removes extra spaces from the beginning/end.
        # .lower() converts the user's answer to lowercase.
        #
        # Example:
        # " YES " -> "yes"
        edit_choice = input(
            "\nWould you like to edit any of these details? (yes/no): "
        ).strip().lower()

        if edit_choice == "yes":
            print("\nWhich field would you like to edit?")
            print("1. League Name")
            print("2. Bowling Alley")
            print("3. Location")
            print("4. Number of Teams")
            print("5. Bowlers per Team")
            print("6. Games per Bowler")
            print("7. Handicap Base")
            print("8. Handicap Percentage")
            print("9. Number of Weeks")
            print("10. First Week")

            field_choice = input("\nEnter your choice (1-10): ")

            # This section translates the number the user sees
            # into the actual dictionary key Python needs.
            #
            # Example:
            # User enters "4"
            # field_to_edit becomes "number_of_teams"
            if field_choice == "1":
                field_to_edit = "name"
            elif field_choice == "2":
                field_to_edit = "alley"
            elif field_choice == "3":
                field_to_edit = "location"
            elif field_choice == "4":
                field_to_edit = "number_of_teams"
            elif field_choice == "5":
                field_to_edit = "bowlers_per_team"
            elif field_choice == "6":
                field_to_edit = "games_per_bowler"
            elif field_choice == "7":
                field_to_edit = "handicap_base"
            elif field_choice == "8":
                field_to_edit = "handicap_percentage"
            elif field_choice == "9":
                field_to_edit = "number_of_weeks"
            elif field_choice == "10":
                field_to_edit = "first_week"
            else:
                field_to_edit = "invalid"

            # "in" checks whether something exists in a collection.
            #
            # Since league is a dictionary, this checks whether
            # field_to_edit matches one of the dictionary's keys.
            if field_to_edit in league:

                # input() gives us a string at first.
                new_value = input(
                    f"Enter the new value for {field_to_edit}: "
                )

                # These fields need to remain integers.
                #
                # This list lets us check several possible fields
                # using one "if" statement.
                if field_to_edit in [
                    "number_of_teams",
                    "bowlers_per_team",
                    "games_per_bowler",
                    "handicap_base",
                    "number_of_weeks",
                ]:
                    new_value = int(new_value)

                # Handicap percentage needs to remain a float.
                elif field_to_edit == "handicap_percentage":
                    new_value = float(new_value)

                # Dynamic dictionary access:
                #
                # field_to_edit contains the name of the key.
                #
                # Example:
                # field_to_edit = "location"
                #
                # This:
                # league[field_to_edit] = new_value
                #
                # effectively becomes:
                # league["location"] = new_value
                league[field_to_edit] = new_value

            else:
                print(
                    "\nInvalid choice. Please enter a number from 1 to 10."
                )

        elif edit_choice == "no":

            # Changing the Boolean to False ends the while loop.
            editing = False

        else:
            # If the user enters anything other than yes/no,
            # editing stays True, so the loop repeats.
            print("\nInvalid choice. Please enter 'yes' or 'no'.")

    # RETURN sends the completed dictionary back to whoever
    # called create_league().
    #
    # In the main program:
    #
    # league = create_league()
    #
    # the returned dictionary gets stored in the variable "league".
    return league


# Creates all of the teams required by the league.
#
# "league" is a PARAMETER.
#
# A parameter allows information from another part of the program
# to be passed INTO a function.
#
# When we call:
#
# create_teams(league)
#
# the league dictionary becomes available inside this function.
def create_teams(league):

    # Start with an empty LIST.
    #
    # Each completed team dictionary will be added to this list.
    teams = []

    # league["number_of_teams"] tells this function how many
    # teams need to be created.
    #
    # range() stops BEFORE its ending number.
    #
    # If number_of_teams = 12:
    #
    # range(1, 12 + 1)
    #
    # becomes:
    #
    # 1 through 12
    for team_number in range(
        1, league["number_of_teams"] + 1
    ):
        team_name = input(
            f"\nEnter the name of team {team_number}: "
        )

        # A function can call another function.
        #
        # create_teams() pauses here while create_bowlers() runs.
        #
        # We pass TWO arguments:
        #
        # league    -> gives the function league information
        # team_name -> tells it which team these bowlers belong to
        #
        # create_bowlers() returns a LIST of bowlers.
        bowlers = create_bowlers(league, team_name)

        # Each team is stored as a dictionary.
        #
        # "bowlers" contains the list returned by create_bowlers().
        team = {
            "name": team_name,
            "bowlers": bowlers,
        }

        # append() adds ONE item to the end of a list.
        #
        # Here we add the completed team dictionary to teams.
        teams.append(team)

    # After every team has been created, return the entire list.
    return teams


# Creates the bowlers belonging to one team.
#
# This function currently receives two parameters:
#
# league    -> the league dictionary
# team_name -> the name of the team currently being created
def create_bowlers(league, team_name):

    # Empty list that will eventually contain all bowler
    # dictionaries for this particular team.
    bowlers = []

    # league["bowlers_per_team"] determines how many times
    # the loop runs.
    for bowler_number in range(
        1, league["bowlers_per_team"] + 1
    ):
        bowler_name = input(
            f"Enter bowler {bowler_number} for {team_name}: "
        )

        # Right now a bowler only contains a name.
        #
        # NEXT SESSION:
        # Expand this dictionary with:
        #
        # - gender
        # - entering average
        # - USBC number
        # - phone number
        # - address
        # - email
        # - roster status
        #
        # We also discussed eventually keeping the program's own
        # bowler ID separate from the USBC number.
        bowler = {
            "name": bowler_name
        }

        # Add this bowler dictionary to the team's bowler list.
        bowlers.append(bowler)

    # Return all bowlers for this team back to create_teams().
    return bowlers


# -------------------------------------------------------------------
# NOTES FOR NEXT SESSION
# -------------------------------------------------------------------
#
# Next focus: continue building create_bowlers().
#
# 1. Add a validated gender choice:
#
#       1. Male
#       2. Female
#
#    Use a while loop so invalid choices are asked again.
#
#
# 2. Add entering-average logic.
#
#    Ask:
#       Does this bowler have an entering average?
#
#    If YES:
#       ask for the average and store it as an integer.
#
#    If NO:
#       entering_average = None
#
#
# None means:
#       "There is currently no value here."
#
# It is NOT the same as:
#
#       0       -> an actual numeric value of zero
#       ""      -> an empty string
#       "None"  -> text containing the word None
#
# Correct:
#
#       entering_average = None
#
#
# The planned validation flow:
#
#       asking_for_average = True
#
#       while asking_for_average:
#
#           yes -> collect average -> stop loop
#           no  -> use None        -> stop loop
#           invalid -> print error -> loop repeats
#
#
# 3. Add roster status as a controlled choice:
#
#       1. Regular Member
#       2. Substitute
#
#
# 4. Add the simpler string fields:
#
#       USBC number
#       Phone number
#       Address
#       Email
#
#
# Phone numbers and USBC numbers should be stored as STRINGS,
# even though they contain numbers, because we do not perform
# mathematical calculations with them.
#
#
# FUTURE DATA STRUCTURE:
#
# League
# |
# +-- Teams
#     |
#     +-- Team
#         |
#         +-- Bowlers
#             |
#             +-- Bowler
#
#
# Eventually the teams list can be stored inside the league
# dictionary with:
#
#       league["teams"] = teams
#
# We intentionally did NOT add that yet.
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------------

# Controls whether the entire application is running.
running = True


# Main menu loop
while running:
    print("\nPlease select an option:")
    print("\n1. Start")
    print("2. Help")
    print("3. Exit")

    choice = input(
        "\nEnter your choice (1, 2, or 3): "
    )

    if choice == "1":

        # Separate Boolean controls the leagues submenu.
        #
        # Setting leagues_menu to False returns the user to
        # the main menu without closing the entire application.
        leagues_menu = True

        while leagues_menu:
            print("\nPlease select an option:")
            print("\n1. New League")
            print("2. Existing League")
            print("3. Back to Main Menu")

            leagues_choice = input("\nChoice: ")

            if leagues_choice == "1":
                print("\nNew League functionality goes here.")

                # CALL create_league().
                #
                # The returned dictionary is stored in "league".
                league = create_league()

                # PASS the league dictionary into create_teams().
                #
                # create_teams() returns a list of team dictionaries.
                teams = create_teams(league)

            elif leagues_choice == "2":
                print(
                    "\nExisting League functionality goes here."
                )

            elif leagues_choice == "3":

                # Ends ONLY the leagues submenu.
                leagues_menu = False

            else:
                print(
                    "\nInvalid choice. Please enter 1, 2, or 3."
                )

    elif choice == "2":

        # Function CALL.
        #
        # Python jumps to show_help(), runs it, then comes
        # back here when the function finishes.
        show_help()

    elif choice == "3":
        print("\nExiting the program.")

        # Ends the main menu loop and therefore the application.
        running = False

    else:
        print(
            "\nInvalid choice. Please enter 1, 2, or 3."
        )