# 8/1/2020 Saidakbar P. Object-Oriented Programming: classes
import math

class Player():
    # The special __init__ function runs whenever a class is instantiated
    # The init function can take arguments, but self is always the first one
    # Self is just a reference to the instance of the class
    # It's automatically passed in when you instantiate an instance of the class
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]
# assign players to their teams in a class 
class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    # average_age for players in the given team 
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    # this below method can call its own class
    @classmethod
    def older_team(self, team1, team2):
        team1_avg = team1.average_age()
        team2_avg = team2.average_age()
        if team1_avg>team2_avg:
            return team1
        elif team1_avg<team2_avg:
            return team2

old_team = Team.older_team(Team("New York Knicks"), Team("Miami Heat"))

# operator overloading
import math

class Team(object):
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    # Define operators here
    def __lt__(self, other):
        return self.average_age() < other.average_age()
    # Implement the rest of the comparison operators here
    def __gt__(self, other):
        return self.average_age()>other.average_age()
    def __le__(self, other):
        return self.average_age()<=other.average_age()
    def __ge__(self, other):
        return self.average_age()>=other.average_age()
    def __eq__(self, other):
        return self.average_age()==other.average_age()
    def __ne__(self, other):
        return self.average_age()!=other.average_age()
    

jazz = Team("Utah Jazz")
pistons = Team("Detroit Pistons")
older_team = max([jazz, pistons])
