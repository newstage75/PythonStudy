# 大量のデータを順番に破棄しながら扱う
#
# イテレータとは？iter()
# 連続データを操作するオブジェクト
# 連続データ→リスト・集合・タプル
#
# for文は裏側でイテレータが使われている！

# x = ['a', 'b', 'c']
#
# itr_obj = iter(x)
# r1 = next(itr_obj)
# r2 = next(itr_obj)
# r3 = next(itr_obj)
# r4 = next(itr_obj) #エラー発生（StopIteration）

#fがファイルオブジェクト、読み込み終了するとクローズするようにwithをつける
# with open('text.txt') as f:
#     text = f.read()

f = open('text.txt')

print(next(f))
print(next(f))
print(next(f))


#dir()で属性を取得できる→__iter__と__next__の両方がある。
# これらはiter関数とnext関数が呼び出された時の関数
print(dir(f))

"""そのため、自作でイテレータを作りたいときは↓
class MyIterator:
    def __iter__(self):
        return self

    deg __next__(self):
        #処理
        return xxxx

mi = MyIterator()"""

# これを簡単にするために→ジェネレータオブジェクトの利用
# ジェネレータ内の処理を一時停止させて
# 順番ｂんに返したい値をyieldの後ろに設定すればOK

def my_generator():
    x = 10
    yield x
    x = x + 10
    yield x
    x = x + 10
    yield x

#ジェネレータオブジェクトを返す
mg = my_generator()

# print(next(mg))
# print(next(mg))
# print(next(mg))

for x in mg:
    print(x)

#メソッドの確認
print(dir(mg))

# イテレータの性質
# 一度、for文で取り出したデータは、その後forを使っても取り出せない！