# Import example
# from module import chai
# chai("ginger tea")

# List operations
tea_variety = ["olongtea", "herbal", "black"]
print(tea_variety)

# Slicing
print(tea_variety[1:2])   # ['herbal']
print(tea_variety[1:3])   # ['herbal', 'black']

# Update element
tea_variety[2] = "masalatea"
print(tea_variety)

# Insert elements using slicing
tea_variety[1:1] = ['test1', 'test2']
print(tea_variety)

# Access slice
print(tea_variety[1:2])   # ['test1']

# Loop correctly
for tea in tea_variety:
    print(tea)

# Append & check
tea_variety.append("coffee")

if "coffee" in tea_variety:
    print("I have coffee")

# Remove last element
tea_variety.pop()
print(tea_variety)

# Correct list
squared_nums = [1, 2, 2, 3, 4, 4, 5]
print(squared_nums)

# Dictionary operations
dict1 = {"masala": "spicy", "ginger": "zesty", "green": "normal"}
print(dict1)

# Correct way to use get()
print(dict1.get("green"))

# Loop through dictionary
for chai in dict1:
    print(chai, ":", dict1[chai])

# Check key existence
if "masala" in dict1:
    print("Yes, I have masala")

# Dictionary comprehension
squared_num = {x: x**2 for x in range(6)}
print(squared_num)

# Clear dictionary
squared_num.clear()
print(squared_num)

# New empty dictionary
new_dict = {}
print(new_dict)
