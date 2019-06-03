import glob
import shutil
import re
if __name__ == '__main__':

  # 対象ディレクトリ
  file_list = sorted(glob.glob('対象ディレクトリパス/*'))
  # 出力先ファイル
  file = open("出力先ファイルパス","a",encoding="utf-8_sig")

  for filename in file_list:
        ld = open(filename, 'r',encoding="utf-8_sig")
        lines = ld.readlines()
        ld.close()
        
        for line in lines:
            if '抽出条件' in line:
                file.write(line)