def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    a = list1+list1[-1::-1]
    return a
print(main([2,4,6,7]))