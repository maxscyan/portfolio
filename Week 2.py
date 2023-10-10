# Programming portfolio tasks week 2

# First task
def name_input():
    name = str(input("What is your name?\n"))
    print(f"Hello {name}. Good to meet you!")


# Second task
# Celsius to Farenheit
def temperature():
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (9 / 5) * celsius + 32
    print(f"{celsius}C is equivalent to {fahrenheit}F")


# Third task
# Calculating student groups
def student_groups():
    group_size = int(input("How many students make a group?\n"))
    students = int(input("How many students need to be grouped?\n"))
    groups = students // group_size
    rem = students % group_size
    print(f"There will be {groups} with {rem} students left over.")


# Fourth task
# Sweets task
def sweets():
    pupils = int(input("How many pupils will attend today?\n"))
    sweets_count = int(input("How many sweets will be given?\n"))
    sweets_per_student = sweets_count // pupils
    rem = sweets_count % pupils
    print(f"Each student will have {sweets_per_student} sweets. There will be {rem} sweets left over.")


