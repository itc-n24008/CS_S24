import pathlib
p = pathlib.Path('.')
for pf in p.iterdir():
    if pf.is_file():
        print(str(pf))
