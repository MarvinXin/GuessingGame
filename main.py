
from Func import gameStart

def show_initial():
    print("\nGuessing Game between 1 - 10")
    print("1. Start Game")
    print("2. End Game")




def main():
    show_initial()
    while True:
        choice = input("Select an Option: ")

        if choice == '1':
            gameStart()
            return False
        
        elif choice == '2':
            print("Thanks for looking around!")
            return False

        else:
            print("Please select an appropriate number: ")

if __name__ == "__main__":
    main()
