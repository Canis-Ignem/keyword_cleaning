import pandas as pd
import os

def clean_keywords(data, lang, keyword):

    data_copy = data[data["original"].str.contains(keyword)]
    data_copy = data_copy[data["language"] == lang]

    for i in data_copy.index:

        if keyword not in data_copy["translation"][i]:
            data.drop(i, inplace=True)

    return data

def data_cleaning(data, keyword, languages):

    for lang in languages:

        data = clean_keywords(data, lang, keyword)
    
    data.to_csv("Data/clean_skills.tsv", sep="\t", index=False)
    return data


def main(pth, non_translators):

    data = pd.read_csv(pth, sep="\t")
    print("Data has", data.shape[0], "rows")
    for word in os.listdir(non_translators):

        languages = pd.read_csv(non_translators+ "/" + word, sep="\t")["languages"].tolist()
        print(word[:-4])
        print(languages)
        data = data_cleaning(data, word[:-4], languages)
        data.reset_index(inplace=True)
    print("After cleaning data has", data.shape[0], "rows")
main("Data\skills.tsv", "non-translators")
