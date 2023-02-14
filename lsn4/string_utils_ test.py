import pytest
from string_utils import StringUtils

# тесты для capitilize
# 1. позитив - перевод первой буквы в заглавную, все остальные строчные
# 2. позитив - перевод первой буквы в заглавную, все остальные заглавные
# 3. негатив - первая цифра

@pytest.mark.parametrize('str, result', [ ("string", "String"), ("sTRING", "STRING"), ("123string", "123string") ])
def test_capitilize(str, result):
    cap = StringUtils()
    res = cap.capitilize(str)
    assert res == result

# баг в тесте 2 - первая становится capitalized, а остальные decapitalized
# бага в тесте 3 - цифра считается capitalized, тут обсудить надо
# метод должен называться capitAlize? 


# тесты для trim
# 1. позитив - есть пробелы в начале
# 2. негатив - нет пробелов в начале

@pytest.mark.parametrize('str, result', [ ("   string", "string"), (" ...STRING", " ...STRING") ])
def test_trim(str, result):
    cap = StringUtils()
    res = cap.trim(str)
    assert res == result


# тесты для to_list
# 1. позитив - передать строку

@pytest.mark.parametrize('list, result', [ ("t,e,s,t", ["t", "e", "s", "t"]) ])
def test_to_list(list, result):
    cap = StringUtils()
    res = cap.to_list(list)
    assert res == result


# тесты для contains
# 1. позитив - символ есть
# 2. позитив - символа нет
# 3. негатив - поиск пустоты в пустой строке

@pytest.mark.parametrize('str, foundstr, result', [ ("test", "est", True), ("test", "cat", False), ("", "", True) ])
def test_contains(str, foundstr, result):
    cap = StringUtils()
    res = cap.contains(str, foundstr)
    assert res == result


# тесты для delete_symbol
# 1. позитив - символ есть
# 2. позитив - символа нет
# 3. негатив - удаление пустоты в пустой строке

@pytest.mark.parametrize('str, cut, result', [ ("cat", "at", "c"), ("cat", "test", "cat") ])
def test_delete_symbol(str, cut, result):
    cap = StringUtils()
    res = cap.delete_symbol(str, cut)
    assert res == result


# тесты для starts_with
# 1. позитив - символ есть
# 2. позитив - символа нет
# 3. негатив - поиск пустоты в пустой строке

@pytest.mark.parametrize('str, startWith, result', [ ("test", "t", True), ("test", "c", False), ("", "", True) ])
def test_starts_with(str, startWith, result):
    cap = StringUtils()
    res = cap.starts_with(str, startWith)
    assert res == result


# тесты для end_with
# 1. позитив - символ есть
# 2. позитив - символа нет
# 3. негатив - поиск пустоты в пустой строке

@pytest.mark.parametrize('str, endWith, result', [ ("test", "t", True), ("test", "c", False), ("", "", True) ])
def test_end_with(str, endWith, result):
    cap = StringUtils()
    res = cap.end_with(str, endWith)
    assert res == result


# тесты для is_empty
# 1. позитив - пустая строка
# 2. позитив - пробелы
# 3. негатив - текст

@pytest.mark.parametrize('str, result', [ ("test", False), ("   ", True), ("", True) ])
def test_is_empty(str, result):
    cap = StringUtils()
    res = cap.is_empty(str)
    assert res == result

# баг в тесте 2 - строка с пробелами не считается пустой (в примере она считается пустой)


# тесты для list_to_string
# 1. позитив - цифры с разделителем по умолчанию
# 2. позитив - текст с разделителем отличным от дефолтного

@pytest.mark.parametrize('str, result', [ ([1,2,3,4], "1,2,3,4")])
def test_list_to_string(str, result):
    cap = StringUtils()
    res = cap.list_to_string(str)
    assert res == result

@pytest.mark.parametrize('str, separator, result', [ (["k", "o", "t", "i", "k"], "/", "k/o/t/i/k")])
def test_list_to_string_sep(str, separator, result):
    cap = StringUtils()
    res = cap.list_to_string(str, separator)
    assert res == result

# поделила на 2 теста, не смогла в parametrize задать сепаратору дефолтное значение
# баг в тесте 1 - добавляется пробел
