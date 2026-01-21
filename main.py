choice = input("Which way do you want to go? (left, right, straight,quit): ")
if choice == "left":
    print("you went left and stumbled into the libarary!")
elif choice == "right":
    print("you went right and found a empty cafe")
elif choice == "straight":
    print("you went straight and entered the gym")
elif choice == "quit":
    print("thanks for playing!")
else:
    print("that is not a valid choice.")
