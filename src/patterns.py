import re

COMMON_PATTERNS=[
    "password",
    "iLoveyou",
    "admin",
    "lecturer",
    "mpnkey",
    "dragon",
    "nopassword",
    "footbal",
    "iphone",
    "noname",
    "Hello",

]
def detect_patterns(password):
    Warning=[]

    password_lower=password.lower()

    for patterns in COMMON_PATTERNS:
        if patterns in password_lower:
            Warning.append(
                f"contain password patterns: '{patterns}'"
            )

        if re.search(r"(.)\1{2,}", password):
            Warning.append("contin repeated characters")

        sequential_numbers=[
            "012345",
            "123456",
            "234567",
            "345678",
            "456789",
            "567890",
            "678901",
            "789012",
            "890123",
            "901234",
        ]

        for sequence in sequential_numbers:
            if sequence in password:
                Warning.append("contains a predictable number squence")
                break

        sequencial_letters=[
            "abcdef",
            "bcdefg",
            "cdefgh",
            "defghi",
            "efghij",
            "fghijk",
            "ghijkl",
            "hijklm",
            "ijklmn",
            "jklmno",
            "klmnop",
            "lmnopq",
            "mnopqr",
            "nopqrs",
            "opqrst",
            "pqrstu",
            "qrstuv",
            "rstuvw",
            "stuvwx",
            "tuvwxy",
            "uvwxyz",
            "vwxyza",
            "wxyzab",
            "xyzabc",
            "yzabcd",
            "zabcde",
        ]

        for sequence in sequencial_letters:
            if sequence in password_lower:
                Warning.append("contains a predictable letter sequence")
                break

        return Warning
