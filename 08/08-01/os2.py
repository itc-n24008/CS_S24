import os

def delete_dir(dir_name="save_dir"):
    if os.path.exists(dir_name):
        print("ディレクトリ'{}'が存在します。".format(dir_name))
        os.rmdir(dir_name)
        print("ディレクトリ'{}'を削除しました。".format(dir_name))
    else:
        print("ディレクトリ'{}'はありません。".format(dir_name))

delete_dir()
