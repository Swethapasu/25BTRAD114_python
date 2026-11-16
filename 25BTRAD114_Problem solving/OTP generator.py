import random
print("===== OTP GENERATOR =====")
length = int(input("Enter OTP length: "))
otp = ""
for i in range(length):
    otp = otp + str(random.randint(0, 9))
print("Generated OTP:", otp)
