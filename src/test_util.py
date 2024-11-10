import unittest
from util import split_nodes_delimiter
from textnode import TextNode, TextType
class test_util(unittest.TestCase):

    def test_split_notes_code(self):
        test_list = [
            TextNode("I already have a non-normal format", TextType.BOLD),
            TextNode("I should be `code` but my type is Normal", TextType.NORMAL)
            # TextNode("I should be *italic* but my type is Normal", TextType.NORMAL)
        ]
        expected_list = [
            TextNode("I already have a non-normal format", TextType.BOLD),
            TextNode("I should be ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" but my type is Normal", TextType.NORMAL)

        ]
        self.assertEqual(split_nodes_delimiter(test_list,'`', TextType.CODE), expected_list)
    
    # def test_find_delimitier(self):
    #     test_str = "I am a line of text with `CODEEEE`, let's hope this works"
    #     self.assertEqual(_find_delimiter_in_line(test_str, '`'), [25,33])
        
    #     test_str2 = "I am a line of text with *ITALICS*, let's *hope* this works"
    #     self.assertEqual(_find_delimiter_in_line(test_str2, '*'), [25,33,42,47])
