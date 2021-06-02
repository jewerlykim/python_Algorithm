def solution(S):
    files = list(map(str, S.split("\n")))
    music_extension = {'mp3', 'aac', 'flac'}
    image_extension = {'jpg', 'bmp', 'gif'}
    movie_extension = {'mp4', 'avi', 'mkv'}
    music_bytes = 0
    image_bytes = 0
    movie_bytes = 0
    other_bytes = 0

    for file in files:
        info = list(map(str, file.split(" ")))
        extension_list = list(map(str, info[0].split(".")))
        if extension_list[-1] in music_extension:
            music_bytes += int(info[1][:-1])
        elif extension_list[-1] in image_extension:
            image_bytes += int(info[1][:-1])
        elif extension_list[-1] in movie_extension:
            movie_bytes += int(info[1][:-1])
        else:
            other_bytes += int(info[1][:-1])
    answer = "music {}b".format(music_bytes) + "\n" + "images {}b".format(image_bytes) + "\n" + "movies {}b".format(movie_bytes) + "\n" + "other {}b".format(other_bytes)


    return answer

solution("my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b")