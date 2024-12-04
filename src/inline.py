from src.textnode import TextNode, TextType
import re

def text_to_textnodes(text) -> list[TextNode]:
    # First create a listh with 1 TextNode out of text
    list_textnodes = [TextNode(text, TextType.NORMAL)]
    # Then it has to go through split nodes delimiter 3 times
    delimiters = ["`", "**", "*"]
    for delimiter in delimiters:
        list_textnodes = split_nodes_delimiter(list_textnodes, delimiter)
    # then through split_nodes_images
    list_textnodes = split_nodes_images(list_textnodes)
    # and then finally through split_nodes_links.
    list_textnodes = split_nodes_links(list_textnodes)
    return list_textnodes


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter) -> list[TextNode]:

    md_delimiters = {"`": TextType.CODE, "*": TextType.ITALIC, "**": TextType.BOLD}

    if delimiter not in md_delimiters.keys():
        raise ValueError("Not a valid markdown delimiter")

    new_textnodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_textnodes.append(node)
        else:
            first_index = node.text.find(delimiter)
            words_list = node.text.split(delimiter)
            typetext_list = _generate_texttype_list(
                first_index, len(words_list), md_delimiters[delimiter]
            )
            words_with_typetext = zip(words_list, typetext_list)
            for wt in words_with_typetext:
                new_textnodes.append(TextNode(wt[0], wt[1]))

    return new_textnodes


def _generate_texttype_list(first_index, len_words, texttype):
    texttypes = []
    if first_index == 0:
        for i in range(len_words):
            if i % 2 == 0:
                texttypes.append(texttype)
            else:
                texttypes.append(TextType.NORMAL)
    else:
        for i in range(len_words):
            if i % 2 == 0:
                texttypes.append(TextType.NORMAL)
            else:
                texttypes.append(texttype)

    return texttypes


def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        image_matches = extract_markdown_images(node.text)

        if not image_matches:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for alt_text, url in image_matches:
            remaining_text = _split_and_insert_image_or_hyperlink(
                new_nodes, remaining_text, alt_text, url, TextType.IMAGE
            )

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))

    return new_nodes


def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        link_matches = extract_markdown_links(node.text)

        if not link_matches:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for alt_text, url in link_matches:
            remaining_text = _split_and_insert_image_or_hyperlink(
                new_nodes, remaining_text, alt_text, url, TextType.LINK
            )

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))

    return new_nodes


def _split_and_insert_image_or_hyperlink(
    new_nodes: list[TextNode],
    remaining_text: str,
    alt_text: str,
    url: str,
    texttype: TextType,
):
    if texttype == TextType.IMAGE:
        markdown_format = f"![{alt_text}]({url})"
    elif texttype == TextType.LINK:
        markdown_format = f"[{alt_text}]({url})"

    parts = remaining_text.split(markdown_format, 1)
    if parts[0]:
        new_nodes.append(TextNode(parts[0], TextType.NORMAL))
    new_nodes.append(TextNode(alt_text, texttype, url))
    remaining_text = parts[1]
    return remaining_text


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)
pass