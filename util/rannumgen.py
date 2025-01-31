import random
def generate_random_numbers(count):
    if count <= 0:
        print("Please enter a positive integer.")
        return []
    
    random_numbers = [random.randint(0, 10000) for _ in range(count)]
    # print("Generated random numbers:")
    # print(random_numbers)

    return random_numbers
 
if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        generate_random_numbers(count)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
