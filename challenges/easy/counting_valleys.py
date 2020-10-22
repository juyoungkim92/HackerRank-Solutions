"""
HackerRank challenge link: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

Counting Valleys

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, ,
or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path

Returns: int: the number of valleys traversed

Sample Input:

n = 8
s = "UDDDUDUU"

Output: 1

"""


def counting_valleys(path):
    """
    :param path: single string path that describe step
    :return: number of valleys traversed (integer value)

    Function explanation

    We initialise valley and sea_level as 0. And we count how many times the Up or Down steps were in the path.
    A valley always ends with a step up to a sea level. Sea level is 0. Thus we say when the sea level is 0 and
    the character in the PATH is "U", we increment the valley by 1. At the end return how many times the valleys were hiked.
    """

    valley = 0
    sea_level = 0

    for c in path:
        if c == "U":
            sea_level += 1
        else:
            sea_level -= 1
        if c == "U" and sea_level == 0:
            valley += 1

    return valley
