from Fligt import Fligt
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def bild_list_Fligt(stg2):
    list_tabel = {}
    for x in range(1,len(stg2),8):
        emp=Fligt(stg2[x],stg2[x+1],stg2[x+2],stg2[x+3],stg2[x+4],stg2[x+5],stg2[x+6],stg2[x+7])
        list_tabel.update({stg2[x+1] : emp})
    return list_tabel


def seav_data(se,name):
    text_file = open(name+".txt", "w")
    n = text_file.write(se)
    text_file.close()

def seav_data_dec(se,name):
    text_file = open(name + ".txt", "w")
    for x in se:
        text_file.write(x)
        val = ": "+se[x]
        text_file.write(val)
    text_file.close()


def story_Good_bed(st):
    sna = SentimentIntensityAnalyzer()
    return sna.polarity_scores(st)
