import random
import math
from copy import deepcopy


def main():
    random.seed(int(input("SEED")))
    cars = int(input("CAR"))

    problem_number = int(input("CITY"))
    if cars >= problem_number or cars <= 0 or problem_number <= 0:
        print("Error!!!! \n Exit program.")
        return
    problem = []
    for _ in range(problem_number):
        problem.append([random.randint(1, 500), random.randint(1, 500)])

    problem_distances = {}
    for x in range(len(problem)):
        for y in range(len(problem)):
            problem_distances[(y, x)] = abs(problem[y][1] - problem[x][1]) + (
            abs(problem[y][0] - problem[x][0]))

    car_routes = create_car_routes(cars, problem_distances, problem)
    print(neighbor_search(car_routes, problem_distances, int(input("ITERATIONS"))))


def create_car_routes(cars, problem_disctances, problem):
    tabu = []
    car_routes = [[] for i in range(cars)]
    prev = [0 for x in range(cars)]
    for i in range(cars):
        car_routes[i].append(0)
    tabu.append(0)
    car_counter = 0
    while len(problem) != len(tabu):
        position = 0
        while position in tabu:
            position = random.randint(1, len(problem) - 1)
        car_routes[car_counter].append(position)
        tabu.append(position)
        car_counter += 1
        if car_counter == cars:
            car_counter = 0
    return car_routes


def neighbor_search(car_routes, problem_distances, iterations):
    best_route = car_routes.copy()
    best_length = float("inf")

    for it in range(iterations):
        current_route = deepcopy(best_route.copy())
        current_length = 0
        x = random.randint(0, len(car_routes) - 1)
        y = random.randint(0, len(car_routes) - 1)
        if len(car_routes[x]) <2 and len(car_routes[y]) < 2:
            continue
        a = random.randint(1, len(car_routes[x]) - 1)
        b = random.randint(1, len(car_routes[y]) - 1)
        current_route[x][a], current_route[y][b] = (
            current_route[y][b], current_route[x][a],
        )
        for i in range(len(car_routes)):
            current_length += calculatecarlength(problem_distances, current_route[i])
        if current_length <= best_length:
            best_length = current_length
            best_route = current_route.copy()
            print("New good:", best_route, "\n length:", best_length)
        else:
            temp = pow(0.92, it) * 100000
            if temp == 0:
                print("New bad declined:", current_route, "\n length:", current_length)
            else:
                if random.random() < math.exp((best_length - current_length) / temp):
                    print("New bad accepted:", current_route, "\n length:", current_length)
                    best_route = current_route.copy()
                    best_length = current_length
                else:
                    print("New bad declined:", current_route, "\n length:", current_length)

    return best_route, best_length


def calculatecarlength(problem_disctances, car_routes):
    distance = 0
    prev = car_routes[0]
    for i in car_routes:
        distance += problem_disctances[(prev, i)]
        prev = i

    distance += problem_disctances[(car_routes[-1], car_routes[0])]
    return distance


if __name__ == "__main__":
    main()