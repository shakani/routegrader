def convert_grade(grade_scaled: float) -> str:
    """
    Converts the standard scaler grade after inverse transform into 
    a string representing the rock climbing grade
    
    0 maps to 5+
    18 maps to 8C+
    """
    grade_dict = {
                '5+' : 0,
                '6A' : 1,
                '6A+' : 2,
                '6B' : 3,
                '6B+' : 4,
                '6C' : 5,
                '6C+' : 6,
                '7A' : 7,
                '7A+' : 8,
                '7B' : 9,
                '7B+' : 10,
                '7C' : 11,
                '7C+' : 12,
                '8A' : 13,
                '8A+' : 14,
                '8B' : 15,
                '8B+' : 16,
                '8C' : 17,
                '8C+' : 18
            }
    grade_dict_inverse = {val : key for key, val in grade_dict.items()}
    closest, remainder = divmod(grade_scaled, 1)
    closest = grade_dict_inverse.get(int(closest), 'Too hard!!')
    remainder = round(remainder, 3) * 100
    return f"{closest} plus {remainder : .3f}%"