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

for team_number in range(1, number_of_teams + 1):
    team_name = input(
        f"\nEnter the name of team {team_number}: "
    )

    print("Team Name:", team_name)

    for bowler_number in range(1, bowlers_per_team + 1):
        bowler_name = input(
            f"\nEnter the name of bowler {bowler_number} "
            f"for {team_name}: "
        )

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

        series_total = sum(scores)
        average_score = series_total / len(scores)

        print("\nResults for", bowler_name)
        print("Team:", team_name)
        print("Scores:", scores)
        print("Series total:", series_total)
        print("Average score:", average_score)