import sys

def calculate_sum(scores):
    """calculate sum of given scores."""
    return sum(scores)

def calculate_average(scores):
    """calculate average of given scores."""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)



if __name__ == "__main__":
    print("=== Array Scores Processor (main) ===")
    try:
        # Case 1: CLI arguments passed (for Jenkins)
        if len(sys.argv) > 1:
            scores = [int(x) for x in sys.argv[1:]]

        # Case 2: Console input
        else:
            raw_input_value = input("Enter integer scores: ")
            scores = [int(x) for x in raw_input_value.split()]

        print("\n=== Program Parameters ===")
        print("Scores entered:", scores)

        total = calculate_sum(scores)
        avg = calculate_average(scores)
       

        print(f"\nSum of scores = {total}")
        print(f"Average of scores = {avg:.2f}")
   

    except ValueError:
        print("Invalid input! Please enter integer values only.")
