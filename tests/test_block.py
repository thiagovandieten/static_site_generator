import unittest
from src.block import *


class test_block(unittest.TestCase):
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
            "Now here's a list of items:\n- Item 1\n- Item 2\n- Item 3",
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
            "# Header 1: A variable that includes a lot of lines",
            "to break up a string over multiple lines. This is a very long string that I am going to use to demonstrate how to break up a string over multiple lines.",
            "> This is a real quote, I said this! - Abraham Lincoln",
            "Now here's a list of items:",
            "- Item 1\n- Item 2\n- Item 3",
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
            block_types.append(block_to_block_type(block))

        self.assertListEqual([
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.QUOTE,
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST
        ], block_types)


if __name__ == "__main__":
    unittest.main()
