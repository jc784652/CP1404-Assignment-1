


menu = "\nmenu:\n(R) - list required items\n(C) - list completed items\n(A) - add new item\n(M) - mark an item as completed\n(Q) - quit"

def main():
    items_file = open('items.csv', 'r')
    items_data = items_file.readlines()
    required_items_details = []
    completed_items_details = []

    for items_line in items_data:
        if "r" in items_line:
            item = items_line.strip().split(",")
            required_items_details.append(item)
        else:
            item = items_line.strip().split(",")
            completed_items_details.append(item)
    print(required_items_details)

    print('welcome to shopping list 1.0')
    print('Written by Thomas Hodgkin')
    print(menu)

    choice = input('>>> ').upper()
    while choice != "Q":
        if choice == "R":
            for item in required_items_details:
                print('{} {:.,2f} {} {}\n'.format(required_items_details))
            choice = input('>>> ').upper()
        elif choice == "C":
            if completed_items_details != "":
                for item in completed_items_details:
                    print("{} ${:,.2f} ({})".format(completed_items_details, completed_items_details,completed_items_details))
                choice = input('>>> ').upper()
            else:
                print("No completed items")
                choice = input('>>> ').upper()
        elif choice == "A":
            added_item_details = []
            item_details = input("enter item details")
            added_item_details.append(item_details)
            item_adding = True
            print(added_item_details)
            required_items_details.append(added_item_details)
            print(required_items_details)

            choice = input('>>> ').upper()
        elif choice == "M":
            for item in required_items_details:
                print(required_items_details)
            number_of_items = len(required_items_details)
            total_price_of_items = sum(required_items_details)
            print("Total Number of items {} and Total Price {:.,2f}".format(number_of_items,total_price_of_items))
            choice = input('>>> ').upper()
        elif choice == "Q":
            print("goodbye")
        else:
            print('Invalid choice')
            print(menu)
            choice = input('>>> ').upper()











main()