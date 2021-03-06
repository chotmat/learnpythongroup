from nose.tools import *
from ex48 import lexicon
from ex48.parser import *

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east West down up left right back Back")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east'),
                          ('direction', 'West'),
                          ('direction', 'down'),
                          ('direction', 'up'),
                          ('direction', 'left'),
                          ('direction', 'right'),
                          ('direction', 'back'),
                          ('direction', 'Back')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat Stop")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat'),
                          ('verb', 'Stop')])

def test_stops():
    assert_equal(lexicon.scan("the"),[('stop', 'the')])
    result = lexicon.scan("the in of from at It")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ('stop', 'from'),
                          ('stop', 'at'),
                          ('stop', 'It')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess door Cabinet")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess'),
                          ('noun', 'door'),
                          ('noun', 'Cabinet')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
def test_parser():
    result = parse_sentence([('verb', 'eat'),('noun', 'honey')])
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'honey')
    assert_raises(ParserError, parse_sentence,[('noun', 'bla'), ('verb', 'dog')])

