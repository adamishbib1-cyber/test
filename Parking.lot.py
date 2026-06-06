parking_list_level_1 = ["toyota", "honda", "ford", "chevrolet", "nissan"]
parking_list_level_2 = ["bmw", "mercedes", "audi", "volkswagen", "subaru"]
parking_list_level_3 = ["lexus", "infiniti", "acura", "jaguar", "land rover"]
parking_list_level_4 = ["tesla", "nissan", "hyundai", "kia", "suzuki"]
parking_list_level_5 = ["mazda", "mitsubishi", "toyota", "honda", "ford"]
parking_prices_level_1 = [1.25, 1.25, 1.25, 1.25, 1.25]
parking_prices_level_2 = [2.0, 2.0, 2.0, 2.0, 2.0]
parking_prices_level_3 = [2.5, 2.5, 2.5, 2.5, 2.5]
parking_prices_level_4 = [3.0, 3.0, 3.0, 3.0, 3.0]
parking_prices_level_5 = [3.5, 3.5, 3.5, 3.5, 3.5]
available_spots_level_1 = 20
available_spots_level_2 = 10
available_spots_level_3 = 10
available_spots_level_4 = 10
available_spots_level_5 = 10
print("Welcome to the parking lot! Please select a parking level:")
print("1. Level 1")
print("2. Level 2")
print("3. Level 3")
print("4. Level 4")
print("5. Level 5")
level = int(input("Enter the level number (1-5): "))
if level == 1:
    print("You have selected level one. The parking price is $1.25 per hour.")
    print("Available parking spots: ", available_spots_level_1)
elif level == 2:
    print("You have selected level two. The parking price is $2.00 per hour.")
    print("Available parking spots: ", available_spots_level_2)
elif level == 3:
    print("You have selected level three. The parking price is $2.50 per hour.")
    print("Available parking spots: ", available_spots_level_3) 
elif level == 4:    
    print("You have selected level four. The parking price is $3.00 per hour.")
    print("Available parking spots: ", available_spots_level_4)
elif level == 5:
    print("You have selected level five. The parking price is $3.50 per hour.")
    print("Available parking spots: ", available_spots_level_5)
else:
    print("Invalid level number. Please select a number between 1 and 5.")
calculate_price = input("Do you want to calculate the parking price? (yes/no): ")
if calculate_price.lower() == "yes":
    hours = int(input("Enter the number of hours you will be parking: "))
    if level == 1:
        total_price = hours * parking_prices_level_1[0]
        print("Total parking price: $", total_price)
    elif level == 2:
        total_price = hours * parking_prices_level_2[0]
        print("Total parking price: $", total_price)
    elif level == 3:
        total_price = hours * parking_prices_level_3[0]
        print("Total parking price: $", total_price)
    elif level == 4:
        total_price = hours * parking_prices_level_4[0]
        print("Total parking price: $", total_price)
    elif level == 5:
        total_price = hours * parking_prices_level_5[0]
        print("Total parking price: $", total_price)
else:    print("Thank you for visiting the parking lot!")



