print("I renamed some parameters and camel case since Pycharm is annoying")


def calculate(min_num, max_num):
    total = 0
    for num in range(min_num, max_num + 1):
        total += num
    return total


print(calculate(1, 3))
print(calculate(4, 8))


def avg(data):
    total = 0
    employees = data["employees"]
    total_employees = data["count"]
    if total_employees != len(employees):
        total_employees = len(employees)

    for employee in employees:
        total += employee["salary"]
    print(total/total_employees)


avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
})


def max_product(nums):
    new_list = []
    for num in nums:
        for num2 in nums:
            if num == num2:
                continue
            else:
                new_list.append(num*num2)
    return max(new_list)


print(max_product([5, 20, 2, 6]))
print(max_product([10, -20, 0, 3]))
print(max_product([-1, 2]))
print(max_product([-1, 0, 2]))
print(max_product([-1, -2, 0]))


def two_sum(nums, target):
    ans = []
    for num in nums:
        for num2 in nums:
            if num == num2:
                continue
            else:
                if num + num2 == target:
                    if nums.index(num) in ans:
                        continue
                    elif nums.index(num2) in ans:
                        continue
                    else:
                        ans.append(nums.index(num))
                        ans.append(nums.index(num2))
    return ans


result = two_sum([2, 11, 7, 15], 9)
print(result)


def max_zeros(nums):
    total_zero = 0
    max_zero = 0
    for num in nums:
        if num == 0:
            total_zero += 1
            if total_zero > max_zero:
                max_zero = total_zero
        else:
            total_zero = 0
    return max_zero


print(max_zeros([0, 1, 0, 0]))
print(max_zeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
print(max_zeros([1, 1, 1, 1, 1]))
print(max_zeros([0, 0, 0, 1, 1]))

print("\n====I tried to use algorithm, but only use python.====")
print("====And I didn't do the optional :( ====\n")


def max_product(nums):  # Done, I tried my best :)
    length = len(nums)
    if length > 3:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        min1 = min(nums)
        nums.remove(min1)
        min2 = min(nums)
        nums.remove(min2)
        total1 = max1*max2
        total2 = min1*min2
        if total1 > total2:
            return total1
        else:
            return total2
    elif length <= 2:
        if length == 2:
            return nums[0]*nums[1]
        else:
            return nums[0]

    else:
        new_list = []
        for i in range(length):
            for j in range(1, length-1):
                new_list.append(nums[i]*nums[j])
                return max(new_list)


print(max_product([5, 20, 2, 6]))
print(max_product([10, -20, 0, 3]))
print(max_product([-1, 2]))
print(max_product([-1, 0, 2]))
print(max_product([-1, -2, 0]))
print(max_product([-5, 1, 2, -2, 4]))


# used hashmap and didn't even know what i was f writing:(
def two_sum(nums, target):
    length = len(nums)
    dic = {}
    ans = []

    for i in range(length):  # turn list to dict
        dic[i] = nums[i]

    for index in range(length):
        num1 = target - nums[index]
        for position, number in dic.items():
            if number == num1 and position not in ans:
                ans.append(position)
        if num1 < 0 or num1 not in nums:
            continue
        else:
            num2 = target - num1
            for position, number in dic.items():
                if number == num2 and position not in ans:
                    ans.append(position)
    return ans


result = two_sum([2, 11, 7, 15], 9)
print(result)

