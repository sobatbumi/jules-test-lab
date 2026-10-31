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

    def test_remove(self):
        todos = TodoList()
        item1 = todos.add("Belajar Jules")
        item2 = todos.add("Belajar Python")

        removed_item = todos.remove(item1["id"])
        self.assertEqual(removed_item["id"], item1["id"])
        self.assertEqual(removed_item["title"], "Belajar Jules")

        all_items = todos.list_all()
        self.assertEqual(len(all_items), 1)
        self.assertEqual(all_items[0]["id"], item2["id"])

    def test_remove_unknown_id_raises(self):
        todos = TodoList()
        todos.add("Belajar Jules")
        with self.assertRaises(KeyError):
            todos.remove(999)

    def test_search(self):
        todos = TodoList()
        todos.add("Belajar Jules")
        todos.add("Belajar Python")
        todos.add("Membaca buku")

        # Test basic search
        results = todos.search("Belajar")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["title"], "Belajar Jules")
        self.assertEqual(results[1]["title"], "Belajar Python")

        # Test case-insensitive search
        results = todos.search("jules")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Belajar Jules")

        # Test no match
        results = todos.search("coding")
        self.assertEqual(len(results), 0)

        # Test empty keyword returns all items
        results = todos.search("")
        self.assertEqual(len(results), 3)


if __name__ == "__main__":
    unittest.main()
