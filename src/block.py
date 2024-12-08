from src.textnode import TextNode, TextType
from enum import Enum
from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.inline import *
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ORDERED_LIST = "ordered_list"
    UNORDERED_LIST = "unordered_list"


def markdown_to_blocks(markdown: str) -> list[tuple[str, BlockType]]:
    split_block_list = markdown.split("\n\n")
    santized_block_list : list[str] = list(map(lambda x: x.strip(), filter(lambda x: len(x) > 0, split_block_list)))
    block_types : list[BlockType] = []
    tag_removed_block_list : list[str] = []
    for block in santized_block_list:
        block_type = determine_block_type(block)
        block_types.append(block_type)
        tag_removed_block_list.append(remove_markdown_syntax_from_block(block, block_type))

    result = list(zip(tag_removed_block_list, block_types))
    return result

def determine_block_type(block: str):
    # Check for header by seeing if it starts with #'s
    # Currently not sure if I should implement if it's header 1-6 so a basic header check will do
    if block.startswith("#"):
        return BlockType.HEADING
    # Check if the block is a code 
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith('>'):
        return BlockType.QUOTE
    elif block.startswith(("-", "*")):
        return BlockType.UNORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_html(markdown) -> ParentNode:
    # Convert the markdown to blocks
    blocks = markdown_to_blocks(markdown)
    output_nodes = []
    for block in blocks:
        children = text_to_textnodes(block)
        # Here's a regex for finding the markdown syntax: https://regexr.com/894il
        output_nodes.append(block_to_node(block[0], block[1], children))
        pass

    return ParentNode("div", output_nodes)


def block_to_node(block: str, block_type: BlockType, children: list[TextNode]) -> ParentNode:
    '''
    We want to convert with a block to a HTMLNode with potential children that are
    also nodes
    '''
    # Turn the children blocks into leafnodes
    child_nodes = [child.to_leafNode() for child in children]
    # Return ParentNode
    match block_type:
        case BlockType.HEADING:
            return ParentNode("h1", child_nodes) #TODO: Need a way to determine children AND header
        case BlockType.CODE:
            return ParentNode("pre", child_nodes)
        case BlockType.QUOTE:
            return ParentNode("blockquote", child_nodes)
        case BlockType.ORDERED_LIST:
            return ParentNode("ol", child_nodes)
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", child_nodes)
        case _:
            return ParentNode("p", child_nodes)

def remove_markdown_syntax_from_block(block: str, block_type:BlockType) -> str:
    match block_type:
        case BlockType.HEADING:
            return block.replace("#", "").strip()
        case BlockType.CODE:
            return block.replace("```", "").strip()
        case BlockType.QUOTE:
            return block.replace(">", "").strip()
        case BlockType.ORDERED_LIST:
            return block.replace("-", "").strip()
        case BlockType.UNORDERED_LIST:
            return block.replace("*", "").strip()
        case _:
            return block
    