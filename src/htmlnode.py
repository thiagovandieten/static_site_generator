from typing import Any


class HTMLNode:
    """A abstract-ish representation of HTML

    What is meant by abstract-ish is that the class ideally should
    not be used as an object, but for other classes like ParentNode and
    LeafNode to inheirit and implement

    Attributes:
        value: The str value between the opening and closing brackets
        tag: The str that determines what the HTML tag is like e.g <a></a>
        children: Because html tags can get nested, it's children are stored here
        props: A list of attributes for the tags
    """

    def __init__(
        self,
        value: str | None = None,
        tag: str | None = None,
        children: list[Any] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
           return False
        return self.tag == other.tag and self.children == other.children and self.props == other.props
        

    def __repr__(self) -> str:
        return (
            f"HTMLNode data:\n"
            f"value: {self.value}\n"
            f"tag: {self.tag}\n"
            f"children: {self.children}\n"
            f"props: {self.props}"
        )

    """An abstract method that requires its children to implement"""
    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_string(self) -> str:
        if self.props is None:
            raise ValueError("Props is empty")
        props_string = ""
        for i in self.props:
            props_string += f'{i}="{self.props[i]}" '
        return props_string.rstrip()
    
