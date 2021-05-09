################################################################

# Welcome to my DSA final project!

# by Walter Villa
################################################################

# importing only package
import math

# making data that I will need to use in the inital search:

# spots in Queens
pepsiCola = {'name': 'Pepsi Cola Sign', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'neon signs', 'x': 3, 'y': 5}
flushingMeadow = {'name': 'Unisphere - Flushing Meadows Park', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': "nature", 'x': 27, 'y': 15}
gantryStatePlaza = {'name': 'Gantry State Plaza', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'cityscape', 'x': 3, 'y': 4}
astoriaPark = {'name': 'Astoria Park', 'price': 0, 'MTA': True, 'bathroom': False, 'aesthetic': 'park', 'x': 8 , 'y': 14}

# spots in Brooklyn
dominoPark = {'name': 'Domino Park', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'cityscape', 'x': 2, 'y': -1}
brooklynBridge = {'name': 'Brooklyn Bridge', 'price': 0, 'MTA': True, 'bathroom': False, 'aesthetic': 'bridge', 'x': 2, 'y': -8}
dumbo = {'name': 'DUMBO', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'nature', 'x': 2.5, 'y': -6}
coneyIsland = {'name': 'Coney Island', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'beach', 'x': 18, 'y': -18}

# spots in Manhattan
moma = {'name': 'MoMa', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'museum', 'x': -9, 'y': 3}
# insert brooklyn bridge data here again
chinatown = {'name': 'Chinatown', 'price': 0, 'MTA': True, 'bathroom': False, 'aesthetic': 'cultural', 'x': -4, 'y': -4}
lexusEvent = {'name': 'Lexus Event', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'modern', 'x': -13, 'y': -4}
pier16 = {'name': 'Pier 16 - Two Bridges', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'pier', 'x': -5, 'y': -8}
centralPark = {'name': 'Central Park', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'nature', 'x': -10, 'y': 7}
flatiron = {'name': 'FlatIron', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'urban', 'x': -7.1, 'y': -1.9}
timesSQ = {'name': 'Times Square', 'price': 0, 'MTA': True, 'bathroom': False, 'aesthetic': 'urban', 'x': -12, 'y': 2.8}
vessel = {'name': 'The Vessel', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'urban', 'x': 14.8, 'y': -1.8}
# spots in the Bronx
bronxZoo = {'name': 'Bronx Zoo', 'price': 0, 'MTA': True, 'bathroom': True, 'aesthetic': 'animals', 'x': -2, 'y': 18}


spots_dictionary = {
    "Queens": [pepsiCola, flushingMeadow, gantryStatePlaza, astoriaPark],
    "Manhattan": [moma, chinatown, lexusEvent, pier16, centralPark, flatiron, timesSQ, vessel],
    "Brooklyn": [dumbo, brooklynBridge, dominoPark, coneyIsland],
    "Bronx": [bronxZoo],
    "Staten Island": []
}

def getBoroLocations(f):
    # Gives the corresponding list of locations to look at
    """
    Finds the list of locations from the 'spots dictionary' that has the list of locations in lists. 
    Input:
        f: type 'string' --> string of one of the 5 boroughs.
    Returns: 
        list_of_locations: type 'list' --> list of all the spots in a certain borough.
    """
    list_of_locations = spots_dictionary[f]
    return list_of_locations
    
def filterSpots(location, features):
    """
    Matching algorithm/filter query used to match user with spots based off of their input.
    Parameters:
        location: type 'string' --> location of what borough to look at (this narrows down the search)
        features: type 'list' of 'sets' --> features of what the user is looking for based off of properties that each spot has. 
    Returns: 
        validSpots: type 'list' --> list of potential spots as dictionaries (must call validSpots['name] for the name of the spot).
    """
    # validspot_bin = []
    count = 0 
    locations = getBoroLocations(location)
    lenFeatures = len(features)
    global validSpots 
    validSpots = []
    for spot in locations:
        for i in range(lenFeatures):
            if spot[features[i][0]] == features[i][1]:
                count += 1
        if count == lenFeatures:
            validSpots.append(spot)
        count = 0 
    return validSpots

def calculateDistance(x1, y1, x2, y2):
    """
    Function that finds the Euclidean distance between two locations:
    Parameters:
        x1: x coordinate for location 1
        y1: y coordinate for location 1
        x2: x coordinate for location 2
        y2: y coordinate for location 2
    Returns:
        Euclidean distance as a float.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def optimizeTravelDistance(validSpots, bikeRange, local):
    """
    Optimization algorithm that finds the shortest path that maximizes the number of
    locations while minimizing the distance taken given a certain boundary of range on e-bike.
    Parameters: 
        validSpots: 
        bikeRange: type 'int' --> the bikeRange specified by the user.

    """
    # defining variables
    validspot_count = len(validSpots)       # number of spots that are valid. 
    total_distance = 0                      # keeps track of the total distance throughout each iteration of the path
    min_distance = 0                        # place to store the minimum distance of each row
    location_index = 0                      # location of minimum distance 
    visited = []                            # list of visited locations 'nodes' 
    index_path = []                         # list of indices that make up the path.
    start_index_location = []               # list that keeps track of the start indices 
    current_shortest_path = [[], math.inf]  # sets the initial "current shortest path" to an empty list and its distance + infinity
    
    start_index = 0                         # starting at your current location
    # this is a combination of the location and the spots after the filter
    nodeList = [local] + validSpots # this is your current location + the other matched spots.
    len_NL = len(nodeList)

    # Your location is at 0,0 in the Adjacency Matrix

    # base case 
    if validspot_count == 0:
        print("You have no locations to visit. Sorry.")
        return 0
    if validspot_count == 1:
        total_distance += math.ceil(2 * calculateDistance(validSpots[0]['x'], validSpots[0]['y'], local['x'], local['y']))    
        print('The total distance traveled would be ' + str(total_distance) + ' miles.')
        print('You can travel to '+ validSpots[0]['name'] +  ".")
        return validTravel(bikeRange, total_distance)
    
    # setting up adjacency matrix
    rows, cols = (len_NL, len_NL)
    matrix = []
     # add the distance of current location and each location (not between the spots)
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(calculateDistance(nodeList[i]['x'], nodeList[i]['y'], nodeList[j]['x'], nodeList[j]['y']))
        matrix.append(col)
    
    # ^this *successfully* puts all of the distances in an adjacency matrix
    
    # -- DEBUGGING -- This prints out the locations in one row of the 'nodeList'  
        # for i in range(len_NL):
        #     print(nodeList[i]['name'])
        
    # lets assume that the 2D matrix is complete...
    # print(matrix)     --> This will print out the adjacency matrix with distances from all locations

    destinations = []   # final list of destinations (from the 'current_shortest_path' index list)
    r = 0               # number of rotations
    while (r < len_NL - 1):
    #  I want to get the algorithm to repeat this as many times as it needs for the filtered locations
        # resetting variables for the new sequence
        index_path = []
        visited= []
        total_distance = 0
        # intilizing variables to control where I look for indices + keep track of trial #
        i = 0   # indexing the row in which I am to check for the smallest distance. 
        t = 0   # number of trials within a single rotation
        while (i < len_NL and t < len_NL - 1):  
            # print(i, t)
            # i can manipulate to match with row indexing and have t just count for # of trials
            if t == 0:
                min_distance = min(matrix[i][j] for j in range(len_NL) if matrix[i][j] != 0 and j not in index_path and j != 0 and j not in start_index_location)
            if t > 0:
                min_distance = min(matrix[i][j] for j in range(len_NL) if matrix[i][j] != 0 and j not in index_path and j != 0 and j != start_index) #not in start_index_location  
            location_index = matrix[i].index(min_distance)
            # print(location_index)
            if t == 0:
                start_index_location.append(location_index)
                start_index = location_index

            # add to the total distance traversed
            total_distance += min_distance

            # check if the distance from the next "min" spot to home will be enough
            if matrix[0][location_index] + total_distance <= bikeRange and nodeList[location_index]['name'] not in visited:
                visited.append(nodeList[location_index]['name'])
                index_path.append(location_index)
                # print(visited)
                # print(index_path)                                   # this will account for certain paths being taken
            else:
                # this else statement is meant for when there is no more available range on the Super73
                print("it broke")
                print(start_index)
                break
            i = location_index
            t+=1
 
        # checking to see if this is the current shortest path logged in the "shortest path variable" 
        if current_shortest_path[1] > total_distance:
            current_shortest_path[0] = index_path
            current_shortest_path[1] = total_distance
        
        # -- DEBUGGING -- This prints out updates when one certain 'path' is traversed.
        # print(current_shortest_path[0], current_shortest_path[1])
        # print(index_path, start_index_location)

        r += 1                      # increments the location search by 1.
    
    # add the names of the location indices to a final 'destinations' list. 
    for x in range(len(current_shortest_path[0])):
        destinations.append(nodeList[current_shortest_path[0][x]]['name'])
    print("The shortest path to take is: ")
    print(destinations)
    print("With this shortest path, you would have only used " + str(total_distance) + " miles, which is the shortest path.")
    return destinations



def validTravel(bikeRange, distance):
    """
    This function checks for base cases to see if travel is valid. 
    """
    if distance > bikeRange:
        print("You have exceeded the mileage on the Super73. Travel not possible")
        return False
    if distance <= bikeRange:
        remainingDistance = bikeRange - distance
        print("This is a valid route to take with " + str(remainingDistance) + " miles left on the Super73.")
        return True


def goatsAlgo(location, features, bikeRange, local):
    """
    Main function run. 

    Parameters: 
        location: type 'string' --> Borough in which to search location
        features: type 'list of sets' --> List of sets that contain preferences 
        bikeRange: type 'int' --> Range that the e-bike has
        local: type 'hash map' --> Dictionary of current location that has current location and x and y coordinate.
    """
    narrowList = filterSpots(location, features)
    optimizeTravelDistance(narrowList, bikeRange, local)

# user inputs
input_features = [('bathroom', True), ('price', 1)]
input_features1 = [('bathroom', True), ('price', 0), ('aesthetic', 'nature')]
local = {'name': 'Current Location', 'x': 0, 'y':0}
bikeRange = 70                                                                                         

goatsAlgo("Queens", input_features, bikeRange, local)

