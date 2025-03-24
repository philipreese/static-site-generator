from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def block_to_block_type(markdown):
    split = list(filter(lambda x: x != "", markdown.split("\n")))

    if len(split) == 1:
        match = re.findall(r"#+ ", markdown)
        if len(match) == 0:
            return BlockType.PARAGRAPH
        return BlockType.HEADING

    if split[0] == "```" and split[-1] == "```":
        return BlockType.CODE

    quote_count = ordered_count = unordered_count = 0
    for line in split:
        if line.startswith("> "):
            quote_count += 1
        elif len(re.findall(r"\d. ", line)) > 0:
            ordered_count += 1
        elif line.startswith("- "):
            unordered_count += 1
    if quote_count > 0:
        return BlockType.QUOTE
    if ordered_count > 0:
        return BlockType.OLIST
    if unordered_count > 0:
        return BlockType.ULIST


def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")
    stripped_blocks = map(lambda x: x.strip("\n"), blocks)
    filtered_blocks = filter(lambda x: x != "", stripped_blocks)
    return list(filtered_blocks)
