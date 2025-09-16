noun = str(input("Enter a noun: "))
verb = str(input("Enter a verb: ")) 
adjective = str(input("Enter an adjective: "))
adverb = str(input("Enter an adverb: "))
print("Do you " + str(verb) + " your " + str(adjective) + " " + str(noun) + " " + str(adverb) + "? That's hilarious!")
print("One of these fine days," + str(adverb) + " I will " + str(verb) + " my " + str(adjective) + " " + str(noun) + ".")

while True:
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    if not noun or not verb or not adjective or not adverb:
        print("All fields are required. Please try again.")
        continue

    print("Do you " + verb + " your " + adjective + " " + noun + " " + adverb + "? That's hilarious!")
    print("One of these fine days," + adverb + " I will " + verb + " my " + adjective + " " + noun + ".")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Goodbye!")
        break