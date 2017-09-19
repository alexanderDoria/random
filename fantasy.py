import random

picks = []
numTeams = 12

#dictates how much weight to assign to lower numbers i.e. more fairness is less weight to lower numbers
fairness = 2

#init probabilities
for i in range(1, numTeams + 1):
    prob = int(1.0 / (i + 1) * 100)
    prob = prob + int(prob / fairness) + 1
    picks.extend([i] * prob)

#check probabilities
#sum = 0
#for i in range(1, 13):
#    print (i, ": ", picks.count(i))
#    sum += picks.count(i)

#print "sum: ", sum

#pick
print ("Welcome to Bilal and Samir's Yahoo NBA Fantasy League, 2017-2018!")
for i in reversed(xrange(1, numTeams + 1)):
    raw_input()
    print "The #", i, " pick goes to... "
    raw_input()
    pick = random.choice(picks)
    picks = [p for p in picks if p != pick]
    print pick

print ("Good luck this season!")
