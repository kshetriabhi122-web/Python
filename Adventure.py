import time

def start_game():
    print("--- THE ADVENTURES OF CAPTAIN JACK SPARROW ---")
    print("You wake up on a deserted beach. Your compass is broken, and your ship is gone.")
    print("In front of you, the path splits into two directions.\n")

    game_over = False
    while not game_over:
        choice1 = input("Do you head inland into the thick JUNGLE or walk along the SHORE? (JUNGLE/SHORE): ").strip().upper()
        print("-" * 50)
        
        if choice1 == "JUNGLE":
            print("You slice through the vines and stumble upon a hidden cave filled with gold coin stacks!")
            print("Suddenly, you hear growling from the shadows.")
            choice2 = input("Do you RUN back to the beach or FIGHT whatever is in the dark? (RUN/FIGHT): ").strip().upper()
            print("-" * 50)
            
            if choice2 == "FIGHT":
                print("Ah, classic Jack Sparrow overconfidence! It was a wild jaguar. You were defeated.")
                print("💀 GAME OVER. Try again, Captain.")
                game_over = True
            elif choice2 == "RUN":
                print("You sprint back to the beach safely, your pockets rattling with a few stolen coins.")
                print("Let's try a different path.")
                print("-" * 50)
            else:
                print("You hesitated! The creature pounced. 💀 GAME OVER.")
                game_over = True

        elif choice1 == "SHORE":
            print("You walk along the coast and spot a small fishing boat anchored near the rocks.")
            print("There is an old fisherman sleeping on board.")
            choice2 = input("Do you STEAL the boat or WAKE the fisherman to ask for help? (STEAL/WAKE): ").strip().upper()
            print("-" * 50)
            
            if choice2 == "STEAL":
                print("You successfully hotwire the boat and sail into the sunset. A true pirate!")
                print("🏆 YOU WIN, Captain!")
                game_over = True
            elif choice2 == "WAKE":
                print("The fisherman wakes up, recognizes you, and turns you in to the Royal Navy for a bounty!")
                print("💀 GAME OVER. Enjoy the gallows, Jack.")
                game_over = True
            else:
                print("You stood there doing nothing until the tide came in and swept you out to sea. 💀 GAME OVER.")
                game_over = True
                
        else:
            print("Invalid choice, matey! Type JUNGLE or SHORE.")
            print("-" * 50)



if __name__ == "__main__":
    start_game()
