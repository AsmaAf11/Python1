
# task1
def sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True



input = ["d","b","a","c","f","h","g","e"]
sort(input)
print(input)

# task2
from datetime import date, timedelta
from datetime import datetime

start_date_list = []
my_input = input("Enter the start date (day month year):").split()
for item in my_input:
    start_date_list.append(int(item))

end_date_list = []
my_input = input("Enter the end date (day month year):").split()
for item in my_input:
    end_date_list.append(int(item))


start_date = date(start_date_list[2], start_date_list[1], start_date_list[0])
end_date = date(end_date_list[2], end_date_list[1], end_date_list[0])

delta = end_date - start_date

days_number = delta.days
month_number = end_date_list[1] - start_date_list[1]
year_number = end_date_list[2] - start_date_list[2]

print("{} Year, {} Months, {} Days".format(year_number,month_number,days_number))

# task3
number = input("Enter the number: ")
seperating_number = []
for l in number:
    seperating_number.append(int(l))

result = []
for num in seperating_number:
    try:
        if int(number)%num == 0:
            result.append(True)
    except:
        pass

if len(result) == len(seperating_number):
    print("Yes")
else:
    print("NO")