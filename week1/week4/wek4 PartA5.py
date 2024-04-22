def mostPopularFriend(d):
    friend_count = {}
    
    # Count occurrences of each friend
    for friends in d.values():
        for friend in friends:
            friend_count[friend] = friend_count.get(friend, 0) + 1
            
    # Find the friend with the highest count
    most_popular_friend = max(friend_count, key=friend_count.get)
    
    return most_popular_friend
