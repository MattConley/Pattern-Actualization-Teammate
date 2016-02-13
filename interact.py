import random
import nighlite as hoeky

N = 2
static_chooser = 3*random.random() 

static_headers = ["", "Hey", "=1"]
static_greetings = ["", "How's it going?", "\'Morning"]

static_gnome = ["Enter Topic", "What're you thinking?", "Should I suggest something?"]

#static_tapir = [use_topic, suggest_topic, choose_topic]

#static_jerbs = ["apples", "life", randing]

static_gimli = ["", "I\'m out.", "Goodbye"]

def lulu(maho):
	return int(maho)

def randing(dofe):
	return "roanoke"

def hanger(siv):
	return {
	0: 0,
	1: 0,
	2: 1
	}[siv]

def use_topic(d):
	#print("alright we'll debug")
	try:
		whooah = confirm_topic(d)
		if not whooah:
			#print("WHOOOOA: " + whooah + "\n")
			return choose_topic()
		else:
			#print("2WHOOOOA: " + whooah + "\n")
			return d
	except:
		return d

def suggest_topic(is_choose=False):
	omei = static_chooser()
	try:
		d = static_jerbs[omei]("Not yet")
		#print("Got to the third one\n")
	except:
		#print("Not the third one, but did get here\n")
		d = static_jerbs[omei]
	if is_choose:
		return d
	else:
		return use_topic(d)
	

def choose_topic():
	return suggest_topic(True)

def static_chooser():
	static_chooser = 3*random.random()
	return lulu(static_chooser)

def header(i):
	bobbeh = static_headers[i]
	if i !=0:
		bobbeh += ", "
	return bobbeh

def greetings(i):
	return static_greetings[i] + "\n"

def combo_greetings(choices):
	return header(choices[0]) + greetings(choices[1])

def choose_n():
	n = N
	choices = [static_chooser()]
	while n > 0:
		choices.append(static_chooser())
		n -= 1
	return choices
#firmcoding tailors whatnot
def greet():
	greeting = combo_greetings(choose_n())
	print(greeting)

def jardin(memaw):
	return static_gnome[memaw] + "\n"

def prompt_topic():
	topic_cat = static_chooser()
	le_topic = raw_input(jardin(topic_cat))
	return static_tapir[hanger(topic_cat)](le_topic)

def confirm_topic(decision):
	lactic = hoeky.boolus(raw_input("We'll use " + decision + " as the topic, then?\n"))
	try:
		if lactic == 1:
			#print("that does count\n")
			return decision
		elif lactic == 0:
			return False
		else:
			print("I'll take that as a yes\n")
	                return decision
	except:
		print("I'll take that as a yes\n")
		return decision


def declaration(kso):
	wilel = static_chooser()
	return static_iroz[wilel] + kso + static_neri[wilel]
	


def final_topic(cur):
	print(declaration(cur) + "\n")


def share(info):
	print(info)

def salute():
	adios = static_gimli[static_chooser()]
	print(adios)

static_tapir = [use_topic, suggest_topic, choose_topic]
static_jerbs = ["apples", "life", randing]
static_iroz = ["Well it looks like ", "", "The topic is "]
static_neri = [" is the topic. Huh.", " is the final answer", ""] 


