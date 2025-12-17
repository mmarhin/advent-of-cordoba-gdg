def count_vulnerable_sections(stabilities: list[int], security_threshold: int) -> int:
    """
    Calculates the total number of contiguous vulnerable voussoir sections in the Roman Bridge.

    Args:
        stabilities (list[int]): A list of integers representing the stability index of each voussoir.
                                 Values range from 1 to 10.
        security_threshold (int): An integer defining the security threshold.
                                  A voussoir is vulnerable if its stability < security_threshold.

    Returns:
        int: The total number of vulnerable sections found.
    """
    # TODO: Write your code here
    if not stabilities:
        return 0
    
    sections = 0
    in_vulnerable_section = False
    
    for stability in stabilities:
        is_vulnerable = stability < security_threshold
        
        if is_vulnerable:
            if not in_vulnerable_section:
                # Starting a new vulnerable section
                sections += 1
                in_vulnerable_section = True
        else:
            # Stable voussoir - ends any current vulnerable section
            in_vulnerable_section = False
    
    return sections