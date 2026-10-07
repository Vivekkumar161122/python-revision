# Challange: Create the output display for the PayUp app.

# 1. Check out the example output in 'example_output.md' 
# 2. Define a variable for each item:  event name, cost, service charge, 
#  group size, grand total and total person. Use made-up values for now -
#  we'll do the math later!
# 3. Build the display line by line by line using print() and f-strings.
# Remember: an empty print() creates a balnk line. 
# 4. Run it and make sure it matches the example. 


event = "dinner at Fantastic Pizza"
cost = 300
service_charge = 30
group_size = 3
grand_total = 330
total_per_person = 110

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for {event}: ")
print()
print(f"Cost: ${cost}")
print(f"Service charges: ${service_charge}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total}")
print()
print(f"Each person must PayUp: ${total_per_person}")
