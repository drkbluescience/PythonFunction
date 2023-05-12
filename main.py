from functions import numbers, fileOp

def call_functions():
    _num = -1
    while _num < 1:
        p_num = int(input("Enter a positive number:  "))
        _num = p_num

    print(numbers.check_strong(_num), "\n")
    print(numbers.show_neon(_num), "\n")
    print(f"{_num}. Fibonacci is ", numbers.fibonacci(_num), "\n")
    print(numbers.perfect_number(_num), "\n")

if __name__ == "__main__":
    #call_functions()
    file = 'trees.csv'
    min_tree = fileOp.minHeightTree(file)
    print(f"The length of the min. tree in the file is {min_tree}")
    