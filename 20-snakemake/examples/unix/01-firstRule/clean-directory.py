import os

dir_path = os.path.dirname(os.path.realpath(__file__))

hatefiles =['.aux', '.bbl', '.blg', '.fdb_latexmk', '.fls', '.log', '.gz', '.nav', '.out', '.snm', '.toc']

for parent, dirnames, filenames in os.walk(dir_path):
    for fn in filenames:
        for ending in hatefiles:
            if fn.lower().endswith(ending):
                os.remove(os.path.join(parent, fn))
else:
    print('Successfully LaTeX cleaned ' + dir_path + '.')
