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


# Solutions for https://adventofcode.com/2023/day/2.


# Puzzle 1.
#
# COUNTS = {
#     "red": 12,
#     "green": 13,
#     "blue": 14,
# }
#
# def get_number(line):
#     first, second = line.split(":")
#     id_ = int(first.split()[-1])
#     for play in second.split(";"):
#         for group in play.split(","):
#             count, color = group.split()
#             if COUNTS[color] < int(count):
#                 return 0
#     return int(id_)
#
# print(
#     sum(
#         get_number(line)
#         for line in (__import__("pathlib").Path(__file__).parent / "day02.txt")
#         .read_text()
#         .splitlines()
#     )
# )


# Single expression version for puzzle 1.
print(
    sum(
        (
            (
                counts := [
                    max(
                        [
                            int(count.split()[0]) if count.split()[1] == color else 0
                            for play in line.split(":")[1].split(";")
                            for count in play.split(",")
                        ]
                        or [0, 0]
                    )
                    for color in ("red", "green", "blue")
                ]
            )
            and (
                int(line.split(":")[0].split()[-1])
                if (counts[0] <= 12 and counts[1] <= 13 and counts[2] <= 14)
                else 0
            )
            or 0
        )
        for line in (__import__("pathlib").Path(__file__).parent / "day02.txt")
        .read_text()
        .splitlines()
    )
)


# Puzzle 2.
# def compute_power(line):
#     counts = {"red": 0, "green": 0, "blue": 0}
#     for play in line.split(":")[1].split(";"):
#         for group in play.split(","):
#             count, color = group.split()
#             counts[color] = max(counts[color], int(count))
#     return counts["red"] * counts["green"] * counts["blue"]
#
# print(
#     sum(
#         compute_power(line)
#         for line in (__import__("pathlib").Path(__file__).parent / "day02.txt")
#         .read_text()
#         .splitlines()
#     )
# )


# Single expression version for puzzle 2.
print(
    sum(
        __import__("functools").reduce(
            lambda x, y: x * y,
            [
                max(
                    [
                        int(count.split()[0]) if count.split()[1] == color else 0
                        for play in line.split(":")[1].split(";")
                        for count in play.split(",")
                    ]
                    or [0, 0]
                )
                for color in ("red", "green", "blue")
            ],
            1,
        )
        for line in (__import__("pathlib").Path(__file__).parent / "day02.txt")
        .read_text()
        .splitlines()
    )
)
