from pypinyin.style._utils import get_finals
from pypinyin import lazy_pinyin

def read_rhyme_finals(file_path='./rhyme_finals.txt'):
    with open(file_path, 'r') as f:
        rhymes = f.readlines()
        f.close()
    return [i.strip().split(',') for i in rhymes]

def get_rhyme(word):
    rhyme = get_finals(lazy_pinyin(word)[0],strict=False)
    rhymes_chinese = read_rhyme_finals()
    for idx, rhymes in enumerate(rhymes_chinese):
        if rhyme in rhymes:
            return idx + 1
    return 0
