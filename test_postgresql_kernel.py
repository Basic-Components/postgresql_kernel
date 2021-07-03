"""Example use of jupyter_kernel_test, with tests for IPython."""
import sys
import unittest
import jupyter_kernel_test as jkt

helloworld = """ -- connection: postgres://postgres:postgres@localhost:5432/postgres
-- autocommit: true
select 'hello, world' as helloworld
"""


class PGKernelTests(jkt.KernelTests):
    kernel_name = "postgresql"
    language_name = "sql"
    code_hello_world = helloworld


if __name__ == '__main__':
    unittest.main()
