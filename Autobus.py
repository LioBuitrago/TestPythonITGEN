class Autobus:
    def __init__(self, route, star_point, destination_point, time):
        self.route = route
        self.start_point = star_point
        self.destination_point = destination_point
        self.time = time

    def info(self):
        print("Route number:" + self.route)
        print("Starting point:" + self.start_point)
        print("Destination point:" + self.destination_point)
        print("Time:" + self.time)
    
    def set_route(self):
        setter = self.route = input()
        return setter
    def get_route(self):
        return self.route
    def set_start_point(self):
        setter = self.start_point = input()
        return setter
    def get_start_point(self):
        return self.start_point
    def set_destination_point(self):
        setter = self.destination_point = input()
        return setter
    def get_destination_point(self):
        return self.destination_point
    def set_time(self):
        setter = self.time = input()
        return setter
    def get_time(self):
        return self.time

def create_autopark():
    n = int(input("Enter the number of busses: "))
    for i in range(n):
        print("---------------------------------------input")
        r = input("Enter the route of %d bus: " %(i+1))
        s = input("Enter the starting point of %d bus: " %(i+1))
        d = input("Enter the destination point of %d bus: " %(i+1))
        t = input("Enter the travel time of %d bus: " %(i+1))
        print("-------------------------------------------")
        buses.append(Autobus(r,s,d,t))

def show_autopark():
    for obj in buses:
        print("---------------------------------------show")
        print("Route number: " + obj.route)
        print("Starting point: " + obj.start_point)
        print("Destination point: "+ obj.destination_point)
        print("Time: "+ obj.time)
        print("-------------------------------------------")

def sort_by_number():
    sorting = sorted(buses, key=lambda x: x.route, reverse=True)
    for obj in sorting:
        print("-------------------------------------sorted")
        print("Route number: " + obj.route)
        print("Starting point: " + obj.start_point)
        print("Destination point: "+ obj.destination_point)
        print("Time: "+ obj.time)
        print("-------------------------------------------")
def search_by_point(point):
    for x in buses:
        if x.start_point == point:
            print("--------------------------------------found")
            print("Route number: " + x.route)
            print("Starting point: " + x.start_point)
            print("Destination point: "+ x.destination_point)
            print("Time: "+ x.time)
            print("-------------------------------------------")
        elif x.destination_point == point:
            print("--------------------------------------found")
            print("Route number: " + x.route)
            print("Starting point: " + x.start_point)
            print("Destination point: "+ x.destination_point)
            print("Time: "+ x.time)
            print("-------------------------------------------")
    else:
        x = None

buses = []

create_autopark()
show_autopark()
sort_by_number()
point = input()
search_by_point(point)