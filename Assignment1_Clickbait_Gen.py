'''
Author: Aadil Hussain
Built on: Python 3.10.8
'''
import random

# Create a program that will generate a random number of
# clickbait headlines from exisiting lists of:

# 1) nouns (ie. 'Athlete’,'Clown’,'Shovel','Robot')
# 2) places (ie. 'house','attic','school’,'basement’)
# 3) provinces (ie. 'Ontario’,'BC','Alberta’,'Nova Scotia')
# 4) when (ie. 'later this year','soon', later today','right now')
# 5) object pronouns (ie. 'her','him','them’)
# 6) possesive pronouns (ie. 'hers','his','theirs')
# 7) personal pronouns (‘She','he’,'they’)

# Have a random generator that selects from a 5 choice of
# preset sentences that can use the lists to import. Each
# sentence preset should be its own function (the random
# generator will select which preset).

# Lists of words
nouns = ['Athlete', 'Clown', 'Shovel', 'Robot']
places = ['house', 'attic', 'school', 'basement']
provinces = ['Ontario', 'BC', 'Alberta', 'Nova Scotia']
when = ['later this year', 'soon', 'later today', 'right now']
object_pronouns = ['her', 'him', 'them']
possessive_pronouns = ['hers', 'his', 'theirs']
personal_pronouns = ['She', 'he', 'they']

# Sentence presets
def sentence_preset_1():
    return f"{random.choice(personal_pronouns)} found {random.choice(nouns)} in their {random.choice(places)}!"

def sentence_preset_2():
    return f"Why {random.choice(personal_pronouns)} can't stop talking about {random.choice(nouns)}!"

def sentence_preset_3():
    return f"{random.choice(provinces)} is the new hotspot for {random.choice(nouns)} enthusiasts!"

def sentence_preset_4():
    return f"Get ready for {random.choice(when)} – {random.choice(personal_pronouns)} have a surprise for {random.choice(object_pronouns)}!"

def sentence_preset_5():
    return f"{random.choice(personal_pronouns)} just uncovered the secret of {random.choice(nouns)} in the {random.choice(places)}!"

# Randomly select a sentence preset and generate a headline
def generate_clickbait_headline():
    presets = [sentence_preset_1, sentence_preset_2, sentence_preset_3, sentence_preset_4, sentence_preset_5]
    selected_preset = random.choice(presets)
    return selected_preset()

# Generate a specified number of clickbait headlines
num_headlines = 5  # You can change this number as needed
for _ in range(num_headlines):
    headline = generate_clickbait_headline()
    print(headline)
