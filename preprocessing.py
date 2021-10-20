# from fairseq_cli.preprocess import cli_main
# from fairseq import options, tasks, utils
# from fairseq.logging import meters, metrics, progress_bar
# import torch

with open("ice_train.tsv", "r") as source:
    with open("train.ice.g", "w") as sink_word:
        with open("train.ice.p", "w") as sink_ipa:
            for row in source:
                row = row.split("\t")
                word = row[0]
                ipa = (row[1]).strip()
                word_with_spaces = ""
                for letter in word:
                    word_with_spaces = word_with_spaces + letter + " "
                print(word_with_spaces, file=sink_word)
                print(ipa, file=sink_ipa)
