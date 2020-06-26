#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

"""
Lets take an example where you want to use a dropout coefficient of 0.5 in layer 2 of your network.

During training:
The outputs/activations of layer 2 are multiplied elementwise with a binary mask where the probability of each element of the mask being 1 is 0.5 (zero otherwise):

Without dropout: 𝑦2=𝑓(𝑧2)
With dropout: 𝑦2=𝑓(𝑧2)∘𝑚2

where 𝑓() is the activation function (e.g. tanh or ReLU), ∘ is an elementwise multiplication operation, 𝑧2 is the input vector of layer 2, 𝑚2 is the binary dropout mask and 𝑦2 is layer 2 output/activation vector.

During testing/validation:
Inputs 𝑧3 to layer 3 are computed as follows:

Without dropout: 𝑧3=𝑊3𝑦2
With dropout: 𝑧3=0.5𝑊3𝑦2

where 𝑦2 is the output/activation vector of layer 2 and 0.5 is the dropout coefficient of layer 2.

During backpropagation:

With dropout you need to multiply the derivative of 𝑦2 wrt. 𝑧2 with the same dropout mask 𝑚2 that you used during forward propagation.

A small code example:

(the rest of it is available here)

def forward(x, W1, W2, W3, training=False):
    z1 = np.dot(x, W1)
    y1 = np.tanh(z1)

    z2 = np.dot(y1, W2)
    y2 = np.tanh(z2)
    # Dropout in layer 2
    if training:
        m2 = np.random.binomial(1, 0.5, size=z2.shape)
    else:
        m2 = 0.5
    y2 *= m2

    z3 = np.dot(y2, W3)
    y3 = z3 # linear output

    return y1, y2, y3, m2

def backward(x, y1, y2, y3, m2, t, W1, W2, W3):
    dC_dz3 = dC(y3, t)
    dC_dW3 = np.dot(y2.T, dC_dz3)
    dC_dy2 = np.dot(dC_dz3, W3.T)

    dC_dz2 = dC_dy2 * dtanh(y2) * m2
    dC_dW2 = np.dot(y1.T, dC_dz2)
    dC_dy1 = np.dot(dC_dz2, W2.T)

    dC_dz1 = dC_dy1 * dtanh(y1)
    dC_dW1 = np.dot(x.T, dC_dz1)

    return dC_dW1, dC_dW2, dC_dW3
"""