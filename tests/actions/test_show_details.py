from pro_filer.actions.main_actions import show_details  # NOQA

import datetime


def test_show_details_no_file(capsys):
    context = {"base_path": "src/test"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File 'test' does not exist\n"


def test_show_details_file(capsys, tmp_path):
    file_path = tmp_path / "test.py"
    file_path.touch()
    context = {"base_path": str(file_path)}
    show_details(context)

    captured = capsys.readouterr()
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    assert captured.out == (
        "File name: test.py\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .py\n"
        f"Last modified date: {current_date}\n"
    )


def test_show_details_directory(capsys, tmp_path):
    file_path = tmp_path / "test"
    file_path.mkdir()
    context = {"base_path": str(file_path)}
    show_details(context)

    captured = capsys.readouterr()
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    assert captured.out == (
        "File name: test\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        f"Last modified date: {current_date}\n"
    )
