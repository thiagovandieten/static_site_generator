import unittest
from src.block import *


class test_block(unittest.TestCase):
    def test_markdown_to_block_string(self):
        very_long_string = (
            "# Header 1: A variable that includes a lot of lines\n\n "
            "   to break up a string over multiple lines. This is a very long string "
            "that I am going to use to demonstrate how to break up a string over "
            "multiple lines.\n\n "
            "Now here's a list of items:\n\n"
            "- Item 1\n"
            "- Item 2\n"
            "- Item 3\n"
        )
        expected_result = [
            ("Header 1: A variable that includes a lot of lines", BlockType.HEADING),
            (
                "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
                BlockType.PARAGRAPH,
            ),
            ("Now here's a list of items:", BlockType.PARAGRAPH),
            ("- Item 1\n- Item 2\n- Item 3", BlockType.UNORDERED_LIST),
        ]
        self.assertEqual(markdown_to_blocks(very_long_string), expected_result)

    # Test to see if markdown_to_blocks strips away any empty blocks (\n\n\n\n)
    def test_markdown_to_block_string_empty(self):
        very_long_string = (
            "# Header 1: A variable that includes a lot of lines\n\n\n\n "
            "   to break up a string over multiple lines. This is a very long string "
            "that I am going to use to demonstrate how to break up a string over "
            "multiple lines.\n\n\n\n "
            "> This is a real quote, I said this! - Abraham Lincoln\n\n"
            "Now here's a list of items:\n\n"
            "- Item 1\n"
            "- Item 2\n"
            "- Item 3\n"
        )
        expected_result = [
            ("Header 1: A variable that includes a lot of lines", BlockType.HEADING),
            (
                "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
                BlockType.PARAGRAPH,
            ),
            ("This is a real quote, I said this! - Abraham Lincoln", BlockType.QUOTE),
            ("Now here's a list of items:", BlockType.PARAGRAPH),
            ("- Item 1\n- Item 2\n- Item 3", BlockType.UNORDERED_LIST),
        ]
        self.assertEqual(markdown_to_blocks(very_long_string), expected_result)

    def test_block_to_block(self):
        # TODO: The following needs to be added to the test:
        # Code, Ordered List
        result_from_previous_test = [
            "# Header 1: A variable that includes a lot of lines",
            "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
            "> This is a real quote, I said this! - Abraham Lincoln",
            "Now here's a list of items:",
            "- Item 1\n- Item 2\n- Item 3",
        ]
        block_types = []
        for block in result_from_previous_test:
            block_types.append(determine_block_type(block))

        self.assertListEqual(
            [
                BlockType.HEADING,
                BlockType.PARAGRAPH,
                BlockType.QUOTE,
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST,
            ],
            block_types,
        )

    def test_markdown_to_html(self):
        result_from_previous_test = [
            "# Header 1: A variable that includes a *lot* of lines",
            "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
            "> This is a real quote, I said this! - Abraham Lincoln",
            "Now here's a list of items:",
            "- Item 1\n- Item 2\n- Item 3",
        ]

        expected_result = ParentNode(
            "div",
            [
                ParentNode(
                    "h1",
                    [
                        LeafNode("Header 1: A variable that includes a "),
                        LeafNode("i", "lot"),
                        LeafNode(" of lines"),
                    ],
                ),
                LeafNode(
                    "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
                    "p",
                ),
                LeafNode(
                    "blockquote", "This is a real quote, I said this! - Abraham Lincoln"
                ),
                LeafNode("p", "Now here's a list of items:"),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                        LeafNode("li", "Item 3"),
                    ],
                ),
            ],
        )
        result_string = "\n\n".join(result_from_previous_test)
        result = markdown_to_html(result_string)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
