#From given list create separate lists of strings and numbers.
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

strings = []
integers = []
for val in gadgets:
    if isinstance(val, str):
        strings.append(val)
    else:
        integers.append(val)
print(strings)
print(integers)
