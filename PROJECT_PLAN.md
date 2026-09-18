# Bowling League Tracker - Project Plan

## Project Overview

The Bowling League Tracker is a Python program designed to manage and track a bowling league season.

The program will track bowlers, teams, weekly scores, matchups, league standings, handicaps, and season statistics.

The first versions of the project will be based on the rules used by my current bowling league. Later versions may allow users to configure the program for leagues with different schedules, team sizes, scoring systems, and handicap rules.

This project will also serve as a way for me to learn Python and practice designing and developing a larger software project from the ground up.

---

# Version 0.1

Version 0.1 will focus on getting the core program working using the rules of my current bowling league.

The goal is not to support every possible type of bowling league yet. League customization can be added in later versions.

## League Settings

For Version 0.1, the following settings will be built into the program:

### Schedule

- League meets weekly
- Approximately 30 weeks per season
- 3 games are bowled each week

### Teams

- 2 active bowlers per team
- Teams may also have team substitutes
- League substitutes may bowl for teams when needed

### Handicap

- Handicap is enabled
- Handicap base: 220
- Handicap percentage: 90%
- Individual handicap is based on the bowler's average

Example:

A bowler with a 180 average:

220 - 180 = 40

40 × 90% = 36 handicap

The exact handicap rounding rules still need to be confirmed.

### League Points

Each matchup has a maximum of 8 points available.

- Game 1 win: 2 points
- Game 2 win: 2 points
- Game 3 win: 2 points
- Series total win: 2 points
- Tie: 1 point to each team

---

# Program Structure

The main structure of the program will be:

League
- Teams
  - Bowlers
- League Substitutes
- Weeks
  - Matchups
    - Bowlers
    - Scores

Statistics and reports will be calculated using this information.

---

# League

The League will contain the overall information needed to run the season.

## League Information

- League ID
- League name
- Season name/year
- Number of teams
- Number of active bowlers per team
- Number of scheduled weeks
- Current week
- Number of games per matchup

## League Rules

- Handicap enabled
- Handicap base
- Handicap percentage
- Points per game win
- Points per series win
- Points awarded for ties

## League Roster

Every bowler who participates in the league will be part of the full league roster.

The league roster will then identify whether each bowler is:

- A regular team bowler
- A team substitute
- A league substitute

---

# Bowlers

Each bowler will have their own unique record.

## Stored Information

- Bowler ID
- Name
- Team ID, if applicable
- Roster type
  - Regular bowler
  - Team substitute
  - League substitute
- Games bowled
- Total pinfall

## Calculated Statistics

- Average
- Handicap
- High game
- High series

Additional bowler statistics may be added as the project develops.

---

# Teams

Each team will have its own unique record.

## Stored Information

- Team ID
- Team name
- Regular bowlers
- Team substitutes

## Calculated Statistics

- Team handicap for each week
- Total pinfall
- Points won
- Points lost
- League place
- Team high game
- Team high series

A team's handicap should be calculated using the bowlers who actually participate in a particular week's matchup rather than being stored as one permanent number.

---

# Substitutes

The league may have two types of substitutes.

## Team Substitutes

Team substitutes are officially part of a particular team's roster but are not one of the team's regular active bowlers.

They may bowl for their team when needed.

## League Substitutes

League substitutes belong to the league but are not permanently assigned to a team.

They may substitute for any team that needs another bowler.

## Substitute Statistics

When a substitute bowls:

- Their scores count toward their own individual statistics
- Their scores count toward the team they represented that week
- A league substitute does not permanently become a member of that team

The Matchup record will identify which team a bowler represented during that particular week.

---

# Weeks

Each bowling week represents one scheduled league session.

## Stored Information

- Week number
- Date
- Matchups scheduled for the week

The Week itself will remain relatively simple.

Statistics such as weekly leaders, standings, and season highs will be calculated from the scores stored in the week's matchups.

---

# Matchups

Matchups will mainly be used internally by the program.

A matchup represents two teams bowling against each other during one league week.

## Matchup Information

- Matchup ID
- Week ID
- Team 1 ID
- Team 2 ID

## Participating Bowlers

For each team:

- Bowler name
- Bowler ID
- Bowler average entering the week
- Bowler handicap entering the week
- Whether the bowler is a regular bowler or substitute

## Scores

For each participating bowler:

- Game 1
- Game 2
- Game 3
- Series total

## Team Calculations

The matchup will calculate:

- Game 1 team total
- Game 2 team total
- Game 3 team total
- Scratch series total
- Team handicap
- Handicap game totals
- Handicap series total

## Points

The matchup will determine:

- Game 1 points
- Game 2 points
- Game 3 points
- Series points
- Total points earned by each team

---

# Weekly Reports

The program should eventually be able to display information about the most recently completed league week.

## Last Week

- Matchup results
- Scores from the week
- Top individual bowlers
- Top teams
- Updated league standings
- Updated team points
- Updated team places

## Current and Next Week

- Current week's matchups
- Next week's matchups

---

# Season Statistics

The program should track statistics across the entire season.

## Bowler Statistics

- Average
- Handicap
- Games bowled
- Total pinfall
- High game
- High series
- Season leaders

## Team Statistics

- Total pinfall
- Total points
- Points won
- Points lost
- League place
- High team game
- High team series
- Season leaders

---

# Data Storage

Program data must remain available after the program closes.

Version 0.1 will need a way to save and load:

- League information
- League rules
- Bowlers
- Teams
- Substitutes
- Weeks
- Matchups
- Scores

The exact storage method will be decided during development.

A database may be added in a later version.

---

# League Rules Still to Confirm

The following information needs to be checked against my current league rules.

- [ ] Exact number of weeks in the season
- [ ] How absentee/blind scores are calculated
- [ ] Whether handicap is applied to absentee scores
- [ ] How bye teams are handled
- [ ] How teams bowling a bye earn points
- [ ] Handicap rounding rules
- [ ] Handicap rules for bowlers averaging over 220
- [ ] Review all information displayed on the current weekly league sheet

These rules will be checked at league before finalizing the Version 0.1 requirements.

---

# Future Versions

Later versions may make league rules configurable instead of using hardcoded settings.

Possible future features include:

- User-selected league schedule
- Weekly, biweekly, monthly, or custom league schedules
- Custom season length
- Custom number of bowlers per team
- Custom number of games per matchup
- Handicap enabled or disabled
- Custom handicap base
- Custom handicap percentage
- Custom scoring systems
- Multiple leagues
- Multiple seasons
- Schedule generation
- Advanced standings
- Graphs and statistics
- Graphical user interface
- Database storage
- Report exporting
- Historical player statistics
- Historical team statistics

---

# Technology

## Programming Language

Python

## Development Tools

To be determined.

## Version Control

Git and GitHub

Repository:

`bowling-league-tracker`

---

# Development Stages

## Stage 1 - Planning

- Define Version 0.1 requirements
- Confirm league rules
- Determine what information needs to be stored
- Design the program structure

## Stage 2 - Python Fundamentals

Learn the Python concepts necessary to begin building the project.

Small practice programs may be created when necessary.

## Stage 3 - Bowler System

- Create bowlers
- Assign Bowler IDs
- Store bowler information
- Store scores
- Calculate averages
- Calculate handicaps
- Calculate high games and series

## Stage 4 - Team System

- Create teams
- Assign Team IDs
- Assign bowlers to teams
- Add team substitutes
- Calculate team statistics

## Stage 5 - League Roster

- Build the complete league roster
- Identify regular bowlers
- Identify team substitutes
- Identify league substitutes

## Stage 6 - Weekly Matchups

- Schedule matchups
- Select participating bowlers
- Enter scores
- Calculate team totals
- Calculate handicap totals
- Award league points

## Stage 7 - League Standings

- Calculate total team points
- Calculate total pinfall
- Determine team placement
- Track season leaders

## Stage 8 - Saving and Loading Data

- Save program data
- Load an existing league
- Verify data remains correct between sessions

## Stage 9 - Reports

- Display previous week's results
- Display top bowlers
- Display top teams
- Display standings
- Display upcoming matchups

## Stage 10 - Testing and Improvement

- Test score calculations
- Test averages
- Test handicaps
- Test points
- Test substitutes
- Test invalid input
- Fix bugs
- Improve program organization

---

# Current Status

Planning / Requirements Gathering

Version 0.1 rules are currently being defined using my existing bowling league as the initial model.