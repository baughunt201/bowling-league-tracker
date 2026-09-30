# Bowling League Tracker version 0.2.0
# Hunter Baughman
# 9/24/2026
# Added functionality to calculate the bowler's handicap scores and series total based on their qualifying entering average or first-session average.

# Used the math module to round handicap calculations down according to league rules.
import math

# Project name
project_name = "Bowling League Tracker"
print(f"\nWelcome to {project_name} version 0.2.0")


running = True # Sets the running variable to True to start the main menu loop

# Main menu loop
while running:
    print("\nPlease select an option:")
    print("\n1. Start")
    print("2. Help")
    print("3. Exit")

    choice = input("\nEnter your choice (1, 2, or 3): ")

    if choice == "1":
        leagues_menu = True # Sets the leagues_menu variable to True to start the leagues menu loop

        # Handle the user's choice
        while leagues_menu:
            print("\nPlease select an option:")
            print("\n1. New League")
            print("2. Existing League")
            print("3. Back to Main Menu")

            leagues_choice = input("\nChoice: ")
            if leagues_choice == "1":
                print("\nNew League functionality goes here.")
                bowling_league = input("\nEnter the name of the bowling league: ")
                bowling_alley = input("Enter the name of the bowling alley: ")
                city_state = input("Enter the city and state of the bowling alley (e.g., New York, NY): ")
                number_of_teams = int(input("Enter the number of teams in the league: "))
                bowlers_per_team = int(input("Enter the number of bowlers per team: "))
                games_per_bowler = int(input("Enter the number of games per bowler: "))
                handicap_base = int(input("Enter the handicap base (e.g., 200): "))
                handicap_percentage = float(input("Enter the handicap percentage (e.g., .8 for 80%): "))
                bowling_weeks = int(input("Enter the number of weeks in the bowling season: "))
                first_week = input("Enter the date of the first week of bowling (e.g., 09/01/2026): ")

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

            elif leagues_choice == "2":
                print("\nExisting League functionality goes here.")
            elif leagues_choice == "3":
                leagues_menu = False
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")

    elif choice == "2":
        print("\nWelcome to the Bowling League Tracker Help Section.")
        print("\nHere are some frequently asked questions and answers:")
        print("\nQ: How do I create a new bowling league?")
        print("A: From the main menu, select 'Start' and then 'New League'.")
        print("\nQ: How do I view an existing bowling league?")
        print("A: From the main menu, select 'Start' and then 'Existing League'.")
    elif choice == "3":
        print("\nExiting the program.")
        running = False # Sets the running variable to False to exit the main menu loop
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")