# Copyright 2023 Yilei Yang.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Solutions for https://adventofcode.com/2023/day/6.

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day06.txt")
        .read_text()
        .splitlines()
    )
    and (times := list(map(int, input_[0].split(":")[1].split())))
    and (distances := list(map(int, input_[1].split(":")[1].split())))
    and (
        counter := lambda t, d: (
            int((t + __import__("math").sqrt(t * t - 4 * d)) / 2)
            - int(
                __import__("math").ceil(
                    max(0, (t - __import__("math").sqrt(t * t - 4 * d)) / 2)
                )
            )
            + 1
        )
    )
    and (counts := [counter(t, d + 1) for t, d in zip(times, distances)])
    and __import__("functools").reduce(int.__mul__, counts, 1)
)

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day06.txt")
        .read_text()
        .splitlines()
    )
    and (time := int("".join(input_[0].split(":")[1].split())))
    and (distance := int("".join(input_[1].split(":")[1].split())))
    and (
        counter := lambda t, d: (
            int((t + __import__("math").sqrt(t * t - 4 * d)) / 2)
            - int(
                __import__("math").ceil(
                    max(0, (t - __import__("math").sqrt(t * t - 4 * d)) / 2)
                )
            )
            + 1
        )
    )
    and counter(time, distance + 1)
)
