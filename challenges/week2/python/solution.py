def classify_arch(arch: list[list[int]]) -> str:
    """
    Evaluate the similarity of the received arch with the given examples of charts. The most similar is your solution
    
    Args:
        arch (list[list[int]]): Matrix with the given arch. The parts marked with 1 are filled 
                                and those with 0 are empty spaces, keep in mind when 2 appears.

    Returns:
        str: Name of the arch period as it appears on challenge.md.
    """
    
    patterns = {
        "Romanos": [
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        "Abderraman I": [
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ],
        "Abderraman II": [
            [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        ],
        "Al-Hakam II": [
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        ],
        "Almanzor": [
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
    }

    best_match = None
    max_matches = -1

    input_rows = len(arch)
    if input_rows == 0:
        return ""
    input_cols = len(arch[0])

    for name, pattern in patterns.items():
        pattern_rows = len(pattern)
        if pattern_rows != input_rows:
            continue
        
        pattern_cols = len(pattern[0])
        match_cols = min(input_cols, pattern_cols)
        
        current_matches = 0
        
        for r in range(input_rows):
            for c in range(match_cols):
                if arch[r][c] == pattern[r][c]:
                    current_matches += 1
        
        if current_matches > max_matches:
            max_matches = current_matches
            best_match = name
            
    return best_match
