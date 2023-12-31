from textwrap import dedent

import pytest

from package_statistics import PRIMARY, Failed, main, parsefile, summary, tabulate


def test_prasefile():
    assert not parsefile("")
    assert parsefile(["aa A", "bb A"]) == {"A": 2}
    assert parsefile(["aa A", "bb A,B"]) == {"A": 2, "B": 1}
    assert parsefile(["a a a A"]) == {"A": 1}


def test_summary():
    assert summary({"a": 1, "f": 2, "b": 3}, n=2) == [("b", 3), ("f", 2)]


def test_tabulate():
    assert tabulate([]) == ""
    assert tabulate([(1, 2)]) == "1.  1 2"
    assert tabulate([(1, 2), (10, 20)]) == "1.  1  2\n2.  10 20"


def test_smoke(pytestconfig):
    expected = dedent(
        """
        1.  admin/systemd           4
        2.  admin/elogind           3
        3.  net/iputils-ping        3
        4.  admin/systemd-container 2
        5.  net/inetutils-ping      2
        6.  utils/coreutils         1
        7.  utils/kbd               1
        8.  utils/pax               1
        9.  admin/sysvinit-utils    1
        10. admin/finit             1
        """
    ).strip()

    with (pytestconfig.rootpath / "tests/data/sample").open("r") as f:
        assert tabulate(summary(parsefile(f))) == expected


@pytest.mark.network
def test_functional(capsys):
    main(PRIMARY, "arm64", True)
    stdout = capsys.readouterr().out
    assert "\n10. " in stdout
    # The leaderboard may change, but dev libs are likely to stay on
    assert "libdevel" in stdout


@pytest.mark.network
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_negative():
    with pytest.raises(Failed):
        main("https://google.com", "foobar", False)
