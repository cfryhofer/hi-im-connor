#Connor Fryhofer Student ID 1853826


import csv

from datetime import datetime


class OutputInventory:
    # Class for output inventory files from input
    def __init__(self, item_list):
        '''
        These are all the items
        '''
        self.item_list = item_list

    def full(self):
        '''
        This makes it to where an inventory is entirely created through alphabetical order and will include item id, item type, price, manufacturer name, service date, and damaged. All onto a csv file.
        '''
        with open('./output_files/FullInventory.csv', 'w') as file:
            items = self.item_list
            # get order of keys to write to file based on manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def by_type(self):
        '''
        This makes it to where items will get sorted by the item ID, one item on each row of file, and creates csv output files.
        '''
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('./output_files/' + file_name, 'w') as file:
                for item in keys:
                    id = item
                    man_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))

    def past_service(self):
        '''
        This makes it to where an output file will be created for the items that are expired. Oldest to most recent with one item on each row.
        '''
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(),
                      reverse=True)
        with open('./output_files/PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def damaged(self):
        '''
        Output files will be created for any damaged items from most to least expensive, one item on each row.
        '''
        items = self.item_list
        # get order of keys to write to file based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('./output_files/DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))


if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    inventory = OutputInventory(items)
    # Create all the output files
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()

    # Get the different manufacturers and types in a list
    types = []
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)

    # Prompt the user for input
    user_input = None
    while user_input != 'q':
        user_input = input(
            "\nPlease enter an item manufacturer and item type (ex: Lenovo laptop) or enter 'q' to quit:\n")
        if user_input == 'q':
            break
        else:
            # Check each word from user to see if there is a match in manufacturer and item type
            selected_manufacturer = None
            selected_type = None
            user_input = user_input.split()

            print("manufacturers: ", manufacturers)
            print("types: ", types)
            print("user input", user_input)
            for word in user_input:
                if word in manufacturers:
                    selected_manufacturer = word
                elif word in types:
                    selected_type = word

            print("selected_manufacturer: ", selected_manufacturer)
            print("selected_type: ", selected_type)
            print("selected_manufacturer and selected_type", (selected_manufacturer != None and selected_type != None))

            if (selected_manufacturer != None and selected_type != None):
                # Ordered list of keys to iterate through based on highest price first
                keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

                # Get the matching list of items based on user input
                matching_items = []

                # Store items with same type but different manufacturer
                # - item type must match
                # - item must be in inventory and not damaged or past service
                similar_items = {}
                for item in keys:
                    if items[item]['item_type'] == selected_type:
                        # Don't add damaged items or past service to matched list or similar list
                        today = datetime.now().date()
                        service_date = items[item]['service_date']
                        service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                        expired = service_expiration < today
                        if items[item]['manufacturer'] == selected_manufacturer:
                            if not expired and not items[item]['damaged']:
                                matching_items.append((item, items[item]))
                        else:
                            if not expired and not items[item]['damaged']:
                                similar_items[item] = items[item]

                # Output the item if matched
                if matching_items:
                    item = matching_items[0]
                    item_id = item[0]
                    man_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']
                    print("Your item is: {}, {}, {}, {}\n".format(item_id, man_name, item_type, price))

                    # Output item from different manufacturer that is closest in price to matched item
                    if similar_items:
                        matched_price = price
                        # Get the similar item with the closest price to the initial item
                        closest_item = None
                        closest_price_diff = None
                        for item in similar_items:
                            if closest_price_diff == None:
                                closest_item = similar_items[item]
                                closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < closest_price_diff:
                                closest_item = item
                                closest_price_diff = price_diff
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, man_name, item_type, price))

            else:
                print("Inventory doesn't have this item")
