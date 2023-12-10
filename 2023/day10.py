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


# Solutions for https://adventofcode.com/2023/day/10.

print(
    (__import__("sys").setrecursionlimit(1000000) or True)  # Unfortunately
    and (map_ := {"F": "┌", "J": "┘", "7": "┐", "L": "└"})  # Make debugging easier
    and (
        input_ := (__import__("pathlib").Path(__file__).parent / "day10.txt")
        .read_text()
        .splitlines()
    )
    and (m := [[map_.get(c, c) for c in line] for line in input_])  # matrix
    and (
        start := next(
            (i, j) for i in range(len(m)) for j in range(len(m[i])) if m[i][j] == "S"
        )
    )
    and (sm := [["-"] * len(line) for line in m])  # steps matrix
    and (sm[start[0]].__setitem__(start[1], 1) or True)
    and (remains := [start])
    and (
        walk := lambda: (
            True
            if not remains
            else (
                (xy := remains.pop(0))
                and ((x := xy[0]) or True)
                and ((y := xy[1]) or True)
                and ((p := m[x][y]) or True)
                and ((s := sm[x][y]) or True)
                and (
                    True
                    if x - 1 < 0
                    or isinstance(sm[x - 1][y], int)
                    or not (p in "S|┘└" and m[x - 1][y] in "|┌┐")
                    else (
                        sm[x - 1].__setitem__(y, s + 1)
                        or remains.append((x - 1, y))
                        or 1
                    )
                )
                and (
                    True
                    if y - 1 < 0
                    or isinstance(sm[x][y - 1], int)
                    or not (p in "S-┘┐" and m[x][y - 1] in "-└┌")
                    else (
                        sm[x].__setitem__(y - 1, s + 1)
                        or remains.append((x, y - 1))
                        or 1
                    )
                )
                and (
                    True
                    if y + 1 >= len(m[x])
                    or isinstance(sm[x][y + 1], int)
                    or not (p in "S-┌└" and m[x][y + 1] in "-┘┐")
                    else (
                        sm[x].__setitem__(y + 1, s + 1)
                        or remains.append((x, y + 1))
                        or 1
                    )
                )
                and (
                    True
                    if x + 1 >= len(m)
                    or isinstance(sm[x + 1][y], int)
                    or not (p in "S|┌┐" and m[x + 1][y] in "|┘└")
                    else (
                        sm[x + 1].__setitem__(y, s + 1)
                        or remains.append((x + 1, y))
                        or 1
                    )
                )
                and walk()
            )
        )
    )
    and walk()
    and (max(v if isinstance(v, int) else 0 for line in sm for v in line) - 1)
)

print(
    (
        enclosed := lambda x, y: (
            (
                critical_pipes := [
                    m[i][y]
                    for i in range(x)
                    if m[i][y] in "-┌└┘┐" and isinstance(sm[i][y], int)
                ]
                or False
            )
            and sum(
                ((previous := None if i == 0 else critical_pipes[i - 1]) or True)
                and (
                    p in "-┌┐"
                    or (p == "└" and ((previous == "┌" and -1) or previous != "┐"))
                    or (p == "┘" and ((previous == "┐" and -1) or previous != "┌"))
                )
                for i, p in enumerate(critical_pipes)
            )
            % 2
            == 1
        )
    )
    and sum(
        enclosed(x, y)
        for x in range(len(m))
        for y in range(len(m[x]))
        if not isinstance(sm[x][y], int)
    )
)
