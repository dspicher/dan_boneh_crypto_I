from IPython import embed
import hashlib
from functools import reduce


def do(file):
    print(file)
    with open(file, "rb") as f:
        all_bytes = []
        byte = f.read(1)
        all_bytes.append(byte)
        while byte:
            byte = f.read(1)
            all_bytes.append(byte)
    last_block_length = len(all_bytes) % 1024
    prev_hash = b""
    for start_idx in range(0, len(all_bytes), 1024)[::-1]:
        curr_block = all_bytes[start_idx:start_idx+1024]
        digest = reduce(lambda x, y: x+y, curr_block)
        to_hash = digest + prev_hash
        m = hashlib.sha256(to_hash)
        prev_hash = m.digest()
    print(prev_hash.hex())


do("6.1.intro.mp4_download")
do("6.2.birthday.mp4_download")
