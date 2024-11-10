import unittest
from util import *
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
    
    def test_extract_image(self):
        test_str = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(test_str), expected_result)

    def test_extract_hyperlink(self):
        test_str = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_result = [("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(test_str), expected_result)

