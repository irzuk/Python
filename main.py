# import as pic_gen

def convert_arr_to_str(arr):
    return "\documentclass{article}\n\\begin{document}\n\\begin{center}\n\\end{document}\n"


def easy_task(arr):
    f = open("artifacts/easy_task.tex", "w")
    f.write(convert_arr_to_str(arr))
    f.close()


def medium_task(arr):
    easy_task(arr)
    # pic_gen.main()
    with open("artifacts/easy_task.tex", "r") as old_tex:
        contents = old_tex.readlines()

    contents.insert(1, "\\usepackage{graphicx}\n")
    contents.insert(len(contents) - 1, "\includegraphics{artifacts/ast.png}\n")
    new_tex = open("artifacts/medium_task.tex", "w")
    new_tex.writelines(contents)


def main():
    arr = [["res: " + str(i + j) for j in range(8)] for i in range(7)]
    medium_task(arr)


if __name__ == "__main__":
    main()