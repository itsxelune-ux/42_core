#!/usr/bin/env python3

def average(scores_dict):
    if not scores_dict:  # handle empty dictionary
        return 0
    total = sum(scores_dict.values())  # sum all the scores
    count = len(scores_dict)           # number of students
    return total / count                # return the average


if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")