def friendsOfFriends(d):
    friends_of_friends = {}
    for person, friends in d.items():
        fofs = set()
        for friend in friends:
            fofs.update(d.get(friend, set()))
        fofs -= friends
        fofs -= {person}
        friends_of_friends[person] = fofs
    return friends_of_friends

# Test case
d = { 
    "jon": set(["arya", "tyrion"]),
    "tyrion": set(["jon", "jaime", "pod"]),
    "arya": set(["jon"]),
    "jaime": set(["tyrion", "brienne"]),
    "brienne": set(["jaime", "pod"]),
    "pod": set(["tyrion", "brienne", "jaime"]),
    "ramsay": set()
}

print(friendsOfFriends(d))
def friendsOfFriends(d):
    friends_of_friends = {}
    for person, friends in d.items():
        fofs = set()
        for friend in friends:
            fofs.update(d.get(friend, set()))
        fofs -= friends
        fofs -= {person}
        friends_of_friends[person] = fofs
    return friends_of_friends

# Test case
d = { 
    "jon": set(["arya", "tyrion"]),
    "tyrion": set(["jon", "jaime", "pod"]),
    "arya": set(["jon"]),
    "jaime": set(["tyrion", "brienne"]),
    "brienne": set(["jaime", "pod"]),
    "pod": set(["tyrion", "brienne", "jaime"]),
    "ramsay": set()
}

print(friendsOfFriends(d))
