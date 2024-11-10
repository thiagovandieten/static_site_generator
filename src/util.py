# from enum import Enum
from textnode import TextNode, TextType

def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter, text_type: TextType
) -> list[TextNode]:

    md_delimiters = {"`": TextType.CODE, "*": TextType.ITALIC, "**": TextType.BOLD}

    if delimiter not in md_delimiters.keys():
        raise AttributeError("Not a valid markdown delimiter")

    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            first_index = node.text.find(delimiter)
            words_list = node.text.split(delimiter)
            typetext_list = _generate_texttype_list(
                first_index, len(words_list), text_type
            )
            words_with_typetext = zip(words_list, typetext_list)
            for wt in words_with_typetext:
                new_nodes.append(TextNode(wt[0], wt[1]))

    return new_nodes


def _generate_texttype_list(first_index, len_words, texttype):
    texttypes = []
    if first_index == 0:
        for i in range(len_words):
            (
                texttypes.append(texttype)
                if i % 2 == 0
                else texttypes.append(TextType.NORMAL)
            )
    else:
        for i in range(len_words):
            (
                texttypes.append(TextType.NORMAL)
                if i % 2 == 0
                else texttypes.append(texttype)
            )

    return texttypes


# I didn't get to use this method but would still like to keep it incase.

# def _find_delimiter_in_line(string: str, delimiter: str, offset: int = 0) -> list[int]:
#     """A method to find the delimiters' indexes

#     This method returns a list of all the delimiter indexes.
#     Different methods can use this information to determine what is wrapped
#     within certain delimiters.

#     Args:
#         string: Perferably one line
#         delimiter: The delimiter is usually the markdown syntax
#         offset: Offset is used to remember the string's length through
#         the recursion.

#     Returns:
#         A list with indexes (int)

#     Raises:
#         AttributeError for a non markdown delimiter
#     """

#     index = string.find(delimiter)
#     if index == -1:
#         return []
#     elif delimiter == "*":
#         # We want to check if the character next to it is also a *, indicating a bold type
#         if string[index + 1] == "*":
#             new_offset = offset + index + 2
#             _find_delimiter_in_line(string[index + 2 :], delimiter, new_offset)

#     new_offset = offset + index + 1
#     list_indexes = _find_delimiter_in_line(string[index + 1 :], delimiter, new_offset)
#     list_indexes.insert(0, index + offset)

#     return list_indexes
