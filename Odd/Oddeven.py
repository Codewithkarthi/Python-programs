#To print the given list in odd and even.
nums = [43, 20, 53, 12, 53, 5, 3, 2]

even = []
odd = []

for i in nums:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
        
print("Even List: ",even)
print("Odd List: ",odd)
