def class_to_json(obj):
    """
    Converts an instance of a class to a JSON-serializable dictionary.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the serialized attributes of the object.
    """
    # Initialize an empty dictionary to store the serialized data
    serialized_data = {}

    # Get the list of attributes of the object
    attributes = dir(obj)

    for attr in attributes:
        # Check if the attribute is not a special method (e.g., __init__)
        if not attr.startswith('__'):
            # Get the attribute value
            attr_value = getattr(obj, attr)

            # Check if the attribute is serializable (list, dict, str, int, bool)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                serialized_data[attr] = attr_value

    return serialized_data
