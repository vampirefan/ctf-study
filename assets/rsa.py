from Crypto.Util.number import inverse

# 已知的参数
p = 473398607161
q = 4511491
e = 17

# 计算 n 和 φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# 计算 d，使得 d ≡ e⁻¹ mod φ(n)
d = inverse(e, phi)

# 输出结果
print("d =", d)
