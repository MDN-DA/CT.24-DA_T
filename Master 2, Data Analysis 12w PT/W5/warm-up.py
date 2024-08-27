list = [34,67,5,81,2,45,9,23,55,41,42,84,109,109,109]

def find_mean(data):
    total = sum(data)
    count = len(data)
    mean = total/count
    return mean
print("The mean of this list is: "(find_mean))