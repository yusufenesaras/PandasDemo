import pandas as pd # pandas kütüphanesini import ettik.

df = pd.read_csv("Data/GBvideos.csv")  # verimizi pandas ile okuduk.
# result = df.head(10) # ilk 10 kaydımızı önizledik.


# result = df.columns # tüm kolonları çektik.
# result = len(df.columns) #kolonların sayısı gösterir.


# Çektiğimiz verideki istediğimiz kolonları çekelim.
# yani drop ile bu kolonları silelim.
"""df = df.drop(["thumbnail_link",
              "comments_disabled",
              "ratings_disabled",
              "video_error_or_removed",
              "description"],
               axis = 1,) # axis belirtmemiz lazım yoksa default olarak satırı baz alır.
# aldığımız veride bu kolonları seçip analiz edelim."""

# result = df


# Like ve Dislike sayılarının ortalamasını bulalım.

# result = df["likes"].mean() #bütün videolardaki like ların ortalamaları gelir.
# result = df["dislikes"].mean() #bütün videolardaki dislike ların ortalamaları gelir.


# şimdi ilk 50 videonun like ve dislike kolonlarını getirelim.

# result = df.head(50)[["title","likes","dislikes"]]


# En çok görüntülenen video' yu bulalım

# result = df[df["views"].max() == df["views"]]["title"].iloc[0]#Views görüntüleme kolonudur.
# max metodu ile bir arama gerçekleştirisek bize en çok görüntülenen video gelir.


# En düşük görüntülenen video' yu bulalım
# result = df[(df["views"].min()) == df["views"]][["title","views"]] # max yerine min yaptık


# En fazla görüntülenen ilk 10 video' yu bulalım.
# result = df.sort_values("views", ascending = False)[["title","views"]] # burayı çalıştırısak en çoktan az' a doğru gider.
# result = df.sort_values("views", ascending = False)[["title","views"]].head(10) # burada ilk 102 u buluruz.
# sıralama işlemi yine views' e göre yapılır.
# ama böyle yaparsak en azdan en fazlaya doğru gider.
# Sort ile sıralama yaptığımızda 1. indexten başlar bu durumda en düşükten başlar.
# Tersten sıralarsak sorun çözülür. Bunu da ascending ile yaparız.


# Kategoriye göre beğeni ortalamalarını sıralı şekilde getirelim.
result = df.groupby("category_id").mean().sort_values("likes")[
    "likes"]  # groupby ile category_id 'ye göre  gruplama yaparız. mean() metodu ile ortalaması alınmış şekilde gelir.

# Her kategoride kaç video vardır?
result = df["category_id"].value_counts()  # value_counts category_id ye karşılık gelen değerleri sayar.


# Her video için kullanılan tag sayısını yeni kolonda gösterelim.


def tagCount(tag):
    return len(tag.split('|'))


result = df["tag_count"] = df["tags"].apply(
    tagCount)  # metoda bir tag gidicek ve tagi | split edip(ayırıp) geriye sayısını döndürecek.

# En popüler videoları like/dislike oranına göre listeleyelim.

"""likesList = list(df["likes"])
dislikesList = list(df["dislikes"])"""  # burada like ve dislike ları görüntülüyebiliriz. bunları metoda alalım.


def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList, dislikesList))  # zip ile tuple ile ayırmamızı sağlıyor.
    # yani her videonun like ve dislike ayır olarak tuple içerisinde gelir.

    oranListesi = []

    for like, dislike in liste:  # (212,1212)
        if (like + dislike) == 0:  # beğeni sayısı yoksa yani nötrse popülerlik oranını sıfır yaparız.
            oranListesi.append(0)
        else:
            oranListesi.append(like / (like + dislike))  # buradaki oran popülerlik orarını verir.

    return oranListesi


df["beğeni_orani"] = likedislikeoranhesapla(df)

print(df.sort_values("beğeni_orani", ascending=False)[["title", "likes", "dislikes", "beğeni_orani"]])

# yine beğeni_orani ' na göre sıralama yapıp
# ascending ile popülerliği en fazla olandan başlattık.
