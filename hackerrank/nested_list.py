# Problem: Nested list (HackerRank)
# Link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


# Question:
# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
 # Note : 📌 Second Lowest number means (The number just greater than the smallest number):

# Approach: Just add a and b.
# 
# Time Complexity: (O(N^2log N)) ❌  (O(Nlog N)).✅
# I know this solution is slow 
# Status: Solved



records = []
scores =[]
names = []
for i in range(int(input("number of student :"))):
   
    name = input("Name of student :")
    score = float (input("Enter this score :"))
    records.append([name,score]) # This is the way to make lested list like 
                                 # [['Harry', 37.21], ['Berry', 37.21]
    scores.append(score)
    # scores.sort() >> Need if you use while 💡


# print(records)
# print(scores)

#❌❌❌
# secondls = scores[1]  >> [19,20 ] it grab 20
#  This way fail when score is like [19.0, 19.0, 20.0, 20.0, 21.0]
# to solve this problem I have to remove lowest value then grab 0 index value 
# for second lowest value 


# lowestval = scores[0] >> when you use while of for loop :


# IST WAY ✅🚨
# scoresN = scores[:]
# for lowestval in scoresN:
#     scores.remove(lowestval)
# SECOND WAY : ✅💡 ❌
# while lowestval in scores:
#     scores.remove(lowestval)
# secondlwval = scores[0]

# 🚨🚨✅ Instant of using while loop use set for this problem 
# because while take more time 
scoreNew =sorted(list( set(scores))) # (19,20.0)
 # scores already sorted but set distroyed the ordered so sort leter 
# remember 🚨>> Set are unordered 
secondlwval = scoreNew[1] 
  
for i in records:
    if i[1]  == secondlwval:
        # print(i)
        # print(i[1])
        names.append(i[0]) 

names.sort() # arrange names alphabatically
# print(names)
for i in names:
    print(i) # TO print every names in next line