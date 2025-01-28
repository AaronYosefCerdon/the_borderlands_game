import sys

# Print intro message for the trivia game.
introduction = "Welcome to the Borderlands, the place between life and death. Clear all 16 games to find the truth of this place."
print(introduction)

# Print the instructions for the game.
mechanics = "Start by choosing a game from the following options. Each game can only be cleared once. Trying to repeat a game will force you into the selection area again. The games will not stop unless all 16 games are cleared or incorrect answers are put in."
print(mechanics)

message = "The games can be cleared in any order. The truth will be revealed once all games have been cleared. Failure in any game and failure to complete all games will result in death. Best of luck. "
print(message)

# Create a format for each game.
def play_game(questions, game_name, num_questions):
    # Initialize a score counter.
    score = 0
    for question in questions:
        print(question["question"])
        answer = input("Your answer: ").strip()
        if answer.lower() == question["answer"].lower():
            score += 1
        else:
            print(f"Wrong answer! The correct answer was: {question['answer']}")
            print("Game Over! Death awaits.")
            sys.exit()  # Terminate the program if the answer is wrong
    print(f"Congratulations! Game Cleared! You've cleared {game_name}!")
    return True  # Return True if the player clears the game

def main():
    # Set a list to ensure no repeated games and track the finished games.
    game_clear = 0
    games_played = []  
    while len(games_played) < 16:  
        print("Choose the game you want to play: ")
        print("1. Ace of Diamonds")
        print("2. Ace of Hearts")
        print("3. Ace of Spades")
        print("4. Ace of Clubs")
        print("5. Jack of Diamonds")
        print("6. Jack of Hearts")
        print("7. Jack of Spades")
        print("8. Jack of Clubs")
        print("9. Queen of Diamonds")
        print("10. Queen of Hearts")
        print("11. Queen of Spades")
        print("12. Queen of Clubs")
        print("13. King of Diamonds")
        print("14. King of Hearts")
        print("15. King of Spades")
        print("16. King of Clubs")
        game_choice = input("Enter the number of your chosen game: ")

        # Create the Ace of Diamonds game.
        if game_choice == "1" and "Ace of Diamonds" not in games_played:
            print("Welcome to the Ace of Diamonds. The game is called Star Magic.")
            print("Answer these 10 questions about constellations to clear the game. If a mistake is made, game over. Good luck!")
            star_questions = [
                {"question": "What constellation is depicted by the lion?", "answer": "Leo"},
                {"question": "Which animal is represented by Aries?", "answer": "Ram"},
                {"question": "Which constellation is said to be the bird that carried Zeus' thunderbolts?", "answer": "Aquila"},
                {"question": "Which constellation is depicted as the sea monster?", "answer": "Cetus"},
                {"question": "There are _____ well-known constellations, each depicting different animals, beings or objects. How many official constellations are there?", "answer": "88"},
                {"question": "What constellation is known as the smallest?", "answer": "Crux"},
                {"question": "What constellation is the oldest known?", "answer": "Taurus"},
                {"question": "Orion is considered as the ________ constellation. What is he considered as?", "answer": "Hunter"},
                {"question": "Which constellation is known as the biggest?", "answer": "Hydra"},
                {"question": "Which constellation is depicted as the Twins?", "answer": "Gemini"}
            ]
            if play_game(star_questions, "Star Magic", 10):
                games_played.append("Ace of Diamonds")
                game_clear += 1

        # Create the Ace of Hearts game.
        elif game_choice == "2" and "Ace of Hearts" not in games_played:
            print("Welcome to the Ace of Hearts. The game is called Mind Heart.")
            print("Complete these 7 quotes from the TV show Alice in Borderland by filling in the blanks. The game will be cleared once all quotes are finished. Any mistake means game over. Good luck!")
            quote_questions = [
                {"question": "Ryohei Arisu: 'You guys are all I have. If someone has to _________ this game, it's not me'. This heartbreaking statement by Ryohei was uttered as he pleaded for his friends to reveal their locations in the deadly 7 of Hearts. Fill in the blank with the correct word. Here's a clue: it is an action word that depicts a certain condition when disaster strikes.", "answer": "Survive"},
                {"question": "Shuntaro Chishiya: To gain something, you need to ______ something. This brutal statement is caused by Chishiya's jaded look in life. What word describes the statement so it fills the criteria for you to gain something? Hint: it's an action word that every person has experienced in life.", "answer": "lose"},
                {"question": "Hikari Kuina: You just keep turning your back on your past, but I will ______ my past once more in order to survive. This determined statement fueled her fire to clear the games, what did she do to her past instead of turning her back on it? Hint: What you see in the mirror.", "answer": "Face"},
                {"question": "Niragi Suguru: Left to our own devices, _______ will rape, steal and kill each other. That's just who we really are. Niragi's beliefs came from his troubled life, who does he think will harm each other? No hints for this one.", "answer": "Humans"},
                {"question": "Usagi Yuzuha: It amazes me that I'm willing to do ________ just so I can survive. If we weren't willing, we might as well die. Usagi's words highlight her will to survive the deadly games. What is she willing to do to survive? Hint: It is something we can all do.", "answer": "Anything"},
                {"question": "Ginji Kyuma: Your life is yours. Don't _______ someone else's path. This statement inspires everyone to take their own fate into their hands. What is he saying we should not do?", "answer": "Follow"},
                {"question": "Mira Kano: Life is just a _______ we play together. You should try to enjoy it. Mira's last words are a statement that encompassed the themes of the Borderlands. What word is she comparing life to? Hint: It is something that can be done alone but is more fun together.", "answer": "Game"}
            ]
            if play_game(quote_questions, "Mind Heart", 7):
                games_played.append("Ace of Hearts")
                game_clear += 1

        # Create the Ace of Spades game.
        elif game_choice == "3" and "Ace of Spades" not in games_played:
            print("Welcome to the Ace of Spades. The game is called Run Rabbit Run.")
            print("You are a rabbit running through a 5km long road. The goal of the game is to make it through the obstacles blocking the road.")
            print("Answer 5 health-related questions to clear the game. Failure will result in death. Remember that each question will increment at every 1km.")
            health_questions = [
                {"question": "A woman is competing in a fun run with a total distance of 3 kilometers. She forgets to drink her water from the 2-liter flask she carried and passes out at the 2-kilometer mark. If she ran at a pace of 200 meters per 15 minutes and she estimated that she needed to drink 250mL of her water every 30 minutes, how much water should she have already drunk? Answer in mL.", "answer": "1250 mL"},
                {"question": "Organizers of a scavenger hunt created resting stations inside the 5km scope area for the hunt. How many resting stations are there if they are placed every 200 meters?", "answer": "25"},
                {"question": "A teenager created an exercise regimen to stay fit and healthy. He should consider his ________ so he does not overexert himself. What should he consider?", "answer": "limits"},
                {"question": "A college student has been awake for 4 days without any sleep. He should have _______ instead of focusing on his work. What should he have done instead?", "answer": "slept"},
                {"question": "12 people are competing in a swimming contest. What equipment should they wear for their eyes?", "answer": "Goggles"}
            ]
            if play_game(health_questions, "Run Rabbit Run", 5):
                games_played.append("Ace of Spades")
                game_clear += 1

        # Create the Ace of Clubs game.
        elif game_choice == "4" and "Ace of Clubs" not in games_played:
            print("Welcome to the Ace of Clubs. The game is called Escape Rules.")
            print("You are trapped in a rectangular room with 6 other people. The key to your escape is your teamwork.")
            print("Answer 7 questions about passcodes each participant received to find the keys that will unlock the 7 padlocks of the exit. Participants may not say their passcode out loud. They may only give clues. Failure will result in death by poison gas.")
            escape_questions = [
                {"question": "Participant B's code is their height. If Participant A at 160cm is taller and Participant C at 158cm is shorter, what is the height of Participant B? Answer in this format: i.e. 100cm.", "answer": "159cm"},
                {"question": "Participant D's code is their favorite color. They said it is not a part of the rainbow but at the same time it is all parts of the rainbow. What color are they describing?", "answer": "White"},
                {"question": "Participant G's code is their favorite food. They said that it is something sweet that has a hole in the middle. What food are they describing?", "answer": "Doughnut"},
                {"question": "Participant A's code is their dream career. They said it is in the field of engineering. Additionally, they said that this certain career can handle both hardware and software. What career is being described?", "answer": "Computer Engineer"},
                {"question": "Participant F's code is their favorite flower. They said that it is the most common flower to give your significant other and that it was red. What flower is this?", "answer": "Rose"},
                {"question": "Participant C's code is their pet dog's breed. They said that the breed is black and white with dots. What dog is this?", "answer": "Dalmatian"},
                {"question": "Participant E's code is their birth month. They said that a new beginning happens during this month. What month is it?", "answer": "January"}
            ]
            if play_game(escape_questions, "Escape Rules", 7):
                games_played.append("Ace of Clubs")
                game_clear += 1
        #Create the Jack of Diamonds game.
        elif game_choice == "5" and "Jack of Diamonds" not in games_played:
            print("Welcome to the Jack of Diamonds. The game is called Mathlete Mayhem.")
            print("You are trapped at the center of a massive maze. Certain paths are blocked off by math equations.")
            print("Answer 7 math questions to escape the maze in the shortest possible path. Failure will result in death by drowning.")
            math_questions = [
                {"question": "A baker made seven dozen cupcakes. Half are strawberry, a quarter are blueberry and the last quarter are chocolate. How many strawberry and blueberry cupcakes are there?", "answer": "63"},
                {"question": "A town with a population of 138,492 is holding an election for mayor. How many votes does a candidate need for a majority? Answer in this format: 10,000.", "answer": "69,246"},
                {"question": "A school is sending 48 students abroad for an exchange program. 15 are for Humanities, 8 are for Science, 12 are for History and the rest are for Math. How many students are there for Math? ", "answer": "13"},
                {"question": "A couple are planning their wedding. They invited 427 guests in total. Tables for the reception are for 7. How many tables are needed to seat all 427 guests?", "answer": "61"},
                {"question": "A flower shop sells bouquets depending on the number of flowers. 20 flowers cost Php 150. How much does 90 flowers cost? Answer only the number i.e. 400.", "answer": "675"},
                {"question": "A pet shop has 47 of a certain breed of dog. If each dog needs about 4kg of food per month and the cost of food per kg is Php 200, how much do they spend a year on food? Answer in this format: 10,000", "answer": "451,200"},
                {"question": "A laboratory synthesized a new serum for a certain disease. There are 176 patients awaiting this treatment. If each patient needs a dose for day and each dose is inside a syringe, how many syringes do all the patients need for a week?", "answer": ""}
            ]
            if play_game(math_questions, "Mathlete Mayhem", 7):
                games_played.append("Jack of Diamonds")
                game_clear += 1
        #Create the Jack of Hearts game.
        elif game_choice == "6" and "Jack of Hearts" not in games_played:
            print("Welcome to the Jack of Hearts. The game is called Inner Soul.")
            print("Answer these simple question with simple answers. Do not overthink.")
           
            simple_questions = [
                {"question": "A person at one point or another asks in life: What is my ________? What does a person wonder? No hint.", "answer": "Purpose"},
                {"question": "No one is born to be alone in this _______. You'll find people who will love and care for you. Where is a person not born to be alone?", "answer": "World"},
                {"question": "I would _________ myself for the ones I love. What would someone do for their loved ones? ", "answer": "Sacrifice"},
                
            ]
            if play_game(simple_questions, "Inner Soul", 3):
                games_played.append("Jack of Hearts")
                game_clear += 1    
        #Create the Jack of Spades game.
        elif game_choice == "7" and "Jack of Spades" not in games_played:
            print("Welcome to the Jack of Spades. The game is called Lava Floor.")
            print("The arena's floor is lava. Navigate the obstacles to make it to the goal. Choose your actions wisely.")
           
            lava_questions = [
                {"question": "The start has two possible paths. A small jump to a frail platform or a large jump to a sturdy platform. Do you do a small or large jump?", "answer": "large"},
                {"question": "Reaching the platform, there are 2 sets of stairs. One leads downward and the other leads upward. Do you go upward or downward?", "answer": "Upward"},
                {"question": "Upon finishing the stairs, there are 2 bridges. One is made of thick wood and the other is made of heat resistant steel. Which bridge do you cross? Wood or Steel? ", "answer": "Steel"},
                {"question": "The goal is only step away. There are however two doors in your way. One is covered by hearts and the other is filled with spades. Which door leads to the goal? Hearts or Spades?", "answer": "Spades"},
                
            ]
            if play_game(lava_questions, "Lava Floor", 4):
                games_played.append("Jack of Spades")
                game_clear += 1  
        #Create the Jack of Clubs game.
        elif game_choice == "8" and "Jack of Clubs" not in games_played:
            print("Welcome to the Jack of Clubs. The game is called Better Together.")
            print("The arena is a huge mansion. Find 88 keys pertaining to the constellations scattered around. Work together with the 21 other participants to find them all.")
            print("Since teamwork is key, each participant needs to find 4 keys. The ones assigned to you are Virgo, Libra, Andromeda and Draco. Do your part and find your keys. Failure will result in death.")
           
            better_questions = [
                {"question": "The key for Libra lies behind a painting stained with blood. This clue narrows down the answer to a war painting and a massacre painting. Noting the game is about teamwork, which painting is hiding Libra's key?", "answer": "War"},
                {"question": "After getting Libra's key, the clue for Andromeda says that it is hidden in the depths of the mansion. Do you go to the attic or the basement?", "answer": "Basement"},
                {"question": "Upon finding Andromeda's key, you proceed to Virgo's key. The clue says it is hidden where the helpers sleep. The only places that apply are a 1st floor and a 3rd floor room. Which room is the key in?", "answer": "1st floor"},
                  {"question": "The final key is Draco's. The clue says it is hidden where dragons rule. Upon getting to the roof, there are 7 towers with different symbols: a dove, a dragon, a star, a lion, a pegasus, a centaur and a fairy. Which tower is Draco's key in? Answer the animal only.", "answer": "Dragon"},
                
            ]
            if play_game(better_questions, "Better Together", 4):
                games_played.append("Jack of Clubs")
                game_clear += 1                              

        #Create the Queen of Diamonds game.
        elif game_choice == "9" and "Queen of Diamonds" not in games_played:
            print("Welcome to the Queen of Diamonds. The game is called Display Exploration.")
            print("The arena is an museum with various exhibits in different areas. Each participant is locked with a collar that will detonate after a certain amount of time passes and given a phone for the game.")
            print("The employees of the museum have placed various riddles around the place that will unlock the collars. The catch is, the collars have 9 locks each. Enter the answers for each riddle in the given phone to the corresponding lock to open them.")
            print("Be careful, just one incorrect answer will detonate the collar.")
           
            riddle_questions = [
                {"question": "I have a mouth and a bed but I don't eat or sleep. What am I?", "answer": "River"},
                {"question": "I am always moving but I never move. Also, I follow you everywhere but you only see me when there's light. What am I?", "answer": "Shadow"},
                {"question": "What is something that people repeatedly break but will never physically hold?", "answer": "Promise"},
                {"question": "What is something that you know is always approaching but will never actually arrive?.", "answer": "Tomorrow"},
                {"question": "I always move at certain speeds. I feel happy when love finds me, but I always break when I'm alone and betrayed. What is being described?", "answer": "Heart"},
                {"question": "What is something that will inevitably happen but we can never prevent?", "answer": "Death"},
                {"question": "I disappear at night but I greet you in the morning. I do this to everyone but at different times. What am I?", "answer": "Sun"},
                {"question": "This happens in different stages of our lives. Some will fade and some will stay. New ones will appear and go, but it is undeniable that this exists even if it disappears.", "answer": "Memories"},
                {"question": "I am older than everyone but bit by bit I will fade. When the time comes, I will be nothing and disappear as if I never existed. What is this?", "answer": "Universe"}
                                
            ]
            if play_game(riddle_questions, "Display Exploration", 9):
                games_played.append("Queen of Diamonds")
                game_clear += 1
                                                                        
        # End if all games have been cleared.
        if len(games_played) == 16:
            print("Congratulations! You have cleared all the games!")
            break
   

if __name__ == "__main__":
    main()
