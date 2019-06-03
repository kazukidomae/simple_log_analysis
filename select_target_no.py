import glob
import shutil
import re
if __name__ == '__main__':
    # 対象ファイル
    target_log = open("出力先ファイルパス" ,'r',encoding="utf-8_sig")
    # 出力先ファイル
    file = open("出力先ファイル","a",encoding="utf-8_sig")
   
    lines = target_log.readlines()
    for line in lines:
        kaiin_no = line.split('xxxxxxxxxx')[-1].split(',')[0].replace(r'\":\"', '')
        kaiin_no = kaiin_no.replace(r'\"', '')
        file.write(kaiin_no)
        file.write('\n')
        print(kaiin_no)
    target_log.close()