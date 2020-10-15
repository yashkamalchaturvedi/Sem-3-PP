import random

#Vocabulary: words in 4 different parts of speech
articles     = ("A", "THE")
nouns        = ("BOY", "GIRL", "BAT", "BALL")
verbs        = ("HII", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
    """Builds and returns a sentence"""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a nounPhrase"""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verbPhrase"""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositionalPhrase"""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allow users to input the number of sentences
    to generate"""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()
