#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# pylint: disable=C

import unittest
from parameterized import parameterized

from dagwhat.dagwhat_execution import _next_simulation
from dagwhat.base import TaskOutcome


def _make_simulation_from_outcomes(outcomes):
    return [("%s" % i, outcome) for i, outcome in enumerate(outcomes)]


class ExecutionUtilsTest(unittest.TestCase):
    @parameterized.expand(
        [
            (
                [TaskOutcome.SUCCESS, TaskOutcome.SUCCESS],
                [TaskOutcome.FAILURE, TaskOutcome.FAILURE],
            ),
            (
                [TaskOutcome.FAILURE, TaskOutcome.FAILURE],
                [TaskOutcome.FAILURE, TaskOutcome.SUCCESS],
            ),
            (
                [TaskOutcome.FAILURE, TaskOutcome.SUCCESS],
                [TaskOutcome.SUCCESS, TaskOutcome.FAILURE],
            ),
            (
                [TaskOutcome.SUCCESS, TaskOutcome.FAILURE],
                [TaskOutcome.SUCCESS, TaskOutcome.SUCCESS],
            ),
            (
                [TaskOutcome.SUCCESS, TaskOutcome.FAILURE, TaskOutcome.SUCCESS],
                [TaskOutcome.SUCCESS, TaskOutcome.SUCCESS, TaskOutcome.FAILURE],
            ),
        ]
    )
    def test_evaluate_next_execution(self, in_ex, out_ex):
        self.assertEqual(
            _next_simulation(_make_simulation_from_outcomes(in_ex)),
            _make_simulation_from_outcomes(out_ex),
        )


if __name__ == '__main__':
    unittest.main()
