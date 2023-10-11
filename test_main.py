import unittest
from mylib.query import Query

class testFDBFunctions(unittest.TestCase):
    def test_Query(self):
        result = Query()
        self.assertEqual(result, "Success", "Failed to execute the query")

if __name__ == "__main__":
    unittest.main()

# import subprocess

# def test_extract():
#     result = subprocess.run(
#         ["python", "main.py", "extract"],
#         capture_output=True,
#         text=True,
#         check=True
#     )
#     assert "Extracting data..." in result.stdout

# def test_transform_load():
#     result = subprocess.run(
#         ["python", "main.py", "transform_load"],
#         capture_output=True,
#         text=True,
#         check=True
#     )
#     assert "Transforming data..." in result.stdout

# def test_Query():
#     result = subprocess.run(
#         ["python", "main.py", "Query"],
#          capture_output=True,
#          text=True,
#          check=True
#     )
#     assert result.returncode == 0

# if __name__ == "__main__":
#     test_extract()
#     test_transform_load()
#     test_Query()