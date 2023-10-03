# Programming portfolio tasks week 1

# First task
def hello_world():
    print("Hello World"

          )

# Second task
def hello_max():
    print("Hello Max")

# Third task
# Celsius to farenheit
def convert_c_to_f():
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"The temperature is {fahrenheit} degrees Fahrenheit, which is {celsius} degrees!")

# Fourth task
# Calculating batting average of Geoffery Boycott
def batting_average():
    batted = 1014
    not_out = 162
    matches = 609
    runs = 48426
    completed_innings = batted - not_out
    batting_average = runs / completed_innings
    print(f"The batting average of Geoffery Boycott is {batting_average}")

# Fifth task
# Calculating student groups
def student_groups():
    group_size = 24
    valid = False
    while not valid:
        students = input("How many students need to be grouped?\n")
        if students.isalnum():
            valid = True
        else:
            pass
    students = int(students)
    groups = students // group_size
    rem = students % group_size
    print(f"{students} were able to fit into {groups} groups, and {rem} were left over.")

student_groups()