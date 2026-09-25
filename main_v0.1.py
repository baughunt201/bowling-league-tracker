# Bowling League Tracker
# Hunter Baughman
# 9/24/2026
# Added functionality to calculate the bowler's handicap scores and series total based on their qualifying entering average or first-session average.

# Used the math module to round handicap calculations down according to league rules.
import math

# Project name
project_name = "Bowling League Tracker"
print(project_name)

# Get user input for the bowling league details
bowler_league = input("Enter the name of the bowling league: ")
number_of_teams = int(input("Enter the number of teams in the league: "))
bowlers_per_team = int(input("Enter the number of bowlers per team: "))
games_per_bowler = int(input("Enter the number of games per bowler: "))

# Print the bowling league details
print("Bowling League:", bowler_league)
print("Number of Teams:", number_of_teams)
print("Bowlers per Team:", bowlers_per_team)
print("Games per Bowler:", games_per_bowler)

#Store the results for each bowler in a list of dictionaries
bowler_results = []

# Ask for the team name
for team_number in range(1, number_of_teams + 1):
    team_name = input(
        f"\nEnter the name of team {team_number}: "
    )
    print("Team Name:", team_name)

    # Ask for the bowlers name
    for bowler_number in range(1, bowlers_per_team + 1):
        bowler_name = input(
            f"\nEnter the name of bowler {bowler_number} "
            f"for {team_name}: "
        )

        # Ask if the bowler has a qualifying entering average or if they are a new bowler
        has_entering_average = input(f"Does {bowler_name} have a qualifying entering average? (yes/no): ").strip().lower()
        if has_entering_average == "no":
            print(f"{bowler_name} does not have a qualifying entering average.")
            entering_average = None
        else:
            entering_average = float(
            input(f"Enter the qualifying entering average for {bowler_name}: ")
            )

        # Ask for the bowler's category (Male/Female)
        bowler_category = input(f"Enter the category for {bowler_name} (Male/Female): ")

        # Ask for the bowler's scores
        scores = []
        for game_number in range(1, games_per_bowler + 1):
            score = int(
                input(
                    f"Enter game {game_number} score "
                    f"for {bowler_name}: "
                )
            )

            scores.append(score)
            print("Recorded score:", score)

        # Calculate the bowler's scratch series total
        scratch_series = sum(scores)

        # Calculate the bowler's weekly average
        weekly_average = scratch_series / len(scores)

        # Store the bowler's season totals
        games_bowled = len(scores)
        total_pinfall = scratch_series

        # Calculate the bowler's season average
        season_average = total_pinfall / games_bowled

        # Determine which average should be used for the Week 1 handicap
        if entering_average is not None:
            handicap_current = math.floor((220 - entering_average) * 0.9)
        else:
            handicap_current = math.floor((220 - weekly_average) * 0.9)

        if handicap_current < 0:
            handicap_current = 0

        print(f"{bowler_name}'s current handicap is: {handicap_current}")

        # Calculate the bowler's handicap scores
        handicap_scores = []

        for score in scores:
            handicap_score = score + handicap_current
            handicap_scores.append(handicap_score)

        # Calculate the bowler's handicap series total
        handicap_series = sum(handicap_scores)

        # Print the results for the bowler
        print("\nResults for", bowler_name)
        print("Category:", bowler_category)
        print("Team:", team_name)
        print("Qualifying entering average:", entering_average)
        print("Current handicap:", handicap_current)
        print("Scratch games:", scores)
        print("Scratch series total:", scratch_series)
        print("This week's average:", weekly_average)
        print("Season average:", season_average)
        print("Handicap series total:", handicap_series)

        # Store the results for the bowler
        bowler_results.append({
            "name": bowler_name,
            "category": bowler_category,
            "team": team_name,
            "qualifying_entering_average": entering_average,
            "current_handicap": handicap_current,
            "scratch_games": scores,
            "scratch_series_total": scratch_series,
            "this_weeks_average": weekly_average,
            "games_bowled": games_bowled,
            "total_pinfall": total_pinfall,
            "season_average": season_average,
            "handicap_scores": handicap_scores,
            "handicap_series_total": handicap_series,
        })

# 

# From here on I will start working on setting up "results" page that will display the points won for each team and the overall league standings. 
# I will also add a top scores page that will display the top three scratch games, handicap games, scratch series, and handicap series for each week.
# Later I plan to add a feature that will allow the user to save the results to a file and load them back in later. 
# This will allow the user to keep track of their league standings over time.
