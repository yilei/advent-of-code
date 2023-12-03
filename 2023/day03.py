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


# Solutions for https://adventofcode.com/2023/day/3.


# Puzzle 1.
# input_ = (
#     (__import__("pathlib").Path(__file__).parent / "day03.txt").read_text().splitlines()
# )
#
# answer = 0
# for line_index, line in enumerate(input_):
#     for m in __import__("re").finditer(r"\d+", line):
#         start, end = m.span()  # end is exclusive.
#         if (
#             (start > 0 and input_[line_index][start - 1] != ".")
#             or (end < len(line) and input_[line_index][end] != ".")
#             or (
#                 line_index > 0
#                 and any(
#                     c != "."
#                     for c in input_[line_index - 1][
#                         max(0, start - 1) : min(len(line), end + 1)
#                     ]
#                 )
#             )
#             or (
#                 line_index < len(input_) - 1
#                 and any(
#                     c != "."
#                     for c in input_[line_index + 1][
#                         max(0, start - 1) : min(len(line), end + 1)
#                     ]
#                 )
#             )
#         ):
#             answer += int(m.group())
#
# print(answer)


# Single expression version for puzzle 1.
print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day03.txt")
        .read_text()
        .splitlines()
    )
    and sum(
        ((start := m.span()[0]) or True)
        and ((end := m.span()[1]) or True)
        and (
            int(m.group())
            if (
                (start > 0 and input_[line_index][start - 1] != ".")
                or (end < len(line) and input_[line_index][end] != ".")
                or (
                    line_index > 0
                    and any(
                        c != "."
                        for c in input_[line_index - 1][
                            max(0, start - 1) : min(len(line), end + 1)
                        ]
                    )
                )
                or (
                    line_index < len(input_) - 1
                    and any(
                        c != "."
                        for c in input_[line_index + 1][
                            max(0, start - 1) : min(len(line), end + 1)
                        ]
                    )
                )
            )
            else 0
        )
        for line_index, line in enumerate(input_)
        for m in __import__("re").finditer(r"\d+", line)
    )
)


# Puzzle 2
print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day03.txt")
        .read_text()
        .splitlines()
    )
    and (
        # dict of tuple[int, int] -> list of numbers
        gears := {
            (i, j): []
            for i, line in enumerate(input_)
            for j, c in enumerate(line)
            if c == "*"
        }
    )
    and (
        sum(
            ((start := m.span()[0]) or True)
            and ((end := m.span()[1]) or True)
            and sum(
                gears[(i, j)].append(int(m.group())) or 1
                for i in range(max(0, line_index - 1), min(len(input_), line_index + 2))
                for j in range(max(0, start-1), min(len(line), end + 1))
                if (i, j) in gears
            )
            for line_index, line in enumerate(input_)
            for m in __import__("re").finditer(r"\d+", line)
        )
        or True
    )
    and (sum(r[0] * r[1] for r in gears.values() if len(r) == 2))
)
