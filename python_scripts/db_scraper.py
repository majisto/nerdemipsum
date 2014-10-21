import mysql.connector
import random
import textwrap
import re
nouns = []
verbs = []
adjectives = []
adverbs = []
time = []
lexicon = {}


quotes = """""Go to {place} and fetch me the {thing}," said {person}.
"{person}, hand me the {thing}!" yelled {person}.
"We ran after {pl_species} overran {place}," {person} said.
"Anger leads to hate.  Hate leads to {place}."
"{person} and {person} at {place}.  {person}, when the walls fell."
"Where were the {pl_species} when {place} fell?!" {person} shouted.
"Where are {person} and {person}, for I much desire to speak with them... {adv}."
"They're taking the {species} to {place}!" said {person}.
"{pl_thing}!  Boil them, mash them, stick them in a {thing}!" shouted {person}.
{person} told them, "It's dangerous to go alone. Take this {thing}."
"Speak {thing} and enter." said {person}.
"A day may come when the {thing} of {species} fails... but that is not THIS day!" shouted {person}.
"I am no man," said {person}.
"{adj} {species}! You shall not pass!" shouted {person}.
"{person}, I recognized your foul {thing} when I was brought on board."
"I used to bullseye {pl_species} with my {thing}."
"Many {pl_species} {verb} to bring us this {thing}."
"{person}, {thing} won't help us now!" {person} shouted.
"Ah, {person}... We meet again," {person} said.""".split("\n")

non_quotes = """{person} {adv} {t_verb} the {thing}.
{person} and {thing} simply don't mix.
{thing} and {thing}: two great tastes that go great together.
{time}, the {pl_species} had no fear of {pl_thing}.
{person} and {person} {adv} {verb} to their death.
{time}, the {pl_species} and the {pl_species} were at war.
{time}, the {species} people lived {p_place}.
{person} was a {species} from {place}.
{person} used the {thing} and {t_verb} the {thing}.
{person} and {person} travelled together to {place}.
{person} had never seen a {adj} {thing} before.
During {event}, the {pl_species} fled into {place}.
The {adj} {thing} was lost during {event}.
{place}:  You will never find a more wretched hive of {thing} and {thing}.
Don't underestimate the {thing}.
{person} vowed vengeance against the {pl_species}.
{person} taught {person} how to use the {thing}.
{person} and {person} embarked upon a quest to destroy the {thing}.
{person} led the rebels against {person}'s evil empire.
{person} grew up on {place} and was raised by {pl_species}.
{person} {t_verb} the {thing}.
The {pl_species} {verb} from the {pl_species} after {event}.
The {pl_species} {verb} to {place}.
The {pl_species} {verb} too {adv} and too {adv}.
{person} paid far too much money for that new {thing}.
{person} {verb} and {person} {verb}.
{person} challenged {person} to a battle to the death.
That {species} is terrorizing {place}!
{person} leads his {species} army against {place}.
{time}, the {species} kingdom hailed {person} as their leader.
Time was, {p_place}, you couldn't swing a {thing} without hitting a {thing}.
The {pl_species} were known to steal {pl_thing} from the surrounding villages.
{person} and {person} climbed to the top of {place}, with the hopes of destroying the {thing}.
{person} mourned with the {pl_species} after {event}.
Then {person} {verb} all the way to {place}.
{person} {t_verb} the {thing} against all advice.
That {thing} just {t_verb} {place}!
{p_place}, {thing} {t_verb} you.
{person} {t_verb} an entire village of {pl_species}.""".split('\n')

def connect():
	config = {
	'user': 'bdddb6df4683a5',
	'password': 'fe4a4628',
	'host': 'us-cdbr-azure-central-a.cloudapp.net',
	'database': 'ni42mysql'
	}
	try:
		cnx = mysql.connector.connect(**config)
		cursor = cnx.cursor(buffered=True)
	except:
		print "Connecting went wrong.  All is doom."
		exit(-1)
	return cnx, cursor

def fill_lists(cnx,cursor,table_name):
	global nouns,verbs,adjectives,adverbs
	query = "SELECT * FROM %s"%(table_name)
	try:
		cursor.execute(query)
	except:
		print "Such crap, much fail"
		cursor.close()
		cnx.close()
		exit(-1)
	for (word) in cursor:
		eval(table_name).append(word)

def parse(pattern):
    """Replaces every {term} with a random item from lexicon[term].  Allows recursion."""
    while "{" in pattern:
        pattern = re.sub('{([^}]+)}', replacer, pattern)
    return pattern

def replacer(matchobj):
    return random.choice(lexicon[matchobj.group(1)])

def get_line():
	randnum = random.randint(0,2)
	if randnum == 0:
		return parse(random.choice(quotes))
	else:
		return parse(random.choice(non_quotes))

def make_lexicon():
    """Makes a dictionary of lists with the info replacer() cares about,
    using the lists from the initial database queries.
    """
    global lexicon

    for x in "time", "adj", "adv", "person", "event", "place", "p_place", "t_verb", "verb", "species", "pl_species", "thing", "pl_thing":
        lexicon[x] = []
    for x in nouns:
    	if "person" in x[3]:
    		lexicon["person"].append(x[1])
    	elif "event" in x[3]:
    		lexicon["event"].append(x[1])
    	elif "place" in x[3]:
    		lexicon["place"].append(x[1])
    		lexicon["p_place"].append(x[7] + " " + x[1])
    	elif "thing" in x[3]:
    		if "singular" in x:
    			lexicon["thing"].append(x[1])
    		else: lexicon["pl_thing"].append(x[1])
    	elif "species" in x[3]:
    		if "singular" in x:
    			lexicon["species"].append(x[1])
    		else: lexicon["pl_species"].append(x[1])
    for x in verbs:
    	if "yes" in x[3]:
    		lexicon["t_verb"].append(x[1])
    	else:
    		lexicon["verb"].append(x[1])
    lexicon["time"] = [x[1] for x in time]
    lexicon["adj"] = [x[1] for x in adjectives]
    lexicon["adv"] = [x[1] for x in adverbs]

def main():
    width = 100
    numSent = 8
    cnx, cursor = connect()
    fill_lists(cnx,cursor,'nouns')
    fill_lists(cnx,cursor,'adverbs')
    fill_lists(cnx,cursor,'verbs')
    fill_lists(cnx,cursor,'adjectives')
    fill_lists(cnx,cursor,'time')
    text = ""
    wrapper = textwrap.TextWrapper(fix_sentence_endings = False, width = width)
    make_lexicon()
    for i in range (0,numSent):
    	text += get_line() + "  "
    print wrapper.fill(text)
    cursor.close()
    cnx.close()

main()