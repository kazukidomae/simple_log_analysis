import glob
import shutil
import re
if __name__ == '__main__':

    # 対象ディレクトリ
    file_list = sorted(glob.glob('対象ディレクトリパス/*'))
    # 出力先ファイル
    file = open("出力先ファイルパス","a")
    # 出力先ディレクトリ
    dir = '出力先ディレクトリパス'
    for filename in file_list:
            ld = open(filename, 'r',encoding="utf-8_sig")
            lines = ld.readlines()
            ld.close()

            for line in lines:
                # 抽出条件
                if line.find("条件文字列") >= 0:
                    # ファイルコピー
                    shutil.copy(filename,dir)
                    break                