import unittest
from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a Bold text node", TextType.BOLD)
        node2 = TextNode("This is a Italic text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_urls(self):
        node = TextNode("I'm code!", TextType.LINK, "https://code.dev")
        node2 = TextNode("I'm code!", TextType.LINK, "https://code.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
