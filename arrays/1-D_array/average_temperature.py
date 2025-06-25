temperature = [1,2,3,4,5,6,7,8,9,10]
total = 0

for i in range(1,len(temperature)+1):
    total += i

number_of_days = len(temperature)

average_of_temp = round(total/number_of_days,2)
print("Average of temperature", average_of_temp)