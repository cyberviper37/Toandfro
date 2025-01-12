global w1, w2, b
w1, w2, b = 0.5, 0.5, -1
global i
i = 0
def activate(x):
    return 0 if x <= 0 else 1

def train(input, desired_output, b, epoch):
    for epoch in range(epoch):
        A, B = input[i]
        target_output = desired_output[i]
        output = activate(w1 * A + w2 * B + b)
        error = target_output - output
        w1 = w1 * error * A
        w2 = w2 * error * B    
        b = b * error
        i = i + 1
        i = i / epoch
        return output
    
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
d_output = [0, 0, 0, 1]
output = train(inputs, d_output, b, 50)
print(output)
