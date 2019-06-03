import glob
# 会員番号1行取得
for no_line in open('対象ファイルパス1',"r",encoding="utf-8_sig"):
    # ファイル作成
    outfile = open("作成ファイルパス", "a", encoding="utf-8_sig")
    for log_line in open('対象ファイルパス2', "r",encoding="utf-8_sig"):
        if no_line.strip('\n') in log_line:
            outfile.write(log_line)
    outfile.close()