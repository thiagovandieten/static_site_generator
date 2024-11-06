import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_html_output(self):
        node = LeafNode(
            "Google", "a", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Google</a>')

    def test_html_output_no_props(self):
        node = LeafNode("Hello", "p")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_html_output_no_tag(self):
        node = LeafNode("Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_html_output_empty_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("", "p")
            node.to_html()

    def test_html_output_with_multiple_props(self):
        node = LeafNode(
            "Link", "a", {"href": "https://example.com", "class": "external-link"}
        )
        self.assertEqual(node.to_html(), '<a href="https://example.com" class="external-link">Link</a>')

if __name__ == "__main__":
    unittest.main()