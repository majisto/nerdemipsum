import mysql.connector
import random
import textwrap
nouns = []
verbs = []
adjectives = []
adverbs = []
time = []

quotes = """""Go to {place} and fetch me the {thing}," said {person}.
"{person}, hand me the {thing}!" yelled {person}.
"We ran after {pl_species} overran {place}." {person} said.
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
{thing} and {thing}: two tastes that go great together.
{time}, the {pl_species} had no fear of {pl_thing}.
{person} and {person} {adv} {verb} to their death.
{time}, the {pl_species} and the {pl_species} were at war.
{time}, the {species} people lived {p_place}.
{person} was a {species} from {place}.
{person} used the {thing} to {t_verb} the {thing}.
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
{person} {t_verb} an entire villiage of {species}.""".split('\n')

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

def parse(a,cursor):
	b = a.find('{')
	while (b != -1):
		c = a.find('}')
		word = a[b+1:c]
		subs = get_symbol(word,cursor)
		a = a.replace("{"+word+"}",subs,1)
		b = a.find('{')
	return a

def get_symbol(word,cursor):
	word2 = ""
	if word == 'adv':
		word2 = random.choice(adverbs)[1]
	if word == 'person':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='person'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'adv':
		word2 = random.choice(adverbs)[1]
	if word == 'thing':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='thing'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 't_verb':
		things = []
		query = "SELECT * FROM verbs WHERE trans='yes'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'place':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='place'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'pl_species':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='species' AND number='plural'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'p_place':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='place' AND prep!=''"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		blah = random.choice(things)
		word2 = blah[7] + " " + blah[1] 
	if word == 'species':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='species'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'time':
		word2 = random.choice(time)[1]
	if word == 'event':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='event'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'pl_thing':
		things = []
		query = "SELECT * FROM nouns WHERE subtype='thing' AND number='plural'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'verb':
		things = []
		query = "SELECT * FROM verbs WHERE trans='no'"
		cursor.execute(query)
		for word in cursor:
			things.append(word)
		word2 = random.choice(things)[1]
	if word == 'adj':
		word2 = random.choice(adjectives)[1]
	return word2

def get_line(cursor):
	randnum = random.randint(0,2)
	if randnum == 0:
		quote = get_quote()
		return parse(quote,cursor)
	else:
		non_quote = get_non_quote()
		return parse(non_quote,cursor)

def get_quote():
	global quotes
	return random.choice(quotes)

def get_non_quote():
	global non_quotes
	return random.choice(non_quotes)

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
	wrapper = textwrap.TextWrapper(fix_sentence_endings = True, width = width)
	for i in range (0,numSent):
		text += get_line(cursor) + "  "
	print wrapper.fill(text)
	cursor.close()
	cnx.close()

main()