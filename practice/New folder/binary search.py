#create a textfile
#doc and pdf(do try with this)
def binarysearch(filename, target):
    with open(filename, 'r') as file:
        words = file.readline().splitlines()  # Read all lines as list of words/lines
        words.sort()  # Sort the words for binary search
    
    left = 0
    right = len(words) - 1
    steps = 0

    print(f"\nSearching for '{target}' in file '{filename}'")
    print("Sorted words:", words)

    while left <= right:
        mid = (left + right) // 2
        steps += 1

        # Show current search range
        print(f"Step {steps}: Searching in range {words[left:right+1]}")

        if words[mid] == target:
            print(f"Target '{target}' found at index {mid} after {steps} steps.")
            return mid
        elif words[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Target '{target}' not found after {steps} steps.")
    return -1


# Example usage:
filename = r"D:\rushda\python\practice\New folder\rushda.txt" # Put your file path here
target = input("Enter word to search: ")
binarysearch(filename, target)
