"""
Generator on the Collatz Conjecture (v1.0).
Created within the Project "DevLounge".
Licenced under the European Union Public License (EUPL) 1.2
Copyright (c) 2023 Daniel Siebke, Benjamin Siebke

Visit our website: https://dev-lounge.org.
"""

import functools
import time

cache: dict = {}


def get_num_iterations(num: int):
    if num in cache.keys():
        return cache[num]

    nums: list = []

    cache[num] = 0
    x: int = num
    while x != 1:
        x = x // 2 if x % 2 == 0 else x * 3 + 1

        cache[num] += 1
        if x in cache.keys():
            cache[num] += cache[x]
            for n in nums:
                cache[n] = cache[num] - cache[n]
            return cache[num]
        cache[x] = cache[num]
        nums.append(x)

    n: int
    for n in nums:
        cache[n] = cache[num] - cache[n]

    return cache[num]


@functools.cache
def calc(step: int) -> int:
    return step // 2 if step % 2 == 0 else step * 3 + 1


def get_range(n_range: range, *args):
    if args[0]:         # if fast mode
        start_time: float = time.time()
        stop_time: float
        i: int

        for i in n_range:
            get_num_iterations(i)

        stop_time = time.time()

        print("\nDone, generating stats data...")

        max_iter: int = 0
        max_iter_num: int = 0

        if args[1]:
            iter_counts: str = ("\nNumbers with iteration counts:\n"
                                "----------------------------------------------------\n")

            for i in n_range:
                iter_counts += f"{i}: {cache[i]}\n"

                if cache[i] > max_iter:
                    max_iter, max_iter_num = cache[i], i
            iter_counts += "----------------------------------------------------"

            print(iter_counts)
        else:
            for i in n_range:
                if cache[i] > max_iter:
                    max_iter, max_iter_num = cache[i], i

        print(f"\nStats:\n"
              f"----------------------------------------------------",
              f"Number range: {n_range.start} - {n_range.stop - 1}",
              f"Most iterations at number {max_iter_num}: {max_iter} iterations",
              f"Time elapsed: {round((stop_time - start_time) * 1000)} ms",
              f"----------------------------------------------------", sep="\n")

    # -------------------------------------------------- #

    else:                   # if detailed mode
        start: int = n_range.start
        stop: int = n_range.stop - 1
        step: int = start
        global_max_step: list = []
        global_len_step: list = []
        global_max: int = 0
        global_len: int = 0
        current_max: int
        current_len: int
        lst: list

        stop_time: float
        start_time: float = time.time()

        while step <= stop:
            val: int = step
            lst = [val]
            while not val == 1:
                val = calc(val)
                lst.append(val)
            if args[1]:
                print(f"\n{lst}")

            # handle stats
            current_max = max(lst)
            current_len = len(lst) - 1
            if args[1]:
                print(f"--> max: {current_max}, len: {current_len}")

            if current_max > global_max:
                global_max, global_max_step = current_max, [step]
            elif current_max == global_max:
                global_max_step.append(step)

            if current_len > global_len:
                global_len, global_len_step = current_len, [step]
            elif current_len == global_len:
                global_len_step.append(step)

            step += 1

        stop_time = time.time()

        print(f"\nStats:",
              f"----------------------------------------------------",
              f"Number Range: {start} - {stop}",
              f"Biggest Numb: {global_max_step} --> max: {global_max}",
              f"Longest Term: {global_len_step} --> len: {global_len}",
              f"Time elapsed: {round((stop_time - start_time) * 1000)} ms",
              f"----------------------------------------------------", sep="\n")


if __name__ == "__main__":
    print('Generator on the Collatz Conjecture (v1.0).',
          'Created within the Project "DevLounge".',
          'Licenced under the European Union Public License (EUPL) 1.2',
          'Copyright (c) 2023 Daniel Siebke, Benjamin Siebke',
          '',
          'Visit our website: https://dev-lounge.org.', sep="\n", end="\n\n\n")

    while True:
        try:
            gen_args: list[str, str] = [input("Use fast mode (less detailed stats but much faster)? (y/n): ") in "Yy",
            				  			input("Print iteration counts for each number? (y/n): ") in "Yy"]
            get_range(range(max(int(input("Enter a start point: ")), 1),
                            max(int(input("Enter a stop point: ")) + 1, 1)), *gen_args)
            break
        except ValueError:
            print("Please enter a number, not a string.\n")
