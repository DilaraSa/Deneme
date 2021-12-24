from pytube import YouTube

url = input("Video Bağlantısını Giriniz:")
yt = YouTube(url)
if yt.length > 120:
    question = input("Videoyu İndirmek İstiyor Musunuz? (Evet/Hayır): ")
    if question== "Evet":
        print("Video İndiriliyor...")
    else:
        print("Video İndirilmeye İzin Verilmedi Veya Yanlış Komut Yazıldı")
video1 = yt.streams.filter(progressive=True).get_by_itag(22)
video1.download()