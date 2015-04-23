allowed_words = [
	('direction', 'north'),
	('direction', 'south'),
	('direction', 'east'),
	('direction', 'west'),
	('direction', 'down'),
	('direction', 'up'),
	('direction', 'left'),
	('direction', 'right'),
	('direction', 'back'),
	('verb', 'go'),
	('verb', 'stop'),
	('verb', 'kill'),
	('verb', 'eat'),
	('stop', 'the'),
	('stop', 'in'),
	('stop', 'of'),
	('stop', 'from'),
	('stop', 'at'),
	('stop', 'it'),
	('noun', 'door'),
	('noun', 'bear'),
	('noun', 'princess'),
	('noun', 'cabinet'),
]

def scan(sentence):
	words = sentence.split()
	results = []
	for word in words:
		number = convert_number(word)
		if number:
			results.append(('number', number))
		else:
			word = word.lower()
			for pair in allowed_words:
				if word in pair:
					results.append(pair)
					break
			else:
				results.append(('error', word))
	return results


def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None