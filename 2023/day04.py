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


# Solutions for https://adventofcode.com/2023/day/4.


print(
    sum(
        (
            (parts := line.split(":")[1].split("|"))
            and (wins := set(parts[0].split()))
            and (count := sum(1 for n in parts[1].split() if n in wins))
            and 2 ** (count - 1)
        )
        for line in (__import__("pathlib").Path(__file__).parent / "day04.txt")
        .read_text()
        .splitlines()
    )
)


print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day04.txt")
        .read_text()
        .splitlines()
    )
    and (cards := [1] * len(input_))
    and sum(
        (
            (parts := line.split(":")[1].split("|"))
            and (wins := set(parts[0].split()))
            and (count := sum(1 for n in parts[1].split() if n in wins))
            and sum(
                cards.__setitem__(i, cards[i] + cards[index]) or 1
                for i in range(index + 1, index + 1 + count)
            )
        )
        for index, line in enumerate(input_)
    )
    and sum(cards)
)
