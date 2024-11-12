print("******** Parking Lot ********")
a = input("Enter max of car,car in soi,operation : ").split()
max_cars = int(a[0])
cars_in_soi = a[1].split(",")

if cars_in_soi == ['0']:
    cars_in_soi = []

operation = a[2]
car = a[3]

if operation == "arrive":
    if len(cars_in_soi) < max_cars and car not in cars_in_soi:
        print(f"car {car} arrive! : Add Car {car}")
        cars_in_soi.append(car)
    elif len(cars_in_soi) >= max_cars:
        print(f"car {car} cannot arrive : Soi Full")
    elif car in cars_in_soi:
        print(f"car {car} already in soi")
elif operation == "depart":
    if not cars_in_soi:
        print(f"car {car} cannot depart : Soi Empty")
    elif car not in cars_in_soi:
        print(f"car {car} cannot depart : Dont Have Car {car}")
    else:
        print(f"car {car} depart ! : Car {car} was remove")
        cars_in_soi.remove(car)

if not cars_in_soi:
    print([])
else:
    print([eval(i) for i in cars_in_soi])