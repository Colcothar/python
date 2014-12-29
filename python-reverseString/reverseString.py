def reverse(text):
    count = 0
    for c in text:
        count +=1
    print count
    l = count - 1
    rev_list = [""]
    for char in text:
        print text[l],
        rev_list.append(text[l])
        l -= 1
    return "".join(rev_list)
reverse("hello")
reverse("Python!")
print