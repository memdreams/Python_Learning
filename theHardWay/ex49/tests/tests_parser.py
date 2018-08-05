from nose.tools import *
from ex49 import *

def test_peek():
    assert_equal(peek([('direction', 'north')]), 'direction')
    assert_equal(peek([]), None)

def test_match():
    assert_equal(match([('direction', 'north')], 'direction'), ('direction', 'north'))
    assert_equal(match([('direction', 'north')], 'verb'), None)
    assert_equal(match([], 'verb'), None)

def test_skip():
    assert_equal(skip([('direction', 'north')], 'direction'), None)

def test_parseverb():
    assert_equal(parse_verb([('verb', 'go')]), ('verb', 'go'))
    assert_equal(parse_verb([('stop', 'the'), ('verb', 'go')]), ('verb', 'go'))
    with assert_raises(ParserError):
        parse_verb([('stop', 'the'), ('hello', 'go')])
    assert_raises(ParserError, parse_verb, [('hello', 'go')])

def test_parseobject():
    assert_equal(parse_object([('noun', 'princess')]), ('noun', 'princess'))
    assert_equal(parse_object([('stop', 'the'), ('direction', 'north')]), ('direction', 'north'))
    with assert_raises(ParserError):
        parse_object([('stop', 'the'), ('hello', 'go')])
    assert_raises(ParserError, parse_object, [('hello', 'go')])

def test_parsesubject():
    assert_is_instance(parse_subject([('verb', 'go'), ('noun', 'princess')], ('direction', 'west')), Sentence)

def test_parsesentence():
    assert_is_instance(parse_sentence([('noun', 'princess'), ('verb', 'go'), ('direction', 'east')]), Sentence)
    assert_is_instance(parse_sentence([('verb', 'go'), ('noun', 'bear'), ('direction', 'west')]), Sentence)
    with assert_raises(ParserError):
        parse_sentence([('stop', 'the'), ('hello', 'go')])
    assert_raises(ParserError, parse_sentence, [('hello', 'go')])
