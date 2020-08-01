# 8/1/2020 Saidakbar P. Object-Oriented Programming: Exception handling, lambda function
class Trial(object):
    def __init__(self, datarow):
        self.efficiency = float(datarow[0])
        self.individual = int(datarow[1])
        self.chopstick_length = int(datarow[2])

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                self.trials.append(Trial(row))
    def num_trials(self): # returns the length of the array
        return len(self.trials)
    # average efficiency
    def avg_efficiency(self):
        efficiency_sum = 0
        for row in self.trials: # trail has each chopstick that belongs to one group length
            efficiency_sum += row.efficiency
        return efficiency_sum/self.num_trials()

avg_eff_210 = Chopstick(210).avg_efficiency()
# try-except block
class Trial(object):
    def __init__(self, datarow):
        try:
            self.efficiency = float(datarow[0])
            self.individual = int(datarow[1])
            self.chopstick_length = int(datarow[2])
        except:
            self.efficiency = -1
            self.individual = -1
            self.chopstick_length = -1

class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                trial = Trial(row)
                if trial.individual >= 0:
                    self.trials.append(trial)
    def num_trials(self):
        return len(self.trials)
    def avg_efficiency(self):
        efficiency_sum = 0
        for trial in self.trials:
            efficiency_sum += trial.efficiency
        try:
            return efficiency_sum / self.num_trials()
        except ZeroDivisionError:
            return -1.0
        
bad_average = Chopstick(100).avg_efficiency()

# lambda functions
olleh = "hello world"[4::-1]
able_string = "able was I ere I saw elba"

# Your code goes here
def is_palindrome(my_string):
    if my_string[::-1]==my_string:
        return True
    return False
phrase_palindrome = is_palindrome("able was I ere I saw elba") # true
ints = list(map(int, [1.5, 2.4, 199.7, 56.0])) # map performs the function int to each item in the list

def is_palindrome(my_string):
    return my_string == my_string[::-1]

# filter returns am item that returns True value after performing is_palindrome on that item 
palindrome_passwords = (list(filter(is_palindrome, passwords)))
# we can use a lambda function as well
palindrome_passwords = list(filter(lambda pwd: pwd[::-1]==pwd, passwords)) # this is exactly the same as previous line of code 
# more lambda function
weak_passwords = list(filter(lambda x: len(x)<6, passwords))
medium_passwords = list(filter(lambda x: 6<=len(x)<=10, passwords))
strong_passwords = list(filter(lambda x: len(x)>10, passwords))
