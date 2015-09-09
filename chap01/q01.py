# coding:utf-8

"""
言語処理100本ノック第１章01
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""


def pick_odd_char(unicode_sentence):
    """
    奇数番目の文字列を返す
    :param sentence: unicode
    :return: unicode
    """
    assert type(unicode_sentence) is unicode, "unicode型の文字を入力してください"
    return unicode_sentence[::2]


if __name__ == "__main__":
    example_sentence = u"パタトクカシーー"
    print pick_odd_char(unicode_sentence=example_sentence).encode("utf-8")