'''
map(): used to transform values of a Series using a mapping (function, dict, or Series)

Syntax:
    Series.map(arg, na_action=None)

Parameters:
    arg        - function, dictionary, or Series used for mapping
    na_action  - 'ignore' to skip NaN values

What it Does:
    Replaces or transforms each value of a Series based on the given mapping
    Works ONLY on Series (not DataFrame)

Examples:
    s.map(lambda x: x * 2)
    s.map({'A': 1, 'B': 2})
    df['Grade'].map({'A': 'Excellent', 'B': 'Good'})

Notes:
    • If a value is not found in the mapping, result is NaN
    • Faster and cleaner for single-column transformations
'''