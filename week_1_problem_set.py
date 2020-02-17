from IPython import embed


def question_7():
    encrypted = bytes.fromhex("6c73d5240a948c86981bc294814d")
    msg1 = bytes("attack at dawn", encoding='ascii')
    otp = [encrypted[i] ^ msg1[i] for i in range(len(msg1))]
    msg2 = bytes("attack at dusk", encoding='ascii')
    encrypted2 = bytes([otp[i] ^ msg2[i] for i in range(len(msg2))]).hex()
    otp2 = [bytes.fromhex(encrypted2)[i] ^ msg2[i] for i in range(len(msg2))]
    assert(all([otp[i] == otp2[i] for i in range(len(otp))]))
    print(encrypted2)


question_7()
