import string

# First Coding Challenge

# def cut_line(queue: list, cutter: str) -> list: 
#     """
#     Return a list containing queue's "strings" in the 
#     same order, with the exception of cutter, which will  
#     be moved to the end of list regardless of position in queue. 

#     >>> cut_line(["Sam", "Ben"], "Sam")
#     ['Ben', 'Sam']

#     >>> cut_line([
#     "Max", "Emily", "Helen"],  // list of ppl in line
#     "Max" // cutter)
#     ['Emily', 'Helen', 'Max']

#     >>> cut_line(["Aldric", "Andrew", "Adam"], "Andrew")
  

#     >>> cut_line(["Kevin", "Jimmy", "Dylan"], "Dylan")
#     ['Kevin', 'Jimmy', 'Dylan']

#     >>> cut_line(["Mehul", "Jacob", "Alex"], "Jacob")
#     ['Mehul', 'Alex', 'Jacob']
#     """
#     "*** YOUR CODE HERE ***"

######################################
#                                    #
#              Problem 1             # 
#                                    #
######################################
list = ['Luis','Lindsay', 'Xander' , 'Alicia']
cutter = "Luis"
index = list.index(cutter)

def cut_line(list, cutter): 
  list.remove(cutter)
  list.append(cutter)  
  print(list)  
  
cut_line(list, cutter)

######################################
#                                    #
#              Problem 2             # 
#                                    #
######################################

# Carnival Celebration” costs $25 per adult ticket and $10 per child ticket.
# Full House: 3 adults and 2 children, or 3 children and 2 adults = $60
adult_tix = 25
child_tix = 10
adults   = 3  
children = 3
total_cost = 60
# Three of a Kind: 3 adults = $50
# Date Night: 2 adults = $40
# Single Mom: 1 adult and 1 child = $30

def total_cost(adults, children):
  if adults == 2 and children == 0:
    return 40
  if adults == 1 and children == 1:
    return 30
  if adults == 3 and children == 0:
    return 50 
  if adults==3 and children==2 or children==3 and adults==2:
    return 60
  else:
    return adults *25 + children*10


def ring_toss(chance_matrix: list) -> list:
    """
    Return the coordinate with the highest value in 
    the combined (element-wise multiplied) matrix, composed 
    by multiplying each element in the 'chance_matrix' argument 
    by the corresponding element of the base 'distance_matrix'.

    >>> ring_toss([[1,1,1],
                   [1,1,1],
                   [1,1,2]])
    [2, 2]

    >>> ring_toss([[3,4,2],
                   [1,8,2],
                   [2,1,2]])
    [0, 0]
    """
    "*** YOUR CODE HERE ***"
  def distance(alistofalist)
 newlist.apened(ring_toss)
 split() 
   
     
######################################
#                                    #
#              Problem 3             # 
#                                    #
######################################

  

def odd_otto(sentence: str) -> str:
    """
    Return a string containing the same character elements as sentence 
    with the exception of those consecutive non-space-characters forming a word 
    with an even number of characters, and even numbers, not returning them. 

    >>> odd_otto("How are you doing today Otto")
    'How are you doing today'

    >>> odd_otto("How easy is it for you to listen to us")
    'How for you'

    >>> odd_otto("Hi hi hi hi hi hi hi")
    ''

    >>> odd_otto("Hello hello hello hello")
    'Hello hello hello hello'
    
    >>> odd_otto("All passwords are 192837")
    'All passwords are 192837'

    >>> odd_otto("The passwords include 192834")
    'The passwords include'
    """
    newlist=[]
    word=sentence.split()
    for f in word:
      if f.isdigit() and f%2 == 1:
        newlist.append(f)
    else:
        if len(f)%2==1:
          newlist.append(f)
    return ' '.join(newlist)

######################################
#                                    #
#              Problem 4             # 
#                                    #
######################################

  
def censor_words(sentence: str, censor_words: list) -> str:
    """
    Return a string containing the same character elements as the sentence 
    with the exception of those consecutive characters forming a word 
    within censor_words, replacing them with "****". 

    >>> censor_words("What the lollipop are you doing?", ["lollipop"])
    'What the **** are you doing?'

    >>> censor_words("You're such a smart genius", ["genius", "smart"])
    "You're such a **** ****"

    >>> censor_words("You're a star!", ["robot", "uprising"])
    "You're a star!"

    >>> censor_words("You're a star!", ["star", "PiEboy"])
    "You're a ****!"

    >>> censor_words("I think you're a PaRty PoOpEr!", ["pooper", "stinky"])
    "I think you're a PaRty ****!""""
    newlist= []
    star=sentence.split()
    for word in star:
      if word.lower() in censor_words:
        newlist.append("****")
      else:
        newlist.append(word)
      return ' '.join(newlist)

def censor_words(bad_words, sentence):
    for word in bad_words:
        sentence = sentence.replace(word, "*" * len(word))
    return sentence



bad_words = ["bad word!1", "bad word 2"]
sentence = "bro really be looking like " + bad_words[0]

if bad_words[0] in sentence:
    censored_sentence = censor_words(bad_words, sentence)
    print(censored_sentence)



  

######################################
#                                    #
#              Problem 5             # 
#                                    #
######################################

def decode_riddle(sentence: str, shift: int) -> str:
    """
    Return a string with the original sentence elements shifted 
    across the alphabet 'shift' times. Symbols and non-alphabetical-character 
    elements will be the same in the returned string. 

    >>> decode_riddle("Khoor", -3)
    'Hello'

    >>> decode_riddle("Tfk fk ofkdqlpp", 3)
    'Win in ringtoss'

    >>> decode_riddle("Obxiiv Avixk?", 29)
    'Really Dylan?'

    >>> decode_riddle("AtP cznvd! Qtle Wfi!", -245)
    'PiE rocks! Fiat Lux!'
    """
  kev='abcdefghijklmnopqrstuvwxyz'
  code=[]
  shift=shift%26
  for letter in sentence:
    if letter.lower() in kev:
      if letter==letter.lower():
        code.append(kev[kev.index(letter)+shift])
      else:
        code.append(kev[kev.index(letter)+shift].upper())
    else:
      code.append(letter)
  return ''.jo
#def decode_riddle(wordle):
letter = list(string.ascii_letters)
sentence = "Khoor"
shift = -3

#def decode_riddle(sentence: str, shift: int) -> str:
  index = letter.index(sentence
  for l in letter:
   i = letter.index(l) + shift
    for s in sentence:
     print(s)
  i = letter.index(letter)
  for s in sentence:
    #print(s)
    for l in letter:
      l = s
      print(str(i) + l)
decode_riddle(sentence, shift)



def is_vegan(food: str, menu_dict: dict) -> bool:
    """
    Return a boolean depending on whether there is or isn't a node at 
    the end of the food tree, which is "nonvegan". If any 
    instances of "nonvegan" appear within the food tree, 
    obtained from menu_dict, return False. Otherwise, return True
    
    >>> is_vegan('pizza', {'pizza':['cheese', 'sauce', 'dough'], 'cheese':['soy'], 'sauce':['beef'], 'beef':['nonvegan'], 'dough':['vegan'], 'soy':['vegan']})
    False

    >>> is_vegan('salad', {'salad':['lettuce', 'croutons'], 'lettuce':['vegan'], 'croutons':['bread'], 'bread':['wheat'], 'wheat':['vegan']})
    True

    >>> is_vegan('toast', {'toast':['bread'], 'bread':['flour'], 'flour':['wheat'], 'wheat':['vegan']})
    True
    """
if menu_dict[Food]==["vegan"]:
   return true 
elif menu_dict[food] !=['nonvegan']:
  return all([isvegan(child,menu_dict) for child in menu_dict[food]])

   
######################################
#                                    #
#              Problem 7             # 
#                                    #
######################################

# >>> ring_toss([[1,1,1],
#                    [1,1,1],
#                    [1,2,1]])
#     [2,1]

#     >>> ring_toss([[3,4,2],
#                    [1,8,2],
#                    [2,1,2]])
#     [0,0]

# After figuring out the riddle from Decode Riddle, you decide to go to this ring toss, which you assume you must win as fast as possible. To do this, you hypothesize that the less rings on a bottle, the less your chances are, so you assign a “chance” value to each bottle. You also decide that there is a lower chance of you throwing a ring on a bottle further from the edge, so you create the following ‘distance’ matrix (a list of lists):
	
# 	[[3,2,3],
# 	 [2,1,2],
# 	 [3,2,3]]
	
# Given this matrix and a chance matrix derived from the amount of rings on each bottle, multiply the two values together (element-wise matrix multiplication) and return the index with the highest “chance” value in a list. If there are ties, just return the closest index to [0,0]. 

# Hint: Remember, the 0th index is the first!

# The function must return the nearest coordinate in form of a list (indices of both inner and outer list ex: [2][4] = [2, 4]) with the highest integer value in the combined (element-wise multiplied) matrix, composed of a list containing lists containing integers, which is created by multiplying each element in the ‘chance_matrix’ argument by the corresponding element of the base ‘distance_matrix’.

chance = [3,2,3]
chance2 = [2,1,2]
chance3 = [3,2,3]

chance_comp=[x*2 for x in chance]
chance2_comp=[x*2 for x in chance2]
chance3_comp=[x*2 for x in chance3]

print(chance_comp)
print(chance2_comp)
print(chance3_comp)

for i in chance()
  if i > 2
    print(i)



######################################
#                                    #
#              Problem 9             # 
#                                    #
######################################

# def ac_transit(travel_map)


# The Pioneers in Engineering: “Carnival Celebration”, in addition to all its other high tech accommodations, has its own transit system, “Awesome Carnival” transit, or AC transit. Since the area is so large, some places which aren’t easy to ride end up empty, since most people don’t want to walk far distances. 

# This is where you come in, given a dictionary of locations (with lists for each location indicating where the line travels) for any given transit map, you must return a list of lists containing connected areas (you can transverse from any of these areas to another). If one area is not connected to another (including one way transfers), append a new list onto the main list, containing that area, and add further areas that connect to and from that area. Note that locations can lead to multiple places. 

# The function must return a list containing lists comprising highly connected node elements, of the elements found in ac_transit/travel_map. If a node can reach another node and go back, they are highly connected. If a node cannot go back or to, then it is not highly connected. 

#     >>> ac_transit({“Entrance”:[“Castle”], “Castle”:[“Entrance”]})
#     [[“Entrance”, “Castle”]]

#     >>> ac_transit({“Entrance”:[“Castle”]}, “Castle”:[]})
#     [[“Entrance”], [“Castle”]]

#     >>> ac_transit({“Entrance”:[“Castle”], “Castle”:[“Entrance”],
#                     “Pool”: “Entrance”)})
#     [[“Entrance”, “Castle”], [“Pool”]]

#     >>> ac_transit({“Entrance”:[“Castle, Pool”], “Castle”:[“Entrance”],
#                     “Pool”: [“Castle”, “Cafe”], “Cafe”:[]})
#     [[“Entrance”, “Castle”, “Pool”], [“Cafe”]]
