from name_function import (
    get_formatted_name,
    get_formatted_name_correct,
    get_formatted_name_incorrect,
)


def test_first_last_name():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
    formatted_name = get_formatted_name("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_first_last_name_incorrect():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
    formatted_name = get_formatted_name_incorrect("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_first_last_name_correct():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
    formatted_name = get_formatted_name_correct("janis", "joplin")
    assert formatted_name == "Janis Joplin"


def test_first_last_middle_name_correct():
    """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""
    formatted_name = get_formatted_name_correct("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"
