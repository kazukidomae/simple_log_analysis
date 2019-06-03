lines_seen = set()
outfile = open('出力先ファイルパス', "a",encoding="utf-8_sig")
for line in open('対象ファイルパス', "r",encoding="utf-8_sig"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()