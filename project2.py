import random
import copy
# Row represents instance and column represents feature

def leave_one_out_validation():
    return random.random() # Generates a random float between 0.0 and 1.0


def ForwardSelection(num_features):
    print("\nBeginning search.\n")
    current_set_of_features = []

    accuracy = leave_one_out_validation()
    print(f"Using no features and \"random\" evaluation, I get an accuracy of {accuracy}\n")

    max_accuracy = 0 # Had to initialize outside of for loop to remember previous accuracy for comparison
    for i in range(num_features): # Tree level
        #print(f"On the {i}'nth level of the search tree")
        best_feature = None
        prev_accuracy = copy.deepcopy(max_accuracy)
        max_accuracy = 0

        for j in range(num_features): # Features on each level
            if (j not in current_set_of_features):
                accuracy = leave_one_out_validation()
                print(f"Using feature(s) {j} accuracy is {accuracy}")

                if accuracy > max_accuracy:
                    max_accuracy = accuracy
                    best_feature = j
            
        
        current_set_of_features.append(best_feature)
        print(f"\nFeature set {current_set_of_features} was best, accuracy is {max_accuracy}\n")

        if(max_accuracy < prev_accuracy):
            print("(Warning, Accuracy has decreased!)")
            max_accuracy = prev_accuracy
            current_set_of_features.pop()
            break
    
    print(f"Finished search!! The best feature subset is {current_set_of_features}, which has an accuracy of {max_accuracy}")


def BackwardElimination(num_features):
    print("\nBeginning elimination.\n")
    current_set_of_features = list(range(num_features))

    accuracy = leave_one_out_validation()
    print(f"Using all features and \"random\" evaluation, I get an accuracy of {accuracy}\n")

    max_accuracy = 0 # Had to initialize outside of for loop to remember previous accuracy for comparison
    for i in range(num_features): # Tree level
        print(f"On the {i}'nth level of the search tree")
        best_feature_to_remove = None
        prev_accuracy = copy.deepcopy(max_accuracy)
        max_accuracy = 0

        for j in range(num_features): # Features on each level
            if (j in current_set_of_features):
                accuracy = leave_one_out_validation() # plug in current_set_of_features
                print(f"Removing feature(s) {j} accuracy is {accuracy}")

                if accuracy > max_accuracy:
                    max_accuracy = accuracy
                    best_feature_to_remove = j
        
        current_set_of_features.remove(best_feature_to_remove)
        print(f"\nFeature set {current_set_of_features} was best which removed {best_feature_to_remove}, accuracy is {max_accuracy}\n")

        if(max_accuracy < prev_accuracy):
            print("(Warning, Accuracy has decreased!)")
            max_accuracy = prev_accuracy
            current_set_of_features.append(best_feature_to_remove)
            break
    
    print(f"Finished elimination!! The best feature subset is {current_set_of_features}, which has an accuracy of {max_accuracy}")


def BertieSpecialAlgorithm():
    print("Nothing yet")


def main():
    print("Welcome to Bertie Woosters Kenneth Alvarez Feature Selection Algorithm.")
    print("Please enter total number of features:")
    num_features = int(input())

    print("Type the number of the algorithm you want to run")
    print("1 Forward Selection")  
    print("2 Backward Selection")
    print("3 Bertie's Special Algorithm")
    user_choice = input()

    print("Type the number of the dataset you want to use")
    print("1 Small Test Dataset")  
    print("2 Large Test Dataset")
    file_choice = input()
    if file_choice == '1':
        file = open("small-test-dataset.txt", "r")
    else:
        file = open("Large-test-dataset.txt", "r")
    print(file.read()) 

    if user_choice == '1':
        ForwardSelection(num_features)
    elif user_choice == '2':
        BackwardElimination(num_features)
    else:
        BertieSpecialAlgorithm(num_features)
    
    file.close() 

if __name__ == "__main__":
    main()