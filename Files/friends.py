
friends = input("Enter three list of friends: ").split(",")

people = open("people.txt", "r")
people_nearby = [line.strip() for line in people.readlines()] #read lines a give you a list of lines and strip wil remove all the /n characters
people.close()

freinds_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = freinds_set.intersection(people_nearby_set)
nearby_friends_file = open("nearby_friends.txt ", "w")
for friend in friends_nearby_set:
    print(f"{friend} is nearby!")
    nearby_friends_file.write(f"{friend}\n")
nearby_friends_file.close()
