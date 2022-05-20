import numpy as np
import copy
import time

algorithm_flag = True # Set for forward selection

def leave_one_out_validation(data, current_set, feature_to_add): # Validator Class
    matrix = copy.deepcopy(data) # Have to manipulate data so don't want to overwrite original data
    if algorithm_flag == True: # This is for backward elimination
        for i in range(matrix.shape[0]): # This is for forward selection
                for j in range(1, matrix.shape[1]):
                    if j not in current_set and j != feature_to_add:
                        matrix[i][j] = 0
    else:
        for i in range(matrix.shape[0]):
            for j in range(1, matrix.shape[1]):
                if (j in current_set and j == feature_to_add) or j not in current_set:
                    matrix[i][j] = 0
        

    number_correctly_classified = 0
    for i in range(matrix.shape[0]): # Loop over num of instances
        object_to_classify = matrix[i][1:]
        label_object_to_classify = matrix[i][0]

        nearest_neighbor_distance = np.inf
        nearest_neighbor_location = np.inf
        for k in range(matrix.shape[0]): # See instances compared 
            if k != i:
                #print(f'Ask if {i} is nearest neighbor with {k}')
                distance = np.sqrt(sum(np.power(object_to_classify - matrix[k][1:], 2)))

                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = matrix[nearest_neighbor_location][0]
        
        #print(f'Object {i} is class {label_object_to_classify}')
        #print(f'Its nearest_neighbor is {nearest_neighbor_location} which is in class {nearest_neighbor_label}')

        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1

    accuracy = number_correctly_classified / len(matrix)
    return accuracy


def main():
    #data = np.loadtxt('small-test-dataset.txt')
    data = np.loadtxt('Large-test-dataset.txt')
    
    #print(data.shape[0]) # Instances
    #print(data.shape[1]) # Features per instance ignoring the first one which is the class
    #for i in range(data.shape[0]):
    #    for j in range(data.shape[1]):
    #        print(data[i][j])

    print("Type each feature you want to be in the current set and press enter")
    current_set = []
    feature = ''
    while(feature != 00):
        feature = int(input())
        current_set.append(feature)
        

    print("Type the feature you want to add")
    feature_to_add = input()

    start_time = time.perf_counter()
    accuracy = leave_one_out_validation(data, current_set, feature_to_add)
    end_time = time.perf_counter()
    print(f'accuracy: {accuracy}')
    print(f'Time: {end_time - start_time} seconds')

if __name__ == "__main__":
    main()