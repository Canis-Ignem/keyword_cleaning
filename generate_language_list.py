from os import sep
import pandas as pd

def generate_language_list(data, keyword):

    non_translators = []

    data = data[data["english"].str.contains(keyword)]

    green_occasions = len(data["english"].unique())
    languages = data["language"].unique()

    for language in languages:
        data_copy = data[data["language"] == language]
        count = 0
        for index, row in data_copy.iterrows():

            if keyword in row["translation"]:
               count += 1
            if count > green_occasions-1:
                non_translators.append(language)

    non_translators = pd.DataFrame(non_translators, columns=["languages"])
    non_translators.to_csv("non-translators/"+keyword+".tsv", sep="\t", index=False)
    print(non_translators)

def generate_language_list_all(pth, keywords = ["green" , "cloud", "six sigma"]):

    data = pd.read_csv(pth, sep="\t")

    for keyword in keywords:
        generate_language_list(data, keyword)

generate_language_list_all("Data\skill_pts.tsv")