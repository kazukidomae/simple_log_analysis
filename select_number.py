import glob
import shutil
import re
if __name__ == '__main__':

  # 対象ディレクトリ
  file_list = sorted(glob.glob('対象ディレクトリパス/*'))
  # 出力先ファイル
  file = open("出力先ファイルパス","a")

  for filename in file_list:
        ld = open(filename, 'r',encoding="utf-8_sig")
        lines = ld.readlines()
        ld.close()

        for line in lines:
          if line.find("抽出条件") >= 0:
            # 置換
            kaiin_no = line.split('xxxxxxxxxx')[-1].split(',')[0].replace(r'\":\"', '')
            kaiin_no = kaiin_no.replace(r'\"', '')
            # ファイル書き込み
            file.writelines(kaiin_no)
            file.write("\n")
