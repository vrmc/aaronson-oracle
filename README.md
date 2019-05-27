# Aaronson Oracle

This project provides the base code you would need to build a two-button
pressor predictor on the Raspberry Pi.

## How To Use `oracle.py`

This repository comes with a Python module `oracle.py` which provides two
functions, `feed(xs)` and `guess()`, that will perform the prediction of the
next button to be pressed.

First of all, create a `Model` object. The initialisation function requires
`CHARSET`, a string which determines which characters can appear in the
input, and `MAX_GRAM_LENGTH`, an integer which determines the maximum length
of the n-gram (refer to **Technical Infosheet** for more details).

```python
from oracle import Model
m = Model('LR', 5) # L and R represent the left and right buttons respectively
                   # By default, we use 5 for MAX_GRAM_LENGTH
```

Upon initialisation, the model can be fed with training input, and will track
the input being fed in.

``python
# feed accepts a string of inputs, ordered from left to right
# This can be one char at a time...
m.feed("L")
m.feed("R")
m.feed("L")
# ...or a full string of inputs
m.feed("LRLRRRRLRLRLRLRLLLLRLRLRLLRRR")
```

At any point in time, you may use the model to make a prediction for the next
character with `m.guess()`, or observe all of the previous input fed into the
model with `m.input`.

## Technical Infosheet

This project was inspired by an implementation of the
[Aaronson Oracle](https://github.com/elsehow/aaronson-oracle). The model is a
n-gram model, which uses Markov Chains to predict the next input.

Rather than processing only n-grams, the model is modified to account for
smaller grams, and makes the prediction based on the largest available gram
found. This should improve accuracy when dealing with low amounts of input
(which is expected when using push buttons to record the input from the user,
due to their latency).

