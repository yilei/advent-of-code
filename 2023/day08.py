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


# Solutions for https://adventofcode.com/2023/day/8.

print(
    # Let's cross our fingers that the answer isn't too large.
    (__import__("sys").setrecursionlimit(1000000) or True)
    and (
        input_ := (__import__("pathlib").Path(__file__).parent / "day08.txt")
        .read_text()
        .splitlines()
    )
    and (instructions := input_[0])
    and (nodes := {line[:3]: (line[7:10], line[12:15]) for line in input_[2:]})
    and (
        find_step := lambda key, step_count: (
            step_count
            if key == "ZZZ"
            else (
                find_step(
                    nodes[key][
                        0 if instructions[step_count % len(instructions)] == "L" else 1
                    ],
                    step_count + 1,
                )
            )
        )
    )
    and find_step("AAA", 0)
)

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day08.txt")
        .read_text()
        .splitlines()
    )
    and (instructions := [0 if lr == "L" else 1 for lr in input_[0]])
    and (nodes := {line[:3]: (line[7:10], line[12:15]) for line in input_[2:]})
    and (
        next_round_map := {
            k: (
                (current := k)
                and [current := nodes[current][lr] for lr in instructions][-1]
            )
            for k in nodes
        }
    )
    and (
        get_trip := lambda key, trip, found_z: (
            (key := next_round_map[key])
            and (
                (trip if found_z else get_trip(key, trip + 1, True))
                if key.endswith("Z")
                else get_trip(key, trip + found_z, found_z)
            )
        )
    )
    and (trips := (get_trip(key, 0, False) for key in nodes if key.endswith("A")))
    and __import__("math").lcm(*trips) * len(instructions)
)
