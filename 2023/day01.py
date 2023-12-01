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


# Solutions for https://adventofcode.com/2023/day/1.


# Puzzle 1.
#
# def get_number(line):
#     number = "".join(c for c in line if c.isnumeric())
#     return int(number[0] + number[-1])
#
# print(sum(get_number(line) for line in open("day01.txt")))


# Puzzle 2.
#
# spellings = {
#     "0": "0",
#     "1": "1",
#     "2": "2",
#     "3": "3",
#     "4": "4",
#     "5": "5",
#     "6": "6",
#     "7": "7",
#     "8": "8",
#     "9": "9",
#     "one": "1",
#     "two": "2",
#     "three": "3",
#     "four": "4",
#     "five": "5",
#     "six": "6",
#     "seven": "7",
#     "eight": "8",
#     "nine": "9",
# }
#
# def get_number(line):
#     num = []
#     for i in range(len(line)):
#         for spelling, value in spellings.items():
#             if line[i:].startswith(spelling):
#                 num.append(value)
#                 break
#     return int(num[0] + num[-1])
#
# print(sum(get_number(line) for line in open("day01.txt")))


# Final single expression version.
print(
    (input_ := (__import__("pathlib").Path(__file__).parent / "day01.txt").read_text())
    and (
        spellings := {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
    )
    and sum(
        (
            num := [
                value
                for i in range(len(line))
                for spelling, value in spellings.items()
                if line[i:].startswith(spelling)
            ]
        )
        and int(num[0] + num[-1])
        for line in input_.splitlines()
    )
)
