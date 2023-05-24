song = str(input("Введите стих (вразы разделяются пробелом, слова разделяются знаком - )"))
letters = ["а","я","у","ю","о","е","ё","э","и","ы"]

def check_song(song):
    count = 0
    if len(song.split(" ")) != 1:
        for i in range(len(song.split(" "))):
            temp_count = 0
            word = song.split(" ")
            for j in range(len(word[i])):

                if str.lower(word[i][j]) in letters:
                    temp_count = temp_count + 1
            if i == 0:
                count = temp_count
            elif count != temp_count:
                return False
        return True
    else:
        print("В стихе всего 1 фраза")
        return False

if check_song(song) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")
