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


# Solutions for https://adventofcode.com/2023/day/13.

print(
    (
        vertical_mirror := lambda pattern, index: all(
            not (
                2 * index - k - 1 < len(pattern[j])
                and pattern[j][k] != pattern[j][2 * index - k - 1]
            )
            for j in range(len(pattern))
            for k in range(index)
        )
    )
    and (
        horizontal_mirror := lambda pattern, index: all(
            not (
                2 * index - k - 1 < len(pattern)
                and pattern[k][j] != pattern[2 * index - k - 1][j]
            )
            for j in range(len(pattern[0]))
            for k in range(index)
        )
    )
    and (
        summarize := lambda pattern: next(
            __import__("itertools").chain(
                (i for i in range(1, len(pattern[0])) if vertical_mirror(pattern, i)),
                (
                    i * 100
                    for i in range(1, len(pattern))
                    if horizontal_mirror(pattern, i)
                ),
                [0],
            )
        )
    )
    and (
        input_ := (__import__("pathlib").Path(__file__).parent / "day13_e.txt")
        .read_text()
        .split("\n\n")
    )
    and sum(summarize(pattern) for pattern in [block.splitlines() for block in input_])
)

print(
    (
        vertical_mirror := lambda pattern, index, smudged_at: (
            (smudged_at < 2 * index and smudged_at >= 2 * index - len(pattern[0]))
            and all(
                not (
                    2 * index - y - 1 < len(pattern[x])
                    and pattern[x][y] != pattern[x][2 * index - y - 1]
                )
                for x in range(len(pattern))
                for y in range(index)
            )
        )
    )
    and (
        horizontal_mirror := lambda pattern, index, smudged_at: (
            (smudged_at < 2 * index and smudged_at >= 2 * index - len(pattern))
            and all(
                not (
                    2 * index - x - 1 < len(pattern)
                    and pattern[x][y] != pattern[2 * index - x - 1][y]
                )
                for y in range(len(pattern[0]))
                for x in range(index)
            )
        )
    )
    and (
        smudge := lambda pattern, x, y: (
            (smugged := [list(line) for line in pattern])
            and (
                smugged[x].__setitem__(y, "#" if smugged[x][y] == "." else ".") or True
            )
            and ["".join(line) for line in smugged]
        )
    )
    and (
        summarize := lambda pattern: next(
            __import__("itertools").chain(
                (
                    index
                    for index in range(1, len(pattern[0]))
                    for x in range(len(pattern))
                    for y in range(len(pattern[0]))
                    if vertical_mirror(smudge(pattern, x, y), index, y)
                ),
                (
                    index * 100
                    for index in range(1, len(pattern))
                    for x in range(len(pattern))
                    for y in range(len(pattern[0]))
                    if horizontal_mirror(smudge(pattern, x, y), index, x)
                ),
            )
        )
    )
    and (
        input_ := (__import__("pathlib").Path(__file__).parent / "day13.txt")
        .read_text()
        .split("\n\n")
    )
    and sum(summarize(pattern) for pattern in [block.splitlines() for block in input_])
)
