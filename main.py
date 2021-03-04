# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re
import operator
import  itertools
import pickle

states = ["Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Hawaii", "Florida", "Georgia", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "North Carolina", "North Dakota", "New York", "Ohio, Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",  "Wisconsin", "Wyoming"]
capitals = ["Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Honolulu", "Tallahassee", "Atlanta", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "St. Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Raleigh", "Bismarck", "Albany", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]


Alphabetical_Sorting_States = sorted(states)
Alphabetical_Sorting_Capitals = sorted(capitals)

print("States Sorted Alphabetically", Alphabetical_Sorting_States)

print("Capitals Sorted Alphabetically", Alphabetical_Sorting_Capitals)

with open('states_alphabetical.txt','w') as f:
    for item in Alphabetical_Sorting_States:
        f.write("%s\n" % item)


with open('Capitals_Ascending.txt','w') as f:
    for item in Alphabetical_Sorting_Capitals:
        f.write("%s\n" % item)


Descending_Sorting_States = sorted(states,reverse = True)
Descending_Sorting_Capitals = sorted(capitals,reverse = True)

print("Descending order of States",Descending_Sorting_States)

print("Descending order of Capitals", Descending_Sorting_Capitals)

with open('Descending_states.txt','w') as f:
    for item in Alphabetical_Sorting_States:
        f.write("%s\n" % item)


with open('Descending_Capitals.txt','w') as f:
    for item in Alphabetical_Sorting_Capitals:
        f.write("%s\n" % item)


StatesByCount = sorted(states, key=len)
CapitalsByCount = sorted(capitals, key=len)

print("States by Count",StatesByCount)
print("Capitals By Count",CapitalsByCount)

with open('SortedStates.txt','w') as f:
    for item in Alphabetical_Sorting_States:
        f.write("%s\n" % item)


with open('SortedCapitals.txt','w') as f:
    for item in Alphabetical_Sorting_Capitals:
        f.write("%s\n" % item)




regexp = re.compile(r"(.)\1")


for str in states:
    match = re.search(regexp, str)
    if match:
        print("States with repeated characters in sequence",str)
        matchStates = str

with open('DoubleLetterSeqStates.txt','w') as f:
    for item in matchStates:
        f.write("%s\n" % item)
