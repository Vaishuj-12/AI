import queue as Q

def get_fn(citystr, dict_hn, dict_gn):
    cities = citystr.split(" , ")
    gn = sum(dict_gn[cities[i]][cities[i + 1]] for i in range(len(cities) - 1))
    hn = dict_hn[cities[-1]]
    return hn + gn

def expand(cityq, goal, dict_gn, dict_hn):
    visited = set()
    
    while not cityq.empty():
        tot, citystr, thiscity = cityq.get()
        
        if thiscity == goal:
            return citystr + f" : : {tot}"
        
        if thiscity not in visited:
            visited.add(thiscity)
            for cty in dict_gn.get(thiscity, {}):
                if cty not in visited:
                    next_citystr = f"{citystr} , {cty}"
                    next_tot = get_fn(next_citystr, dict_hn, dict_gn)
                    cityq.put((next_tot, next_citystr, cty))
    
    return None

def main():
    dict_hn = {}
    dict_gn = {}

    for i in range(int(input("Enter the number of cities: "))):
        city = input(f"Enter city {i + 1} name: ")
        dict_hn[city] = int(input(f"Enter heuristic value for city {city}: "))
        connections = input(f"Enter connections for city {city} (e.g., B 21 D 12 E 52): ").split()
        dict_gn[city] = dict(zip(connections[::2], map(int, connections[1::2])))

    start = input("Enter the start city: ")
    goal = input("Enter the goal city: ")
    
    if start not in dict_hn or goal not in dict_hn:
        print("Invalid start or goal city.")
        return
    
    cityq = Q.PriorityQueue()
    cityq.put((get_fn(start, dict_hn, dict_gn), start, start))
    
    result = expand(cityq, goal, dict_gn, dict_hn)

    if result:
        print("The A* path with the total is:")
        print(result)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
