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


# Solutions for https://adventofcode.com/2023/day/7.

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day07.txt")
        .read_text()
        .splitlines()
    )
    and (hands := [(line.split()[0], int(line.split()[1])) for line in input_])
    and (
        sort_key := lambda hand: (
            (th := hand[0].translate(str.maketrans("AKQJT", "EDCBA")))
            and (
                counts := sorted(
                    __import__("collections").Counter(th).values(), reverse=True
                )
            )
            and (
                7
                if counts[0] == 5
                else (
                    6
                    if counts[0] == 4
                    else (
                        5
                        if counts[0] == 3 and counts[1] == 2
                        else (
                            4
                            if counts[0] == 3
                            else (
                                3
                                if counts[0] == counts[1] == 2
                                else (2 if counts[0] == 2 else 1)
                            )
                        )
                    )
                ),
                th,
            )
        )
    )
    and sum((i + 1) * hand[1] for i, hand in enumerate(sorted(hands, key=sort_key)))
)

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day07.txt")
        .read_text()
        .splitlines()
    )
    and (hands := [(line.split()[0], int(line.split()[1])) for line in input_])
    and (
        sort_key := lambda hand: (
            (th := hand[0].translate(str.maketrans("AKQJT", "EDC0A")))  # J -> 0
            and (
                (
                    nz_counts := sorted(
                        (
                            count
                            for c, count in __import__("collections")
                            .Counter(th)
                            .items()
                            if c != "0"
                        ),
                        reverse=True,
                    )
                )
                or True
            )
            and ((z_count := sum(1 if c == "0" else 0 for c in th)) or True)
            and (
                7
                if z_count == 5 or (nz_counts[0] + z_count) == 5
                else (
                    6
                    if (nz_counts[0] + z_count) == 4
                    else (
                        5
                        if (nz_counts[0] + z_count) == 3 and nz_counts[1] == 2
                        else (
                            4
                            if (nz_counts[0] + z_count) == 3
                            else (
                                3
                                if nz_counts[0] == nz_counts[1] == 2
                                else (
                                    2
                                    if nz_counts[0] == 2 or (nz_counts and z_count == 1)
                                    else 1
                                )
                            )
                        )
                    )
                ),
                th,
            )
        )
    )
    and sum((i + 1) * hand[1] for i, hand in enumerate(sorted(hands, key=sort_key)))
)
