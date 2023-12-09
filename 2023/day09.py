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


# Solutions for https://adventofcode.com/2023/day/9.

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day09.txt")
        .read_text()
        .splitlines()
    )
    and (seqs := [list(map(int, line.split())) for line in input_])
    and sum(
        (
            (sheet := [seq])
            and [
                sheet.append(
                    [sheet[-1][j] - sheet[-1][j - 1] for j in range(1, len(sheet[-1]))]
                )
                for _ in range(1, len(seq))
            ]
            and sum(s[-1] for s in sheet)
        )
        for seq in seqs
    )
)

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day09.txt")
        .read_text()
        .splitlines()
    )
    and (seqs := [list(map(int, line.split())) for line in input_])
    and sum(
        (
            (sheet := [seq])
            and [
                sheet.append(
                    [sheet[-1][j] - sheet[-1][j - 1] for j in range(1, len(sheet[-1]))]
                )
                for _ in range(1, len(seq))
            ]
            and sum(
                s[0] * (1 if i % 2 != len(seq) % 2 else -1) for i, s in enumerate(reversed(sheet))
            )
        )
        for seq in seqs
    )
)
