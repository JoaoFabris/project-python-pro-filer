from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_empty(capsys):
    context = {
        "all_files": list(),
        "all_dirs": list()
    }
    show_preview(context)
    output = capsys.readouterr()
    assert output.out == "Found 0 files and 0 directories\n"


def test_show_preview_files(capsys):
    context = {
        "all_files": [
            "src/1.py",
            "src/2.py",
            "src/u/a.py",
            "src/2.py",
        ],
        "all_dirs": ["src", "src/u"],
    }
    show_preview(context)
    expected = """Found 4 files and 2 directories
First 5 files: ['src/1.py', 'src/2.py', 'src/u/a.py', 'src/2.py']
First 5 directories: ['src', 'src/u']\n"""
    captured = capsys.readouterr()
    assert captured.out == expected
