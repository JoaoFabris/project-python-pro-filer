from pro_filer.actions.main_actions import show_disk_usage  # NOQA

from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage_without_files(capsys):
    context = {"all_files": []}
    show_disk_usage(context)

    captured = capsys.readouterr()

    assert captured.out == "Total size: 0\n"


def test_show_disk_usage(tmp_path, capsys):
    file1_path = tmp_path / "test1.txt"
    file2_path = tmp_path / "test2.txt"
    file1_path.touch()
    file2_path.touch()
    file1_path.write_text("test1")
    file1 = str(file1_path)
    file2 = str(file2_path)

    context = {"all_files": [file1, file2]}
    show_disk_usage(context)
    captured = capsys.readouterr()
    output_file1 = f"'{_get_printable_file_path(file1)}':".ljust(70)
    output_file2 = f"'{_get_printable_file_path(file2)}':".ljust(70)
    expected = (
        f"{output_file1} 5 (100%)\n"
        f"{output_file2} 0 (0%)\n"
        f"Total size: 5\n"
    )
    assert (captured.out == expected)
