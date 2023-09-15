#rounding total to 2 decimal places for ratios such as 1/3
def get_options_ratio(option, total):
    ratio = round((option/total), 2)  
    return ratio

#
def get_faculty_rating(ratio):
    score = ""
    if .9 <= ratio <= 1:
        score = "Excellent"
    elif .8 <= ratio <.9:
        score = "Very Good"
    elif .7 <= ratio <.8:
        score = "Good"
    elif .6 <= ratio <.7:
        score = "Needs Improvement"
    elif 0 <= ratio <.6:
        score = "Unacceptable"
    else:
        score = "Invalid Rating"
    return score
    