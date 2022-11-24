def find2(expenses):

    for i in range(0, len(expenses)-2):
        for j in range(i+1, len(expenses)-1):
            if expenses[i] + expenses[j] == 2020:
                return expenses[i] * expenses[j]
    return -1

def find3(expenses):
    
    for i in range(0, len(expenses)-3):
        for j in range(i+1, len(expenses)-2):
            for k in range(i+1, len(expenses)-1):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i] * expenses[j] * expenses[k]
    return -1