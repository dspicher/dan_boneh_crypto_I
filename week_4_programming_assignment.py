import copy
import urllib.request
import urllib.error
import sys
from IPython import embed

TARGET = 'http://crypto-class.appspot.com/po?er='


class PaddingOracle(object):
    def query(self, q):
        target = TARGET + q
        try:
            f = urllib.request.urlopen(target)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return True
            return False


def xor_padding_oracle(c, xor_start_pos, xor_len, xor_val, guesses):
    c_mod = copy.deepcopy(c)
    for idx, i in enumerate(range(xor_start_pos, xor_start_pos+xor_len)):
        c_mod[i] = c_mod[i] ^ xor_val ^ guesses[idx]
    return c_mod


if __name__ == "__main__":
    real_arg = list(bytes.fromhex(
        "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"))
    po = PaddingOracle()
    cleartext = [[[] for _ in range(16)] for __ in range(3)]
    for clear_text_block in range(3):
        cut_arg = real_arg[:16*(clear_text_block+2)]
        print("clear text block {}".format(clear_text_block))
        guessed = []
        for byte_pos in range(16):
            xor_start_pos = (clear_text_block+1)*16-(byte_pos+1)
            print("byte pos {}".format(xor_start_pos))
            xor_len = byte_pos+1
            xor_val = byte_pos+1
            for guess in range(256):
                to_query = xor_padding_oracle(
                    cut_arg, xor_start_pos, xor_len, xor_val, [guess]+guessed)
                to_query = bytes(to_query).hex()
                res = po.query(to_query)
                if res:
                    print("found byte: {}".format(guess))
                    cleartext[clear_text_block][15-byte_pos] = guess
                    guessed = [guess] + guessed
                    break
                # hack for when we submit original message
                if res is None and clear_text_block == 2 and byte_pos == 8:
                    print("found byte: {}".format(guess))
                    cleartext[clear_text_block][15-byte_pos] = guess
                    guessed = [guess] + guessed
                    break

    print(cleartext)
    embed()
