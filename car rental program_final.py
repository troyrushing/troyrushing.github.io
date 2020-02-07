import sys

# get customer rental code input and save as variable
# updated with new more detailed question and leading \n to clean up code look/feel
# added .upper() to make the selection non-case sensative as an additional enhancement
# added for loop to handle invalid selections and limit the invalid selections to 5 before exit
# added failure handling and program exit for invalid selections
# added failure handling to ensure the rentalPeriod is numeric
# this failure handling falls with the limit 5 retry and exit loop, so it will also exit after 5 failed atempts.
# cleaned up printed messages to include leading and trailing \n to make the code more visually appealing

print("\n*** Welcome to Rushing's Rentals ***")

for retry in range(5):
  rentalCode = input("What type of rental would you like?\n(B)udget, (D)aily, or (W)eekly?\n").upper()
  
  if rentalCode == "W":
    rentalPeriod = input("\nEnter number of Weeks Rented:\n")
    if rentalPeriod.isdigit():
      rentalPeriod = int(rentalPeriod)
      break
    else:
      print("\nYou did not enter a number. Please try again.")
        
  elif rentalCode == "B":
    rentalPeriod = input("\nEnter number of Days Rented:\n")
    if rentalPeriod.isdigit():
      rentalPeriod = int(rentalPeriod)
      break  
    else:
      print("\nYou did not enter a number. Please try again.")
        
  elif rentalCode == "D":
    rentalPeriod = input("\nEnter number of Days Rented:\n")
    if rentalPeriod.isdigit():
      rentalPeriod = int(rentalPeriod)
      break  
    else:
      print("\nYou did not enter a number. Please try again.")
        
  else:
    print ("\nYou have made an invalid choice.")
  
else:
  print ("You have made too many invalid choices. Exiting program.")
  exit()

#*** This is the start of Milestone 3 content ***

# failure handling to avoid zero division in future calculations 
if rentalPeriod == 0:
  print("\nYou entered a rental period of zero.")
  print("This means no rental has occured.")
  print("We at Rushing's Rentals look forward to meeting your future rental needs.")
  print("Have a great day!\n")
  exit()
  
# get starting odometer reading and save as variable
# add while loop for failure handling to ensure numeric value is entered
while True:
  odoStart = input("\nEnter starting Odometer Reading:\n")
  if odoStart.isdigit():
    odoStart = int(odoStart)
    break
  else:
    print("\nYou did not enter a number. Please try again.")
    continue

# get ending odometer reading and save as variable
# add while loop for failure handling to ensure numeric value is entered
while True:
  odoEnd = input("\nEnter ending Odometer Reading:\n")
  if odoEnd.isdigit():
    odoEnd = int(odoEnd)
    break
  else:
    print("\nYou did not enter a number. Please try again.")
    continue


# create totalMiles variable
totalMiles = odoEnd - odoStart

# charge amount provided
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00	

# created list of all valid selections.
validSelection = ["B", "D", "W"
                 ]
#created x variable to be used in following while loop
x = rentalCode

# created while loop to define base charge for each valid selection in validSelection list
while x in validSelection:
  # use if/elif/else logic to calculate baseCharge
  if x == "B":
    baseCharge = rentalPeriod * budgetCharge
    break
  elif x == "D":
    baseCharge = rentalPeriod * dailyCharge
    break
  else:
    baseCharge = rentalPeriod * weeklyCharge
    break


# created nested if/elif/else logic used to calculate additional mileage charge 
if rentalCode == "B":
  mileCharge = "%.2f" % (totalMiles * 0.25)

elif rentalCode == "D":
  averageDayMiles = float(totalMiles / rentalPeriod) #create averageDayMiles variable and make it a float 
  if averageDayMiles < 101:
    extraMiles = 0
  else:
    extraMiles = averageDayMiles - 100.00
  mileCharge = "%.2f" % (extraMiles * 0.25)

else:
  averageWeekMiles = float(totalMiles / rentalPeriod)
  if averageWeekMiles > 900:
    extraMiles = 100.00
    mileCharge = extraMiles
  else:
    extraMiles = 0.00
    mileCharge = extraMiles


# created while loop with nested if/else logic to determine whether or not to add a fuel charge 
while True:
  fuelCode = input("\nWas the vehicle returned with a full tank of fuel?\nPlease enter (Y)es or (N)o.\n").upper()
  if fuelCode == "Y":
    fuelCharge = 0.00
    break
  elif fuelCode == "N":
    fuelCharge = 50.00
    break
  else:
    print("\nYou made an invalid choice. Please enter 'Y' for YES or 'N' for NO.")
    continue
    

# convert charges to float for next calculation/amount variable creation
mileCharge = float(mileCharge)
baseCharge = float(baseCharge)

# create subTotal, tax, and amoutDue variables
subTotal = (mileCharge + baseCharge + fuelCharge)
tax1 = (subTotal * 0.1)
tax2 = (subTotal * 0.08)
amountDue = (subTotal + tax1 + tax2)

#convert differnt charges and amounts to 2 decimal float for proper display in summary
baseCharge = "%.2f" % (baseCharge)
mileCharge = "%.2f" % (mileCharge)
fuelCharge = "%.2f" % (fuelCharge)
tax1 = "%.2f" % (tax1)
tax2 = "%.2f" % (tax2)
amountDue = "%.2f" % (amountDue)


# print summary with additional spacing to match required format
# added starting odo, ending odo, miles driven, base charge, mileage charge, fuel charge, and tax fields for more detailed itemization
print("\nRental Summary")
print("Rental Code:        " + rentalCode)
print("Rental Period:      " + str(rentalPeriod)) #deleted extra space on rental period to properly align summary printout
print("Starting Odometer:  " + str(odoStart))
print("Ending Odometer:    " + str(odoEnd))
print("Miles Driven:       " + str(totalMiles))
print("Base Charge:        $" + str(baseCharge))
print("Mileage Charge:     $" + str(mileCharge))
print("Fuel Charge:        $" + str(fuelCharge))
print("10% Tourist Tax:    $" + str(tax1))
print("8% State/Local Tax: $" + str(tax2))
print("Amount Due:         $" + str(amountDue))
print("\nThank you for choosing Rushing's Rentals!")
print("Have a great day!\n")