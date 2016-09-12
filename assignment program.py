"""GitHub Link: https://github.com/thomashodgkin/CP1404-Assignment-1"""


menu = "\nmenu:\n(R) - list required items\n(C) - list completed items\n(A) - add new item\n(M) - mark an item as completed\n(Q) - quit"

def main():
#Opens and reads file
    items_file = open('items.csv','w+')
    items_data = items_file.readlines()
    required_items_details = []
    completed_items_details = []
#Filter data from file into two list
    for items_line in items_data:
        if "r" in items_line:
            item = items_line.strip().split(",")
            required_items_details.append(item)
        else:
            item = items_line.strip().split(",")
            completed_items_details.append(item)
    print(required_items_details)
#welcome message and menu
    print('welcome to shopping list 1.0')
    print('Written by Thomas Hodgkin')
    print(menu)

    choice = input('>>> ').upper()
    while choice != "Q":
#Shows require items to user
        if choice == "R":
            for item in required_items_details:
                print('{} {:.,2f} {} {}\n'.format(required_items_details))
            choice = input('>>> ').upper()
 #shows completed items to users or returns error message if there are none
        elif choice == "C":
            if completed_items_details != "":
                for item in completed_items_details:
                    print("{} ${:,.2f} ({})".format(completed_items_details, completed_items_details,completed_items_details))
                choice = input('>>> ').upper()
            else:
                print("No completed items")
                choice = input('>>> ').upper()
#ask user for item details and appendthem to requrie item list
        elif choice == "A":
            added_item_details = []
            item_details = input("enter item details")
            added_item_details.append(item_details)
            required_items_details.append(added_item_details)
            print(required_items_details)

            choice = input('>>> ').upper()
            # show requrie items that can be mark as completed and total number items and price
        elif choice == "M":
            for item in required_items_details:
                print(required_items_details)
            number_of_items = len(required_items_details)
            total_price_of_items = sum(required_items_details)
            print("Total Number of items {} and Total Price {:.,2f}".format(number_of_items,total_price_of_items))
            choice = input('>>> ').upper()
#Exits program
        elif choice == "Q":
            print("goodbye")
            items_data.append(required_items_details)
            items_data.append(completed_items_details)
            items_file.write(items_data)
            items_file.close()
#error check for choice
        else:
            print('Invalid choice')
            print(menu)
            choice = input('>>> ').upper()











main()