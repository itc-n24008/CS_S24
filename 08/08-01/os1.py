import os
def prepare_dir(dir_name="save_dir"):
    if os.path.exists(dir_name):
        print("ディレクトリ'{}'が存在します。".format(dir_name))
    else:
        os.mkdir(dir_name)
        print("ディレクトリ'{}'を作成しました。".format(dir_name))

prepare_dir()
