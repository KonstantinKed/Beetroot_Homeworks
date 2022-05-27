# with open('spider.txt', "r") as file:
#     file.write("FUCK, FUCK and FUCK again PUTIN,\nPuTIN HUILO, LA-la-la-la-la-la-la-la\nPuTIN HUILO, LA-la-la-la-la-la-la-la\nPuTIN HUILO, LA-la-la-la-la-la-la-la\nPuTIN HUILO, LA-la-la-la-la-la-la-la\nPuTIN HUILO, LA-la-la-la-la-la-la-la")

file = open('spider.txt')
def count_lines(f):
    line_amount = len(f.readlines())
    return line_amount
print(count_lines(file))


file = open('spider.txt')
def count_chars(f):
    string_amount = len(f.read())
    return string_amount
print(count_chars(file))


file = open('spider.txt')
def test(f):
    liiin = count_lines(f)
    file.seek(0)
    chaars = count_chars(f)
    message = (f"Our song consists from {liiin} lines, and has {chaars} chars in total")
    return message
print(test(file))


