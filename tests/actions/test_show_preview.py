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
        "all_files": ["src1", "src2", "src3", "src4", "src5", "src6"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"],
    }

    show_preview(context)
    output = capsys.readouterr()
    assert output.out == (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['src1', 'src2', 'src3', 'src4', 'src5']\n"
        "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']\n"
        )
