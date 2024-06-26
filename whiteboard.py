'''# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"'''

def solution(l_street):
    if l_street.count('F') >= 2:
        return 'Outage'
    else:
        return 'Power'
    

# l_street = [ 'T', 'F', 'F', 'F' ]

# print(solution(l_street))