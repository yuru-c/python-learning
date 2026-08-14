import random

def main():    
    score = 0
    level = get_level()

    for _ in range(10):
        x, y =generate_integer(level)  

        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == x + y:
                    score += 1
                    break

                print("EEE")

            except(ValueError):
                print("EEE")
                
        else:
            print(f"{x} + {y} = {x + y}")        
            

    print(f"Score: {score}")
    

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        # x = random.randint(0, 9)
        # y = random.randint(0, 9)
        # return x, y
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        # x = random.randint(10, 99)
        # y = random.randint(10, 99)
        # return x, y
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        # x = random.randint(100, 999)
        # y = random.randint(100, 999)
        # return x, y
        return random.randint(100, 999), random.randint(100, 999)


if __name__ == "__main__":
    main()