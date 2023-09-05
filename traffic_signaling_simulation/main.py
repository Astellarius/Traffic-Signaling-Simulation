
class Street:
    def __init__(self, begin, end, name, travel_time) -> None:
        self.begin_intersection: Intersection = begin
        self.end_intersection: Intersection = end
        self.name: str = name
        self.travel_time: int = travel_time
    
    def __str__(self):
        street_name = f"Street Name: {self.name}\n"
        travel_time = f"Travel Time: {self.travel_time}\n"
        begin_intersection = f"Begin Intersection: {self.begin_intersection.intersection_id}\n"
        end_intersection = f"End Intersection: {self.end_intersection.intersection_id}\n"

        return street_name + travel_time + begin_intersection + end_intersection


class Intersection:
    def __init__(self, intersection_id) -> None:
        self.intersection_id: int = intersection_id
        self.streets_entering: list[Street] = []
        self.streets_exiting: list[Street] = []
    
    def __str__(self):
        intersection_id = f"Intersection ID: {self.intersection_id} \n"
        entering_streets_str = ', '.join([street.name for street in self.streets_entering])
        entering_streets = f"Entering Streets: {entering_streets_str} \n"
        exiting_streets_str = ', '.join([street.name for street in self.streets_exiting])
        exiting_streets = f"Exiting Streets: {exiting_streets_str} \n"

        return intersection_id + entering_streets + exiting_streets

class Car:
    def __init__(self, car_id, list_of_streets) -> None:
        self.car_id: int = car_id
        self.path: list[Street] = list_of_streets
        self.current_path_street_index: int = 0

    def __str__(self):
        street_names = ""
        for street in self.path:
            street_names += street.name + " "

        car_id = f"Car ID: {self.car_id}, \n"
        car_path = f"Car Path: {street_names}, \n"
        current_street = f"Car Current Street: {self.path[self.current_path_street_index].name} \n"

        return car_id + car_path + current_street

# list_of_streets: list[Street] = []
street_name_to_street: dict[str, Street] = dict()

list_of_cars: list[Car] = []
list_of_intersections: list[Intersection] = []

duration_of_simulation = 0
number_of_intersections = 0
number_of_streets = 0
number_of_cars = 0
bonus_points = 0

file: str = "inputs/a.txt"

with open(file, "r") as input_file:
    firstline: str = input_file.readline() 

    firstline = firstline.strip() # clean string
    firstline_strings: list[str] = firstline.split(" ") # split string
    firstline_integers: list[int] = [int(x) for x in firstline_strings] # convert to int 

    duration_of_simulation = firstline_integers[0]
    number_of_intersections = firstline_integers[1]
    number_of_streets = firstline_integers[2]
    number_of_cars = firstline_integers[3]
    bonus_points = firstline_integers[4]

    print("duration_of_simulation: ", duration_of_simulation)
    print("number_of_intersections: ", number_of_intersections)
    print("number_of_streets: ", number_of_streets)
    print("number_of_cars: ", number_of_cars)
    print("bonus_points: ", bonus_points)

    # init all intersections
    for intersection_id in range(number_of_intersections):
        intersection = Intersection(intersection_id)
        list_of_intersections.append(intersection)

    # init streets 
    for street in range(number_of_streets):
        street_line: str = input_file.readline()
        street_line = street_line.strip()
        street_line_list = street_line.split(" ")

        begin_intersection: int = int(street_line_list[0])
        end_intersection: int = int(street_line_list[1])
        street_name: str = street_line_list[2]
        street_travel_time:int = int(street_line_list[3])

        print("begin_intersection: ", begin_intersection)
        print("end_intersection: ", end_intersection)
        print("street_name: ", street_name)
        print("street_travel_time: ", street_travel_time)

        # make the street 
        street = Street(
            list_of_intersections[begin_intersection],
            list_of_intersections[end_intersection],
            street_name,
            street_travel_time
        )

        # list_of_streets.append(street)
        street_name_to_street[street_name] = street

        list_of_intersections[end_intersection].streets_entering.append(street)
        list_of_intersections[begin_intersection].streets_exiting.append(street)

    # init cars 
    for car_id in range(number_of_cars):
        car_line: str = input_file.readline()
        car_line = car_line.strip()
        car_line_list = car_line.split(" ")

        streets_to_travel: int = int(car_line_list[0])
        names_of_streets: list[str] = car_line_list[1:]

        print("streets_to_travel: ", streets_to_travel)
        print("names_of_streets: ", names_of_streets)

        streets: list[Street] = []
        for street_name in names_of_streets:
            street = street_name_to_street[street_name]
            streets.append(street)

        car = Car(car_id, streets)
        list_of_cars.append(car)




for street in street_name_to_street.values():
    print(street)


for car in list_of_cars:
    print(car)

for intersection in list_of_intersections:
    print(intersection)


intersection_schedules = []
for intersection in list_of_intersections:
    intersection_id = intersection.intersection_id
    intersection_street_schedules = []

    for entering_street in intersection.streets_entering:
        street_name = entering_street.name
        time_green = 1
        street_schedule = (street_name, time_green)

        intersection_street_schedules.append(street_schedule)

    intersection_schedule = (intersection_id, intersection_street_schedules)
    intersection_schedules.append(intersection_schedule)

print("printing intersection schedules .. \n")
print(intersection_schedules)