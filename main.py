# This is my first attempt at creating a python project.
# I will create input variables, a string and call those variables.

name = input("Name: ")
adjective = input("Adjective: ")
noun = input("Plural Noun: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
adjective2 = input("Adjective: ")

madlib = (f"Welcome to Portland, Oregon {name}! I hope you are ready for the {adjective} "
            f"culture you are going to take in. There are mountains and {noun}. "
            f"You can hike, {verb}ing, and bike all over the city. Make sure to not "
            f"miss out on the opportunities to {verb2} around our {adjective2} city.")

print(madlib)