# -*- coding: utf-8 -*-
from colorama import Fore, Style

from .loader import load_test_info

STORAGE = {
    'parents': {}
}
STATUS_ICONS = {
    'passed': '✓',
    'failed': '✖',
    'skipped': '!',
    'error': 'E',
    'xfailed': '✖',
    'xpassed': '✓',
}
COLORS = {
    'passed': Fore.GREEN,
    'failed': Fore.RED,
    'skipped': Fore.YELLOW,
    'error': Fore.RED,
    'xfailed': Fore.YELLOW,
    'xpassed': Fore.YELLOW,
}


def logstart_replacer(self, nodeid, location):
    """Signal the start of running a single test item.
    Hook has to be disabled because additional information
    may break output formatting.
    """


def report_replacer(self, report):
    res = self.config.hook.pytest_report_teststatus(report=report, config=self.config)
    category, letter, word = res
    self.stats.setdefault(category, []).append(report)
    if not letter and not word:
        return

    file_name, text = load_test_info(report.nodeid)
    orig_text = text
    text = [x.strip() for x in text.split('::')]
    parents = []
    if len(text) >= 1:
        parents.extend(text[:-1])
    if not parents:
        parents = [file_name]

    text = text[-1]

    indent = '    '
    test_indent = indent
    tmp_keys = []
    upper_parent_changed = False
    for idx, parent in enumerate(parents):
        tmp_keys.append(idx)
        test_indent = indent * (idx + 1)
        old_parent = STORAGE['parents'].get(idx, None)
        if not upper_parent_changed and parent == old_parent:
            continue

        upper_parent_changed = True
        STORAGE['parents'][idx] = parent
        if idx == 0 and parent != file_name:
            parent = parent + ' :: ' + file_name

        self._tw.line()
        self._tw.write(indent * idx + parent)

    for key in list(STORAGE['parents']):
        if key not in tmp_keys:
            STORAGE['parents'].pop(key)

    category = category.strip()
    self._tw.line()
    self._tw.write("{color}{indent}{icon} {text}{reset}".format(
        color=COLORS[category],
        indent=test_indent,
        icon=STATUS_ICONS[category],
        text=text,
        reset=Style.RESET_ALL
    ))
