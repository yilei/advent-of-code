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


# Solutions for https://adventofcode.com/2023/day/5.


print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day05.txt")
        .read_text()
        .splitlines()
    )
    and (seeds := list(map(int, input_[0].split(":")[1].split())))
    and (
        # list of list of tuple[dest, source, range_].
        maps := [
            [tuple(int(s) for s in line.split()) for line in raw.splitlines()[1:]]
            for raw in "\n".join(input_[2:]).split("\n\n")
        ]
    )
    and (
        map_fn := lambda value, map_tuple: next(
            v
            for v in [
                dest + (value - source) if source <= value < source + range_ else None
                for dest, source, range_ in map_tuple
            ]
            + [value]  # When no mapping is found.
            if v is not None
        )
    )
    and (
        # Resursive function to map the seed through list of maps.
        map_all_fn := lambda value, index: (
            map_all_fn(map_fn(value, maps[index]), index + 1)
            if index < len(maps)
            else value
        )
    )
    and min(map_all_fn(seed, 0) for seed in seeds)
)


print(
    (
        input_ := (
            (__import__("pathlib").Path(__file__).parent / "day05.txt")
            .read_text()
            .splitlines()
        )
    )
    and (seeds := list(map(int, input_[0].split(":")[1].split())))
    and (
        # list of list of tuple[dest, source, range_].
        maps := [
            sorted(
                [tuple(int(s) for s in line.split()) for line in raw.splitlines()[1:]],
                # Sort by source.
                key=lambda t: t[1],
            )
            for raw in "\n".join(input_[2:]).split("\n\n")
        ]
    )
    and (
        map_fn := lambda ranges_, index: (
            ranges_
            if index >= len(maps)
            else map_fn(
                (map_ := maps[index])
                and (
                    candidates := sorted(
                        [
                            (-10, map_[0][1]),
                            # HACK, could be replaced by calculating the max value.
                            (map_[-1][1] + map_[-1][2], 99999999999999999999),
                        ]
                        + [
                            (map_[i][1], map_[i][1] + map_[i][2], map_[i][0])
                            for i in range(len(map_))
                        ]
                        + [
                            (map_[i][1] + map_[i][2], map_[i + 1][1])
                            for i in range(len(map_) - 1)
                        ]
                    )
                )
                and sorted(
                    (
                        (
                            pair := (
                                max(candidate[0], value),
                                min(candidate[1], value + length),
                            )
                        )
                        and (
                            (pair[0], pair[1] - pair[0])
                            if len(candidate) == 2
                            else (
                                pair[0] - candidate[0] + candidate[2],
                                pair[1] - pair[0],
                            )
                        )
                    )
                    for value, length in ranges_
                    for candidate in candidates
                    if candidate[1] > value and candidate[0] < value + length
                ),
                index + 1,
            )
        )
    )
    and map_fn(
        sorted((seeds[i * 2], seeds[i * 2 + 1]) for i in range(len(seeds) // 2)), 0
    )[0][0]
)
