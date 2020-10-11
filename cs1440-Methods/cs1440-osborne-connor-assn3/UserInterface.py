import Deck
import Menu

class UserInterface():
    def __init__(self):
        pass


    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main Menu:\nInput 'C' to create a deck of cards or 'X' to exit the program")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False


    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards

        menu1 = Menu.Menu("Card Size:\nInput the card size(needs to be from 3 to 15 or it wont be any fun :)")
        for i in range(3, 16):
            num = i
            menu1.addOption(str(num), "Input the card size")

        keepGoing = True
        while keepGoing:
            command1 = menu1.show()
            if int(command1) > 10 or int(command1) < 3:
                print("Wrong size, try again!")
                pass
            else:
                while keepGoing:
                    op1 = 2 * int(command1) * int(command1)
                    op2 = 4 * int(command1) * int(command1)
                    menu2 = Menu.Menu("Highest Number:\nChoose the highest number on your card " + str(op1) + " or " + str(op2))
                    menu2.addOption(str(op1), "the highest number on card")
                    menu2.addOption(str(op2), "the highest number on card")
                    command2 = menu2.show()
                    if int(command2) != op1 and int(command2) != op2:
                        print("That's not an option try again.")
                        pass
                    else:
                        while keepGoing:
                            menu3 = Menu.Menu("Deck Creation: How many cards would you like?(choose amount between 3 and 10000)")
                            for i in range(3, 10001):
                                num = i
                                menu3.addOption(str(num), "Number of cards you want")
                                command3 = menu3.show()
                            if int(command3) < 3:
                                print("Not enough cards for a deck!")
                                pass
                            elif int(command3) > 10000:
                                print("Waaaaay too many cards! Are you tying to open a store?")
                                pass
                            else:
                                while keepGoing:
                                    deck = Deck.Deck(int(command1), int(command3), int(command2))
                                    self.__deckMenu()

        # TODO: Create a new deck

        # TODO: Display a deck menu and allow user to do things with the deck
        pass


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen");
        menu.addOption("D", "Display the whole deck to the screen");
        menu.addOption("S", "Save the whole deck to a file");

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False


    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")
