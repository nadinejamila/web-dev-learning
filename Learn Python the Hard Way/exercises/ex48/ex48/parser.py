class ParserError(Exception):
	pass

class Sentence(object):

	def __init__(self, subject, verb, obj):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]


def peek(word_list):
	"""
	A function that can peek at a list of words 
	and return what type of word it is.
	"""
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None


def match(word_list, expecting):
	"""
	A function that confirms that the expected word is the right type, 
	takes it off the list, 
	and returns the word.
	"""
	if word_list:
		word = word_list.pop(0)
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None


def skip(word_list, word_type):
	"""
	This function  skips as many words of a certain type as it finds.
	"""
	while peek(word_list) == word_type:
		match(word_list, word_type)


def parse_verb(word_list):
	"""
	We skip any stop words, 
	then peek ahead to make sure the next word is a "verb" type. 
	If it's not then raise the ParserError to say why. 
	If it is a "verb" then match it, which takes it off the list. 
	"""
	skip(word_list, 'stop')

	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'noun')
	else:
		raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)