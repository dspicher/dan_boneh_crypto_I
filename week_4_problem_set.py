from IPython import embed

pay_100 = "000000000000000031000000"
pay_500 = "000000000000000035000000"
iv = "20814804c1767293b99f1d9cab3bc3e7"
payload = "ac1e37bfb15599e5f40eef805488281d"

pad_length = len(iv)-len(pay_100)
pay_100 += "0"*pad_length
pay_500 += "0"*pad_length

iv_bytes = bytes.fromhex(iv)
pay_100_bytes = bytes.fromhex(pay_100)
pay_500_bytes = bytes.fromhex(pay_500)

result = bytes([a ^ b ^ c for (a, b, c) in zip(
    iv_bytes, pay_100_bytes, pay_500_bytes)]).hex()
print(result + " " + payload)
