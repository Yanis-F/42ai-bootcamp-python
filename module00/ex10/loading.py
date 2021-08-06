from typing import List
import time

def ft_progress(lst: List[int]):
    for e in lst:
        yield e


listy = range(3333)
ret = 0

done_count = 0
start_time = time.time()
for elem in ft_progress(listy):
    ret += (elem + 3) % 5

    time.sleep(0.007)
    done_count += 1

    elapsed_time = time.time() - start_time
    progress = (done_count) / len(listy)
    eta = elapsed_time * (len(listy) - done_count) / done_count
    ARROW_MAX_LENGTH = 20

    print(f"ETA: {eta:.2f}s [{progress*100:3.0f}%][{'=' * int((ARROW_MAX_LENGTH - 1) * progress) + '>':{ARROW_MAX_LENGTH}s}] {done_count}/{len(listy)} | elapsed time {elapsed_time:.2f}")



print()
print(ret)