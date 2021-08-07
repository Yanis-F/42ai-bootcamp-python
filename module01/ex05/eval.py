from typing import List

class Evaluator:

    def zip_evaluate(coefs: List[float], words: List[str]):
        if len(coefs) != len(words):
            return -1

        return sum(len(w) * c for w, c in zip(words, coefs))

    def enumerate_evaluate(coefs: List[float], words: List[str]):
        if len(coefs) != len(words):
            return -1

        return sum(coefs[idx] * len(w) for idx, w in enumerate(words))


