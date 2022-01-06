import re

text = """キリンは大昔から __複数名刺__の興味の対象でした。キリンは__複数名刺__ の中で一番
背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。
キリンの身長は __数値__ __単位__ 近くあり、その高さの殆どは足と __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :param mls: 文字列で。ユーザーに入力してもらいたい単語（＝ヒント）の部分は後を２つの
    アンダースコアで挟んで下さい。ヒントの単語にはアンダースコアを含めないで下さい。
    __hint_hint__ はだめです。__hint__ はOKです。
    """
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = f"{word}を入力:"
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)
