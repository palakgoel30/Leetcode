def canConstruct(ransomNote, magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    for i in ransomNote:
        if (i in magazine):
            magazine.remove(i)
        else:
            return False
    return True

ransomNote = 'aa'
magazine = 'aab'
print(canConstruct(ransomNote, magazine))