# Neural Network Forward Pass
# QA-4 | Artificial Intelligence

import math

# -------- Activation Functions --------
def relu(x):
    return max(0, x)

# -------- Input Layer --------
x1 = 2
x2 = 3

print("Input Layer:")
print("x1 =", x1)
print("x2 =", x2)

# -------- Hidden Layer --------
w1 = 0.5
w2 = 0.8
bias_hidden = 1

hidden_sum = (x1 * w1) + (x2 * w2) + bias_hidden
hidden_output = relu(hidden_sum)

print("\nHidden Layer Calculation:")
print("Weighted Sum =", hidden_sum)
print("After ReLU =", hidden_output)

# -------- Output Layer --------
w3 = 1.2
bias_output = 0.5

final_sum = (hidden_output * w3) + bias_output

print("\nOutput Layer Calculation:")
print("Final Output =", final_sum)
