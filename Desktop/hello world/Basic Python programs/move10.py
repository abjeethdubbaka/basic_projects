def encode(s, k):
    # changed string
    newS = ""

    # iterate for every characters
    for i in range(len(s)):

        # ASCII value
        val = ord(s[i])

        # store the duplicate
        dup = k

        # if k-th ahead character exceed 'z'
        if val + k > 122:
            k -= (122 - val)
            k = k % 26
            newS += chr(96 + k)

        else:
            newS += chr(val + k)

        k = dup

        # print the new string
    print(newS)