def reverse(string):
    if len(string) == 0:
        return ""
    return reverse(string[1:]) + string[0]


print(reverse("wowzers"))

assert reverse("coolbeans") == "coolbeans"[::-1]