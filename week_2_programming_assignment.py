from IPython import embed
from Crypto.Cipher import AES

BLOCKSIZE = 16


def cbc_decrypt(key, iv, cyphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    N_rounds = int(len(cyphertext) / BLOCKSIZE)
    xor_arg = iv
    result = []
    for round_i in range(N_rounds):
        to_decrypt = cyphertext[round_i*BLOCKSIZE:(round_i+1)*BLOCKSIZE]
        decrypted = cipher.decrypt(to_decrypt)
        curr_round = [decrypted[i] ^ xor_arg[i] for i in range(BLOCKSIZE)]
        result += curr_round
        xor_arg = to_decrypt
    return result


def cbc_encrypt(key, iv, cleartext):
    cipher = AES.new(key, AES.MODE_ECB)
    N_rounds = int(len(cleartext) / BLOCKSIZE)
    xor_arg = iv
    result = []
    for round_i in range(N_rounds):
        to_encrypt = [cleartext[round_i*BLOCKSIZE+i] ^ xor_arg[i]
                      for i in range(BLOCKSIZE)]
        encrypted = cipher.encrypt(bytes(to_encrypt))
        result += encrypted
        xor_arg = encrypted
    return result


def ctr_decrypt(key, iv, cyphertext):
    result = []
    for i in range(int(len(cyphertext)/BLOCKSIZE)+1):
        to_decrypt = cyphertext[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
        curr_encrypt = iv[:-1] + bytes([iv[-1]+i])
        cipher = AES.new(key, AES.MODE_ECB)
        xor_arg = cipher.encrypt(curr_encrypt)
        decrypted = [a ^ b for (a, b) in zip(to_decrypt, xor_arg)]
        result += decrypted
    return result


def ctr_encrypt(key, iv, cleartext):
    result = []
    for i in range(int(len(cleartext)/BLOCKSIZE)+1):
        to_encrypt = cleartext[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
        curr_encrypt = iv[:-1] + bytes([iv[-1]+i])
        cipher = AES.new(key, AES.MODE_ECB)
        xor_arg = cipher.encrypt(curr_encrypt)
        encrypted = [a ^ b for (a, b) in zip(to_encrypt, xor_arg)]
        result += encrypted
    return result


def do_cbc(key_hex, cyphertext_hex):
    key = bytes.fromhex(key_hex)
    cyphertext = bytes.fromhex(cyphertext_hex)
    iv = cyphertext[:BLOCKSIZE]
    decrypted = bytes(cbc_decrypt(
        key, iv, cyphertext[BLOCKSIZE:]))
    print(decrypted[:-decrypted[-1]])
    encrypted = cbc_encrypt(key, iv, decrypted)
    assert((iv+bytes(encrypted)).hex() == cyphertext_hex)


def do_ctr(key_hex, cyphertext_hex):
    key = bytes.fromhex(key_hex)
    cyphertext = bytes.fromhex(cyphertext_hex)
    iv = cyphertext[:BLOCKSIZE]
    decrypted = bytes(ctr_decrypt(
        key, iv, cyphertext[BLOCKSIZE:]))
    print(decrypted)
    encrypted = ctr_encrypt(key, iv, decrypted)
    assert((iv+bytes(encrypted)).hex() == cyphertext_hex)


cyphertext_hex = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
key = "140b41b22a29beb4061bda66b6747e14"
do_cbc(key, cyphertext_hex)

cyphertext_hex = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
key = "140b41b22a29beb4061bda66b6747e14"
do_cbc(key, cyphertext_hex)

cyphertext_hex = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
key = "36f18357be4dbd77f050515c73fcf9f2"
do_ctr(key, cyphertext_hex)

cyphertext_hex = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
key = "36f18357be4dbd77f050515c73fcf9f2"
do_ctr(key, cyphertext_hex)
