from IPython import embed


# XOR-ing the two L2s will result in all 1s
def question_4():
    patterns = [["e86d2de2 e1387ae9",
                 "1792d21d b645c008", ],
                ["5f67abaf 5210722b",
                 "bbe033c0 0bc9330e"],
                ["7c2822eb fdc48bfb",
                 "325032a9 c5e2364b"],
                ["7b50baab 07640c3d",
                 "ac343a22 cea46d60"]]
    patterns2 = [["290b6e3a 39155d6f",
                  "d6f491c5 b645c008", ],
                 ["5f67abaf 5210722b",
                  "bbe033c0 0bc9330e"],
                 ["9d1a4f78 cb28d863",
                  "75e5e3ea 773ec3e6"],
                 ["7b50baab 07640c3d",
                  "ac343a22 cea46d60"]]
    for i, pattern in enumerate(patterns2):
        print(i+1)
        parts = list(map(lambda x: x.split(" "), pattern))
        left00 = bytes.fromhex(parts[0][0])
        left10 = bytes.fromhex(parts[1][0])
        print([a ^ b for (a, b) in zip(left00, left10)])


def question_8():
    msgs = ['To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.',
            'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.',
            'We see immediately that one needs little information to begin to break down the process.',
            'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.',
            'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.',
            'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.']
    used = [msgs[4], msgs[1], msgs[3], msgs[5]]
    print([128 - 16 - len(bytes(msg, encoding='ascii')) for msg in used])


question_4()
question_8()
