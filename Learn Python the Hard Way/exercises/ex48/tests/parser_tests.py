from nose.tools import *
from ex48 import parser

word_list = [('noun', 'princess'), ('verb', 'ate'), ('noun', 'honey')]

def test_sentence():
	sentence = parser.Sentence(('noun', 'princess'), ('verb', 'ate'), ('noun', 'honey'))
	assert_equal(sentence.subject, 'princess')
	assert_equal(sentence.verb, 'ate')
	assert_equal(sentence.object, 'honey')

def test_peek():
	assert_equal(parser.peek(word_list), 'noun')

def test_match():
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))	
	assert_equal(parser.match(word_list, 'noun'), None)

def test_skip():
	word_list = [('noun', 'princess'), ('verb', 'ate'), ('noun', 'honey')]
	parser.skip(word_list, 'noun')
	assert_equal(word_list, [('verb', 'ate'), ('noun', 'honey')])

def test_parse_verb():
	word_list = [('noun', 'princess'), ('verb', 'ate'), ('noun', 'honey')]
	assert_raises(parser.ParserError, parser.parse_verb, word_list)
	word_list.pop(0)
	assert_equal(parser.parse_verb(word_list), ('verb', 'ate'))

def test_parse_object():
	word_list = [('noun', 'princess'), ('verb', 'ate'), ('noun', 'honey')]
	assert_equal(parser.parse_object(word_list), ('noun', 'princess'))
	assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
	word_list = [('noun', 'princess'), ('verb', 'walk'), ('direction', 'south')]
	assert_equal(parser.parse_subject(word_list), ('noun', 'princess'))
	assert_equal(parser.parse_subject(word_list), ('noun', 'player'))
	word_list.pop(0)
	assert_raises(parser.ParserError, parser.parse_subject, word_list)

def test_parse_sentence():
	word_list = [('stop', 'the'), ('noun', 'princess'), ('verb', 'ate'), ('stop', 'the'), ('noun', 'honey')]
	sentence = parser.parse_sentence(word_list)
	assert_equal(sentence.subject, 'princess')
	assert_equal(sentence.verb, 'ate')
	assert_equal(sentence.object, 'honey')
