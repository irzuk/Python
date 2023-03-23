# import as pic_gen

from functools import reduce
from testpackagefibbfunpicturegen import generate
def convert_arr_to_str(arr):
    ans = '\\begin{tabular}{|'
    s = len(arr[0])
    ans += 'c|' * s + '}\n\\hline\n'
    # reduce
    ans += reduce(
        lambda l, r: l + '\\hline\n' + r,
        map(lambda line: reduce(lambda l, r: str(l) + ' & ' + str(r), line) + ' \\\\\n', arr)
    )
    ans += '\\hline\n\\end{tabular}\n'
    return ans


def easy_task(arr):
    head = '\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[' \
           'english]{babel}\n\\usepackage{graphicx}\n\\graphicspath{ {./artifacts/} }\n\\begin{document}\n'
    end = '\\end{document}\n'
    f = open("artifacts/easy_task.tex", "w")
    f.write(head + convert_arr_to_str(arr) + end)
    f.close()


def medium_task(arr):
    easy_task(arr)
    generate()
    with open("artifacts/easy_task.tex", "r") as old_tex:
        contents = old_tex.readlines()

    contents.insert(1, "\\usepackage{graphicx}\n")
    contents.insert(len(contents) - 1, "\n\n\includegraphics[scale=0.2]{artifacts/ast.png}\n")
    new_tex = open("artifacts/medium_task.tex", "w")
    new_tex.writelines(contents)


def main():
    arr = [["res: " + str(i + j) for j in range(8)] for i in range(7)]
    easy_task(arr)
    medium_task(arr)


if __name__ == "__main__":
    main()