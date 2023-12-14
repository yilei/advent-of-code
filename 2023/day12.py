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


# Solutions for https://adventofcode.com/2023/day/12.

print(
    (
        input_ := (__import__("pathlib").Path(__file__).parent / "day12.txt")
        .read_text()
        .splitlines()
    )
    and (
        rows := [
            (l.split()[0], list(map(int, l.split()[1].split(",")))) for l in input_
        ]
    )
    and (cache := {"": 1})
    and (keyer := lambda records, groups: records + ",".join(map(str, groups)))
    and (
        count := lambda records, groups: (
            cache[keyer(records, groups)]
            if keyer(records, groups) in cache
            else (
                val := (
                    not groups
                    if not records
                    else (
                        not any(c == "#" for c in records)
                        if not groups
                        else (len(records) >= sum(groups) + len(groups) - 1)
                        and (
                            groups[0] <= len(records)
                            and sum(
                                not any(c == "#" for c in records[0:i])
                                and not any(c == "#" for c in records[i + groups[0] :])
                                and all(c in "#?" for c in records[i : i + groups[0]])
                                for i in range(len(records) - groups[0] + 1)
                            )
                            if len(groups) == 1
                            else (
                                (
                                    sum(c in "?#" for c in records) >= sum(groups)
                                    or sum(groups) >= sum(c == "#" for c in records)
                                )
                                and sum(c in ".?" for c in records) >= len(groups) - 1
                                and not all(c == "#" for c in records)
                                and (
                                    (
                                        d := next(
                                            r
                                            for r in (
                                                len(records) // 2
                                                + (
                                                    (i // 2)
                                                    if i % 2 == 0
                                                    else -((i + 1) // 2)
                                                )
                                                for i in range(len(records))
                                            )
                                            if records[r] != "#"
                                        )
                                    )
                                    or True
                                )
                                and (
                                    sum(
                                        (left := count(records[:d], groups[0:g]))
                                        and (left * count(records[d + 1 :], groups[g:]))
                                        for g in range(len(groups) + 1)
                                    )
                                    if records[d] == "."
                                    else (
                                        count(
                                            f"{records[:d]}#{records[d + 1 :]}", groups
                                        )
                                        + count(
                                            f"{records[:d]}.{records[d + 1 :]}", groups
                                        )
                                    )
                                )
                            )
                        )
                    )
                ),
                cache.__setitem__(keyer(records, groups), val),
            )
            and val
        )
    )
    and sum(count(row[0], row[1]) for row in rows)
)

print(
    (rows := [("?".join([row[0]] * 5), row[1] * 5) for row in rows])
    and sum(count(row[0], row[1]) for row in rows)
)
