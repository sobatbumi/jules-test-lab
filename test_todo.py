import unittest

from todo import TodoList


class TestTodoList(unittest.TestCase):
    def test_add_and_list(self):
        todos = TodoList()
        item = todos.add("Belajar Jules")
        self.assertEqual(item["title"], "Belajar Jules")
        self.assertFalse(item["done"])
        self.assertEqual(len(todos.list_all()), 1)

    def test_add_empty_title_raises(self):
        todos = TodoList()
        with self.assertRaises(ValueError):
            todos.add("   ")

    def test_complete(self):
        todos = TodoList()
        item = todos.add("Belajar Jules")
        done = todos.complete(item["id"])
        self.assertTrue(done["done"])

    def test_complete_unknown_id_raises(self):
        todos = TodoList()
        with self.assertRaises(KeyError):
            todos.complete(999)


if __name__ == "__main__":
    unittest.main()
