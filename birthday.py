print('Hello,Python!')

import datetime

name = 'MeiKawamura'
today = datetime.date.today()
next_birth = datetime.date(2025,1,16)

cnt = (next_birth - today).days

print(f'{name}の次の誕生日は{next_birth}です。')
print(f'{name}の次の誕生日まで{cnt}日です。')

if cnt<90:
    print('３ヶ月以内に誕生日ですね！わーい！')
elif cnt>270:
    print('まだまだ先だね！誕生日から3ヶ月経ってないすね！')
else :
    print('なんでもない日におめでとう')