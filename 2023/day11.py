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


# Solutions for https://adventofcode.com/2023/day/11.

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day11.txt")
        .read_text()
        .splitlines()
    )
    and (map_ := [list(row) for row in input_])
    and (
        columns := [
            y
            for y in range(len(map_[0]))
            if all(map_[x][y] == "." for x in range(len(map_)))
        ]
    )
    and (rows := [x for x, row in enumerate(map_) if all(c == "." for c in row)])
    and (
        galaxies := [
            (x, y)
            for x in range(len(map_))
            for y in range(len(map_[x]))
            if map_[x][y] == "#"
        ]
    )
    and (combinations := __import__("itertools").combinations(galaxies, 2))
    and sum(
        (
            abs(x2 - x1)
            + abs(y2 - y1)
            + sum(min(x1, x2) < v < max(x1, x2) for v in rows)
            + sum(min(y1, y2) < v < max(y1, y2) for v in columns)
        )
        for (x1, y1), (x2, y2) in combinations
    )
)

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day11.txt")
        .read_text()
        .splitlines()
    )
    and (map_ := [list(row) for row in input_])
    and (
        columns := [
            y
            for y in range(len(map_[0]))
            if all(map_[x][y] == "." for x in range(len(map_)))
        ]
    )
    and (rows := [x for x, row in enumerate(map_) if all(c == "." for c in row)])
    and (
        galaxies := [
            (x, y)
            for x in range(len(map_))
            for y in range(len(map_[x]))
            if map_[x][y] == "#"
        ]
    )
    and (combinations := __import__("itertools").combinations(galaxies, 2))
    and sum(
        (
            abs(x2 - x1)
            + abs(y2 - y1)
            + sum(min(x1, x2) < v < max(x1, x2) for v in rows) * 999_999
            + sum(min(y1, y2) < v < max(y1, y2) for v in columns) * 999_999
        )
        for (x1, y1), (x2, y2) in combinations
    )
)
