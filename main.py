import math


project_name = "Bowling League Tracker"
print(project_name)

bowler_league = input("Enter the name of the bowling league: ")

number_of_teams = int(input("Enter the number of teams in the league: "))
bowlers_per_team = int(input("Enter the number of bowlers per team: "))
games_per_bowler = int(input("Enter the number of games per bowler: "))

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
# Ask for the bowler's category (Male/Female)
        bowler_category = input(f"Enter the category for {bowler_name} (Male/Female): ")
# Ask for the bowler's current average
        entering_average = float(
            input(f"Enter the current average for {bowler_name}: ")
        )
# Calculate the bowler's handicap based on the current average
        handicap_current = math.floor((220 - entering_average) * 0.9)
        if handicap_current < 0:
            handicap_current = 0
        print(f"{bowler_name}'s current handicap is: {handicap_current}")
# Ask for the bowler's scores
        scores = []
        handicap_scores = []

        for game_number in range(1, games_per_bowler + 1):
            score = int(
                input(
                    f"Enter game {game_number} score "
                    f"for {bowler_name}: "
                )
            )

            scores.append(score)
            print("Recorded score:", score)

            handicap_score = score + handicap_current
            handicap_scores.append(handicap_score)
            print("Recorded handicap score:", handicap_score)
# Calculate the bowler's scratch series and handicap series totals
        scratch_series = sum(scores)
        handicap_series = sum(handicap_scores)
# Calculate the bowler's weekly average
        weekly_average = scratch_series / len(scores)
# Calculate the bowler's updated average for next week
        updated_average = (entering_average + weekly_average) / 2
# Calculate the bowler's updated handicap for next week
        handicap_update = math.floor((220 - weekly_average) * 0.9)
        if handicap_update < 0:
            handicap_update = 0
# Print the results for the bowler
        print("\nResults for", bowler_name)
        print("Category:", bowler_category)
        print("Team:", team_name)
        print("Current average:", entering_average)
        print("Current handicap:", handicap_current)
        print("Scratch games:", scores)
        print("Handicap games:", handicap_scores)
        print("Scratch series total:", scratch_series)
        print("Handicap series total:", handicap_series)
        print("This week's average:", weekly_average)
        print("Updated average for next week:", updated_average)
        print("Updated handicap for next week:", handicap_update)

        # Store the results for the bowler
        bowler_results.append({
            "name": bowler_name,
            "category": bowler_category,
            "team": team_name,
            "current_average": entering_average,
            "current_handicap": handicap_current,
            "scratch_games": scores,
            "handicap_games": handicap_scores,
            "scratch_series_total": scratch_series,
            "handicap_series_total": handicap_series,
            "this_weeks_average": weekly_average,
            "updated_average": updated_average,
            "updated_handicap": handicap_update
        })