import difflib

text1='this is a new line\nhi\nhow old are you\nand you'
text2='hi\nhow new are you\nand you\nfdsa'

if __name__ == '__main__':
    d=difflib.Differ()
    diff=d.compare(text1.splitlines(),text2.splitlines())
    print('\n'.join(list(diff)))

    d_html=difflib.HtmlDiff()
    diff2=d_html.make_file(text1.splitlines(),text2.splitlines())
    with open('result.html','w') as f:
        f.writelines(diff2)
    # print(diff2)