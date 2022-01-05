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

# Done, I tried my best :)


def max_product(nums):
    length = len(nums)
    negative_num = 0
    new_list = []
    for num in nums:  # check if there is negative num
        if num < 0:
            negative_num += 1
        if negative_num > 2:  # if negative num > 2, there is no reason to check
            break

    while length > 1:
        if negative_num < 2:  # if there is no negative num, use bubble sort
            for i in range(length - 1):
                if nums[i] > nums[i+1]:
                    hold = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = hold
        else:
            for i in range(length - 1):
                if i+1 < length-1:
                    total = nums[i]*nums[i+1]
                    new_list.append(total)
            return max(new_list)

        length -= 1
    return nums[-1]*nums[-2]


print(max_product([5, 20, 2, 6]))
print(max_product([10, -20, 0, 3]))
print(max_product([-1, 2]))
print(max_product([-1, 0, 2]))
print(max_product([-1, -2, 0]))


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

