## easy
sentence_easy = "Python is an object-oriented-programming language. In object-oriented-programming we use classes and objects. One test that interviewers use is fizz-buzz in which we find the numbers that are divisible by '3' or '5' or '3' and '5', and return either fizz-buzz, buzz or fizz. Another test is by writing a factorial function. For example, '5' factorial is '5x4x3x2x1' or '120'. It is also good practice to write your function names using camel-case format. In this, you use variables called dropLast or bubbleSort. \n"

## medium
sentence_medium = "One study in programming is that of combinatorics which is the study of discrete structures. In computer science, combinatorics is important because methods such as the luhn-algorithm are used for credit-card encryption. The topic combinatorics also influences Eigenvalues and eigenvectors, which are influential for linear transformations. Algorithms such as monte-carlo-integrations are also used for vector graphics and topological algorithms used in visual computation and simulations."

## hard 
sentence_hard = "The bowyer-watson algorithm is used for computing triangulation of points used in Voronoi diagrams. Such algorithms, such as the baire-category-theorem are used for calculating topological spaces. This particularly theorem was proved by Baire in 1899. The field of knot-theory is another interesting field that is the study of knots in topological spaces. These algorithms are particularly important for deep learning, where neural networks use alpha-beta-pruning to implement successful algorithms that are used in voice recognition or computer vision."

# choices to activate each level
all_sentences = [sentence_easy, sentence_medium, sentence_hard]

# answers for each level
all_answers = [["object-oriented-programming", "fizz-buzz", "camel-case", "factorial"],
["combinatorics", "luhn-algorithm", "Eigenvalues", "monte-carlo-integrations"],
["bowyer-watson", "baire-category-theorem", "knot-theory", "alpha-beta-pruning"]]

## Game start
def GameOn():
  print "Welcome to Guess the obfuscated programming term." + "\n"
  level = raw_input("Would you like to try easy, medium or hard?")
  
  ## choose your level
  print "You chose {}".format(level)
  if level == "easy":
    level = 0
  elif level == "medium":
    level = 1
  elif level == "hard":
    level = 2
  ## exception handling for level not defined
  else:
    print "Not a valid level. Please try again."
    return GameOn()
  level = WrongOrRight(level)
  return level

## word transformer 
def ReplaceWords(level, filler):
  
  sentences = all_sentences[level]
 ## split each sentence by spaces (tricky no punctuation or won't match!) 
  while filler < len(all_answers[level]):
    index_of_word = 0
    replaced_word = all_answers[level][filler]
    words = sentences.split(" ")
    #print words
    
## replace each word that needs to be guessed with a number     
    while index_of_word < len(words):
      if words[index_of_word] == replaced_word:
        words[index_of_word] = "__{}__".format((filler + 1))
      index_of_word = index_of_word + 1 
## join spaces back and return the full sentence with filler __num__     
    filler = filler + 1 
    sentences = " ".join(words)
  return sentences
  
## guessed right or wrong
def WrongOrRight(level):
  filler = 0 
  while filler < len(all_answers[level]):
    print ReplaceWords(level, filler)
## make user guess 
    prompt = "Make a guess for the number {}".format(str(filler + 1))
    guess = raw_input(prompt).lower()
    
    correct = all_answers[level][filler].lower()
    if correct == guess:
      print "You got it right!\n"
      filler = filler + 1
    else:
      print "Incorrect. Guess again.\n"
  print all_sentences[level]
  print " Thanks for playing!"
  return
## run game 


## function play again or quit?
def Play():
  print "Would you like to play again?"
  play = raw_input("Press Y or N")
  print "You chose {}".format(play)
  if play == 'Y':
    GameOn()
  else:
    quit(0)

## this is essentially where game runs 
GameOn()
## after game is run, ask the user if they want to play again or quit 
Play()

