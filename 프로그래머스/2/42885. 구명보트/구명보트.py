def solution(people, limit):
    people.sort()
    print(people)
    left = 0
    right = len(people) - 1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            boats += 1
        else:
            right -= 1
            boats += 1
            
    return boats