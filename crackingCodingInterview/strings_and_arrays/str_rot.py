# String Rotation: Assume you have a method i5Substring which checks ifone word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to isSubstring (e.g., Uwaterbottleuis a rotation of uerbottlewat U).


def str_rot(s1: str, s2: str) -> bool:
    if len(s1) != len(s1):
        return False
    s3 = s2 + s2
    return s3.find(s1)


if __name__ == "__main__":
    print(str_rot("waterbttle", "bottlewater"))
    print(str_rot("waterbottle", "bottlewater"))
