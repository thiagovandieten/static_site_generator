from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object):
        if not isinstance(other, TextNode):
            raise NotImplementedError

        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"TextNode: ({self.text}, {self.text_type}, {self.url})"
    
    def to_leafNode(self):
        match self.text_type:
            case TextType.NORMAL:
                return LeafNode(self.text)
            case TextType.BOLD:
                return LeafNode(self.text, "b")
            case TextType.ITALIC:
                return LeafNode(self.text, "i")
            case TextType.CODE:
                return LeafNode(self.text, "code")
            case TextType.LINK:
                return LeafNode(self.text, "a", {"href": self.url})
            case TextType.IMAGE:
                return LeafNode(self.text, "img", {"src": self.url})
            case _:
                raise ValueError("Invalid TextType")