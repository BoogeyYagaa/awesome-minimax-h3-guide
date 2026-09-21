"""Regression checks for generated counts and bounded link checks."""
import unittest
from unittest.mock import patch
import build
from catalog import collect
from check_external_links import check, classify, targets


class MaintenanceTests(unittest.TestCase):
    def test_recipe_addition_updates_counts_without_editing_readmes(self):
        records = collect()
        added = dict(next(r for r in records if r['origin'] == 'flyne'), id='FY-999')
        with patch.object(build, 'collect', return_value=records + [added]):
            result = build.outputs()
        self.assertIn('101', result['README_zh.md'])
        self.assertIn('17', result['README_ja.md'])
        self.assertIn('101 recipes', result['prompts/README.md'])
        self.assertNotIn('{{', ''.join(result.values()))

    def test_featured_media_comes_from_records(self):
        entry = dict(id='TEST', title='Example', title_zh='示例', author='creator',
                     thumbnail_url='https://example.org/new.jpg', source_url='https://x.com/creator/status/1',
                     video_url='https://example.org/new.mp4')
        output = build.featured_gallery([entry])
        self.assertIn(entry['thumbnail_url'], output)
        self.assertIn(entry['video_url'], output)
        self.assertIn('@creator', output)

    def test_github_blob_links_are_pages(self):
        pages = [r for r in targets() if '/blob/' in r['url']]
        self.assertTrue(pages)
        self.assertTrue(all(r['kind'] == 'page' for r in pages))

    def test_head_rejection_falls_back_without_body_download(self):
        target = dict(url='https://example.org/video.mp4', kind='video', sources=['test'])
        with patch('check_external_links.request', side_effect=[(405, '', target['url']), (206, 'video/mp4', target['url'])]) as request:
            result = check(target)
        self.assertEqual(result['status'], 'reachable')
        self.assertEqual([c.args[1] for c in request.call_args_list], ['HEAD', 'GET'])

    def test_restricted_is_not_deleted(self):
        for code in (401, 403, 429):
            self.assertEqual(classify(code, 'text/html', 'video'), 'restricted')

    def test_html_error_page_is_not_video(self):
        self.assertEqual(classify(200, 'text/html', 'video'), 'unexpected-content')

    def test_missing_and_transient_are_separate(self):
        self.assertEqual(classify(404, '', 'image'), 'unavailable')
        self.assertEqual(classify(503, '', 'image'), 'temporary-error')

    def test_timeout_is_not_deleted(self):
        with patch('check_external_links.request', side_effect=TimeoutError('test')):
            result = check(dict(url='https://example.org/x', kind='page', sources=['test']))
        self.assertEqual(result['status'], 'network-error')


if __name__ == '__main__':
    unittest.main()
