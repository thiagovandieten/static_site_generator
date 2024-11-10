import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):

    def test_base_raise_not_implemented(self) -> None:
        node = HTMLNode("h1", "Header")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_string(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_string(), 'href="https://www.google.com" target="_blank"'
        )

    def test_raise_empty_props(self):
        node = HTMLNode("h2", "Header 2")
        self.assertRaises(ValueError, node.props_to_html)

    def test_string_repr(self):
        node = HTMLNode(
            "a", "Google", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            f"{node}",
            (
                "HTMLNode data:\n"
                "value: a\n"
                "tag: Google\n"
                "children: None\n"
                "props: {'href': 'https://www.google.com', 'target': '_blank'}"
            )
        )

if __name__ == "__main__":
    unittest.main()

