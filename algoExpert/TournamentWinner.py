# Given a competitions array of two strings and a results array that contains info about winner of the competitions
# Return the winner of the tournament
# The competitions array is an array of two strings where each string is a team name. The results array corresponds with the
# competitions array and indicates 1 the hometeam as the winner and 0 indicates the hometeam is the loser

def tournamentWinner(competitions, results):

    tally = {}
    wTeam = ""
    for i in range(len(competitions)):
        if(results[i] == 1):
            cTeam = competitions[i][0]
            cTally = tally.get(cTeam, 0) + 1
            tally[cTeam] = cTally
            if(tally.get(wTeam, 0) < tally.get(cTeam, 0)):
                wTeam = cTeam
        else:
            cTeam = competitions[i][1]
            cTally = tally.get(cTeam, 0) + 1
            tally[cTeam] = cTally
            if(tally.get(wTeam, 0) < tally.get(cTeam, 0)):
                wTeam = cTeam

    # tallypair = [(v, k) for k, v in tally.items()]
    # tallypair.sort(reverse=True)

    return wTeam


# O(n) time and O(k) space
# tally up the number of wins per team name and output the team with most tallies
# look at each tuple in competition, if index 0 is 1 add index 0, else add index 1
