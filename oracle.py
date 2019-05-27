from collections import Counter

class Model:
    def __init__(self, CHARSET, MAX_GRAM_LENGTH):
        self.data = {}
        self.input = ""
        self.CHARSET = charset
        self.MAX_GRAM_LENGTH = MAX_GRAM_LENGTH

    def __update(self, gram, x):
        if gram not in self.data:
            self.data[gram] = {c: 0 for c in self.CHARSET}
        self.data[gram][x] += 1

    def __predict(self, gram):
        if gram not in self.data:
            return None
        else:
            x, _ = max(
                self.data[gram].items(),
                key=lambda t: t[1] # count of gram
            )
            return x

    def feed(self, xs):
        if not all(x in self.CHARSET for x in xs):
            raise ValueError(
                'Input \'{}\' contains characters not in CHARSET "{}".'.format(
                    xs,
                    self.CHARSET
                )
            )

        for x in xs:
            gram = self.input[-self.MAX_GRAM_LENGTH:]
            self.input += x

            # break up a gram into multiple grams of decreasing size
            # e.g. "abcdef" is broken up into "abcedf", "bcdef", ..., "ef", "f"
            for i in range(len(gram)):
                self.__update(gram[i:], x)

    def guess(self):
        gram = self.input[-self.MAX_GRAM_LENGTH:]
        # predict using the largest gram available
        for i in range(len(gram)):
            x = self.__predict(gram[i:])
            if not x is None:
                return x
        return self.CHARSET[0] # fallback if model has not enough data

