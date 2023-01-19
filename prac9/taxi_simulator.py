from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


if __name__ == '__main__':
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0
    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        input_value = input(">>> ")[0].lower()
        if input_value not in ['q', 'c', 'd']:
            print("Invalid option")
            print("Bill to date: $%.02f" % bill)
            continue
        if input_value == 'q':
            print("Total trip cost: $%.02f" % bill)
            print("Taxis are now:")
            for index, taxi in enumerate(taxis):
                print("%d - %s" % (index, taxi))
            break
        if input_value == 'c':
            print("Taxis available: ")
            for index, taxi in enumerate(taxis):
                print("%d - %s" % (index, taxi))
            Choose_taxi = int(input("Choose taxi: "))
            if 0 <= Choose_taxi < len(taxis):
                current_taxi = taxis[Choose_taxi]
            else:
                print("Invalid taxi choice")
            print("Bill to date: $%.02f" % bill)
            continue
        if input_value == 'd':
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
                print("Bill to date: $%.02f" % bill)
                continue
            drive_far = int(input("Drive how far? "))
            # print(current_taxi)
            current_taxi.start_fare()
            current_taxi.drive(drive_far)
            print("Your %s trip cost you $%.02f" % (current_taxi.name, current_taxi.get_fare()))
            bill += current_taxi.get_fare()
            print("Bill to date: $%.02f" % bill)
            continue



