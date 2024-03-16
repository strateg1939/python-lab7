def get_text_input_from_console():
    """
    Get text input from the console.

    Returns:
        str: Text input entered by the user through the console.
    """
    text_input = input("Enter some text: ")
    return text_input


def get_text_from_file(file_path):
    """
    Read text from a file.

    Args:
        file_path (str): The path to the file from which to read text.

    Returns:
        str: Text read from the file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def get_text_from_file_using_pandas(file_path):
    """
    Read text from a file using pandas.

    Args:
        file_path (str): The path to the file from which to read text.

    Returns:
        str: Text read from the file.
    """
    import pandas as pd

    try:
        data = pd.read_csv(file_path, sep='\t', header=None)
        text = ' '.join(data[0].astype(str))
        return text
    except FileNotFoundError:
        return "File not found"
