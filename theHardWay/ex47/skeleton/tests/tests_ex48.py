# This file is the test file for testing lexicon in ex48, which actually in ex47 now

from nose.tools import *
from ex47.ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("North SOUTH east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 45 9123")
    assert_equal(result, [('number', 3),
                          ('number', 45),
                          ('number', 9123)])

def test_errors():
    assert_equal(lexicon.scan("ASJEUF"), [('error', 'ASJEUF')])
    result = lexicon.scan("bear ISA the princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'ISA'),
                          ('stop', 'the'),
                          ('noun', 'princess')])
