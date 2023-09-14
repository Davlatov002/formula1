# Ba'zi harf tugmachalari ishlamaydigan noto'g'ri ishlaydigan klaviatura mavjud. Klaviaturadagi barcha boshqa tugmalar to'g'ri ishlaydi.

# Bitta boʻsh joy bilan ajratilgan soʻzlar qatori (boshlovchi yoki keyingi boʻshliqlar yoʻq) va singan barcha alohida harf tugmalarining 
# singan harflari qatori berilgan boʻlsa, ushbu klaviatura yordamida toʻliq kiritishingiz mumkin boʻlgan matndagi soʻzlar sonini qaytaring.

def canBeTypedWords(text: str, brokenLetters: str) -> int:
    s, a = text.split(), 0
    for i in s:
        b = 0
        for n in brokenLetters:
            if n not in i:
                b += 1
        if b == len(brokenLetters):
            a += 1      
    return a

print(canBeTypedWords("hello world", "da"))
