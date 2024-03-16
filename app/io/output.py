def output_text_to_console(text):
    """
    Output text to the console.
    Args:
        text (str): The text to be output to the console.
    Returns:
        None
    """
    print(text)


def output_text_to_file(text, file_path):
    """
    Output text to a text file.
    Args:
        text (str): The text to be written to the file.
        file_path (str): The path to the file where the text will be written.
    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(text)