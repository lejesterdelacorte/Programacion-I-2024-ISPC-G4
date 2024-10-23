def bubbleSort(usersList):
    n = len(usersList)
    for i in range(n):
        for j in range(0, n-i-1):
            if usersList[j].username > usersList[j+1].username:
                usersList[j], usersList[j+1] = usersList[j+1], usersList[j]
    return usersList

def sortUsersPy(usersList):
    usersList.sort(key=lambda user: user.username)
    return usersList

