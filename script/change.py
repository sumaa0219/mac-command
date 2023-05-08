import csv
import sys

args = sys.argv


path = args[1]
try:
    outpath = args[1]
except:
     outpath = args[2]
#読み込み用配列
line = []

#読み込み
with open(path, "r", newline="") as f:
    for row in csv.reader(f):
        linex = row[0].strip()
        linex = row[0].split()

        line.append(linex)

#書き込み
with open(outpath, "w", newline="") as f:
        #書き込みオブジェクト作成（タブ区切り）
        writer = csv.writer(f)
        #まとめて書き込み
        writer.writerows(line)
        print("succese")

