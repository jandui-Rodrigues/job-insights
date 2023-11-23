from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('data/jobs.csv', 'Python') == 1639
    assert count_ocurrences('data/jobs.csv', 'python') == 1639
    assert count_ocurrences('data/jobs.csv', 'JavaScript') == 122
    assert count_ocurrences('data/jobs.csv', 'javaScript') == 122
