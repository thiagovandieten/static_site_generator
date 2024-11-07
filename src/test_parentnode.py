import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_output_just_leafnodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("IM BOLD", "b"),
                LeafNode("im italic", "i"),
                LeafNode("I'm a hyperlink", "a", {"href":"https://www.google.com"})
            ]
        )
        self.assertEqual(node.to_html(), '<p><b>IM BOLD</b><i>im italic</i><a href="https://www.google.com">I\'m a hyperlink</a></p>')

    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", [])
            node.to_html()
    
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("bold", "b")])
            node.to_html()

    def test_with_string_values(self):
        node = ParentNode(
            "p",
            [
                "Hi! ",
                "We're both part of a paragraph"
            ]
        )
        self.assertEqual(node.to_html(), "<p>Hi! We're both part of a paragraph</p>")

    def test_nested_parentnodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("IM BOLD", "b"),
                        LeafNode("im italic", "i")
                    ]
                ),
                LeafNode("I'm a hyperlink", "a", {"href":"https://www.google.com"})
            ]
        )
        self.assertEqual(node.to_html(), '<div><p><b>IM BOLD</b><i>im italic</i></p><a href="https://www.google.com">I\'m a hyperlink</a></div>')

if __name__ == "__main__":
    unittest.main()
