import unittest
from util import *
from textnode import TextNode, TextType


class test_util(unittest.TestCase):

    def test_split_notes_code(self):
        test_list = [
            TextNode("I already have a non-normal format", TextType.BOLD),
            TextNode("I should be `code` but my type is Normal", TextType.NORMAL),
            # TextNode("I should be *italic* but my type is Normal", TextType.NORMAL)
        ]
        expected_list = [
            TextNode("I already have a non-normal format", TextType.BOLD),
            TextNode("I should be ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" but my type is Normal", TextType.NORMAL),
        ]
        self.assertEqual(split_nodes_delimiter(test_list, "`"), expected_list)

    def test_extract_image(self):
        test_str = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(extract_markdown_images(test_str), expected_result)

    def test_extract_hyperlink(self):
        test_str = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_result = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(extract_markdown_links(test_str), expected_result)

    def test_split_nodes_images(self):
        test_nodes = [
            TextNode(
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                TextType.NORMAL,
            )
        ]
        expected_nodes_list = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        nodes_list = split_nodes_images(test_nodes)
        self.assertEqual(nodes_list, expected_nodes_list)

    def test_split_nodes_links(self):
        test_nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL,
            )
        ]
        expected_nodes_list = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        nodes_list = split_nodes_links(test_nodes)
        self.assertEqual(nodes_list, expected_nodes_list)

    def test_split_nodes_links_no_link(self):
        test_nodes = [
            TextNode("This is text with no link", TextType.NORMAL),
        ]
        self.assertEqual(split_nodes_links(test_nodes), test_nodes)

    def test_text_to_textnodes(self):
        long_string = (
            f"Hello! I'm Thiago *and* i'm **testing** if `this works`"
            f"throwing a image here ![jerma spinning](https://media.tenor.com/SJXGyYpQFdgAAAAi/jerma-sparkle.gif)"
            f"and a hyperlink [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )

        expected_nodes = [
            TextNode("Hello! I'm Thiago ", TextType.NORMAL),
            TextNode("and", TextType.ITALIC),
            TextNode(" i'm ", TextType.NORMAL),
            TextNode("testing", TextType.BOLD),
            TextNode(" if ", TextType.NORMAL),
            TextNode("this works", TextType.CODE),
            TextNode("throwing a image here ", TextType.NORMAL),
            TextNode(
                "jerma spinning",
                TextType.IMAGE,
                "https://media.tenor.com/SJXGyYpQFdgAAAAi/jerma-sparkle.gif",
            ),
            TextNode("and a hyperlink ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        result_nodes = text_to_textnodes(long_string)
        self.assertEqual(result_nodes, expected_nodes)

    def test_markdown_to_block_string(self):
        very_long_string = (
            "# Header 1: A variable that includes a lot of lines\n\n "
            "   to break up a string over multiple lines. This is a very long string "
            "that I am going to use to demonstrate how to break up a string over "
            "multiple lines.\n\n "
            "Now here's a list of items:\n"
            "- Item 1\n"
            "- Item 2\n"
            "- Item 3\n"
        )
        expected_result = [
            "# Header 1: A variable that includes a lot of lines",
            "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
            "Now here's a list of items:\n- Item 1\n- Item 2\n- Item 3"
        ]
        self.assertEqual(markdown_to_blocks(very_long_string), expected_result)

    # Test to see if markdown_to_blocks strips away any empty blocks (\n\n\n\n)
    def test_markdown_to_block_string_empty(self):
        very_long_string = (
            "# Header 1: A variable that includes a lot of lines\n\n\n\n "
            "   to break up a string over multiple lines. This is a very long string "
            "that I am going to use to demonstrate how to break up a string over "
            "multiple lines.\n\n\n\n "
            "Now here's a list of items:\n"
            "- Item 1\n"
            "- Item 2\n"
            "- Item 3\n"
        )
        expected_result = [
            "# Header 1: A variable that includes a lot of lines",
            "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
            "Now here's a list of items:\n- Item 1\n- Item 2\n- Item 3"
        ]
        self.assertEqual(markdown_to_blocks(very_long_string), expected_result)