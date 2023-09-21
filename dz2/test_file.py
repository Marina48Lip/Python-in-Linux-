from cheks import checkout
import pytest

folderin = '/home/user/test'
folderout = '/home/user/out'
folderext = '/home/user/folder1'

# def test_step1():
#     assert checkout(f' cd {folderin}; 7z a {folderout}/arh1', 'Everything is Ok'), 'test_step1 FAIL'

# def test_step2():
#     assert checkout(f' cd {folderout}; 7z d arh1.7z', 'Everything is Ok'), 'test_step2 FAIL'

# def test_step3():
#     assert checkout(f' cd {folderext}; 7z u {folderout}/arh1', 'Everything is Ok'), 'test_step3 FAIL'

def test_file_list():
    assert checkout(f' cd {folderout}; 7z l arh1.7z', ''), 'test_file_list FAIL'

def test_file_compressed():
    assert checkout(f' cd {folderout}; 7z x arh1.7z', 'Everything is Ok'), 'test_file_compressed FAIL'



if __name__ == '__main__':
    pytest.main(['-vv'])
