from textnode import TextNode, TextType
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"


def markdown_to_blocks(markdown) -> list[str]:
    split_list = markdown.split("\n\n")

    return list(map(lambda x: x.strip(), filter(lambda x: len(x) > 0, split_list)))

def block_to_block_type(block: str):
    # Check for header by seeing if it starts with #'s
    # Currently not sure if I should implement if it's header 1-6 so a basic header check will do
    if block.startswith("#"):
        return "header"
    # Check if the block is a code 
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    pass
