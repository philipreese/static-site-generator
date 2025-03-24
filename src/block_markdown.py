def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")
    stripped_blocks = map(lambda x: x.strip("\n"), blocks)
    filtered_blocks = filter(lambda x: x != "", stripped_blocks)
    return list(filtered_blocks)
