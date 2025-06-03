"""
Solution for Variables and Data Types problem.
This program demonstrates the use of different data types and basic operations in Python.
"""

def demonstrate_variables_and_types():
    # Integer operations
    num1 = 10
    num2 = 5
    int_result = num1 + num2
    print(f"Integer operations: {int_result}")

    # Float operations
    float1 = 5.5
    float2 = 2.0
    float_result = float1 + float2
    print(f"Float operations: {float_result}")

    # String operations
    str1 = "Hello"
    str2 = "World"
    str_result = f"{str1}, {str2}!"
    print(f"String operations: {str_result}")

    # Boolean operations
    bool1 = True
    bool2 = False
    bool_result = bool1 and not bool2
    print(f"Boolean operations: {bool_result}")

    # List operations
    my_list = [1, 2, 3]
    my_list.append(4)
    print(f"List operations: {my_list}")

    # Dictionary operations
    my_dict = {"name": "John", "age": 25}
    my_dict["age"] = 30
    print(f"Dictionary operations: {my_dict}")

    # Tuple operations
    my_tuple = (1, 2, 3)
    print(f"Tuple operations: {my_tuple}")

    # Set operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set_result = set1.union(set2)
    print(f"Set operations: {set_result}")

    # Type checking
    print("\nType checking:")
    print(f"num1 is of type: {type(num1)}")
    print(f"float1 is of type: {type(float1)}")
    print(f"str1 is of type: {type(str1)}")
    print(f"bool1 is of type: {type(bool1)}")
    print(f"my_list is of type: {type(my_list)}")
    print(f"my_dict is of type: {type(my_dict)}")
    print(f"my_tuple is of type: {type(my_tuple)}")
    print(f"set1 is of type: {type(set1)}")

if __name__ == "__main__":
    demonstrate_variables_and_types() 