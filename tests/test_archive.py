import unittest
import os
from scripts.archive_sync import html_to_markdown

class TestArchiveSync(unittest.TestCase):
    def test_html_to_markdown_basic(self):
        sample_html = "<h2>Title</h2><p>This is a <strong>bold</strong> paragraph with a <a href='https://aviperera.com'>link</a>.</p>"
        result = html_to_markdown(sample_html)
        self.assertIn("## Title", result)
        self.assertIn("**bold**", result)
        self.assertIn("[link](https://aviperera.com)", result)

    def test_docs_directory_has_files(self):
        docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs")
        self.assertTrue(os.path.exists(docs_dir))
        md_files = [f for f in os.listdir(docs_dir) if f.endswith(".md")]
        self.assertGreater(len(md_files), 0)

if __name__ == "__main__":
    unittest.main()
