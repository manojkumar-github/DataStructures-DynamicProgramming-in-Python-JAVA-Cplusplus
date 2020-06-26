def reverseVowels(astring):
    astring = list(astring)
    left = 0
    right = len(astring)-1
    while left <= right:
        if astring[left] not in 'aeiouAEIOU':
            left += 1
            continue
        if astring[right] not in 'aeiouAEIOU':
            right -= 1
            continue
        if astring[left] in 'aeiouAEIOU' and astring[right] in 'aeiouAEIOU':
            astring[left], astring[right] = astring[right], astring[left]
            left += 1
            right -= 1
            continue
    return ''.join(astring)


astring = "AIRPLANE"
ex
print(reverseVowels(astring))

x = "Let's take LeetCode contest"
for each in x[::-1]:
    print(each)
print(x[::-1])