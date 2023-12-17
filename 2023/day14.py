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


# Solutions for https://adventofcode.com/2023/day/14.

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day14.txt")
        .read_text()
        .splitlines()
    )
    and (tiles := [list(line) for line in input_])
    and (
        [
            tiles[x][y] != "O"
            or (
                (
                    (
                        swap := next(
                            i
                            for i in range(x - 1, -2, -1)
                            if i == -1 or tiles[i][y] != "."
                        )
                        + 1
                    )
                    or True
                )
                and tiles[swap][y] == "."
                and (
                    (tiles[swap].__setitem__(y, "O"), tiles[x].__setitem__(y, "."))
                    if swap >= 0
                    else None
                )
            )
            for x in range(len(tiles))
            for y in range(len(tiles[x]))
        ]
    )
    and sum(
        (len(tiles) - x) * (tiles[x][y] == "O")
        for x in range(len(tiles))
        for y in range(len(tiles[x]))
    )
)

print(
    (
        north := lambda: [
            tiles[x][y] != "O"
            or (
                (
                    (
                        swap := next(
                            i
                            for i in range(x - 1, -2, -1)
                            if i == -1 or tiles[i][y] != "."
                        )
                        + 1
                    )
                    or True
                )
                and tiles[swap][y] == "."
                and (
                    (tiles[swap].__setitem__(y, "O"), tiles[x].__setitem__(y, "."))
                    if swap >= 0
                    else None
                )
            )
            for x in range(len(tiles))
            for y in range(len(tiles[x]))
        ]
    )
    and (
        west := lambda: [
            tiles[x][y] != "O"
            or (
                (
                    (
                        swap := next(
                            i
                            for i in range(y - 1, -2, -1)
                            if i == -1 or tiles[x][i] != "."
                        )
                        + 1
                    )
                    or True
                )
                and tiles[x][swap] == "."
                and (
                    (tiles[x].__setitem__(swap, "O"), tiles[x].__setitem__(y, "."))
                    if swap >= 0
                    else None
                )
            )
            for x in range(len(tiles))
            for y in range(len(tiles[x]))
        ]
    )
    and (
        south := lambda: [
            tiles[x][y] != "O"
            or (
                (
                    (
                        swap := next(
                            i
                            for i in range(x + 1, len(tiles) + 1)
                            if i == len(tiles) or tiles[i][y] != "."
                        )
                        - 1
                    )
                    or True
                )
                and tiles[swap][y] == "."
                and (
                    (tiles[swap].__setitem__(y, "O"), tiles[x].__setitem__(y, "."))
                    if swap < len(tiles)
                    else None
                )
            )
            for x in range(len(tiles) - 1, -1, -1)
            for y in range(len(tiles[x]) - 1, -1, -1)
        ]
    )
    and (
        east := lambda: [
            tiles[x][y] != "O"
            or (
                (
                    (
                        swap := next(
                            i
                            for i in range(y + 1, len(tiles[x]) + 1)
                            if i == len(tiles[x]) or tiles[x][i] != "."
                        )
                        - 1
                    )
                    or True
                )
                and tiles[x][swap] == "."
                and (
                    (tiles[x].__setitem__(swap, "O"), tiles[x].__setitem__(y, "."))
                    if swap < len(tiles[x])
                    else None
                )
            )
            for x in range(len(tiles) - 1, -1, -1)
            for y in range(len(tiles[x]) - 1, -1, -1)
        ]
    )
    and (rotate := lambda: (north(), west(), south(), east()))
    and (tiles := [list(line) for line in input_])
    and (keyer := lambda: "".join("".join(line) for line in tiles))
    and (
        summerize := lambda: sum(
            (len(tiles) - x) * (tiles[x][y] == "O")
            for x in range(len(tiles))
            for y in range(len(tiles[x]))
        )
    )
    and (cache := {keyer(): (0, summerize())})
    and (
        repeated_at := next(
            (i, *cache[key])
            for i in range(1, 1_000_000_000)
            if not (
                (rotate(), (key := keyer()))
                and (key not in cache)
                and (cache.__setitem__(key, (i, summerize())) or True)
            )
        )
    )
    # dict preserving insertion order FTW!
    and list(cache.values())[
        (1_000_000_000 - (repeated_at[0] - 1)) % (repeated_at[1] - repeated_at[0])
        + (repeated_at[0] - 1)
    ][1]
)
