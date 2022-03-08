"""Parse a directory of files into a json based ngram structure

Returns:
    json : ngram data structure
"""

import argparse
from functools import reduce
import json
from rich import print_json
from nltk.util import ngrams
import nltk.corpus


def ngram_builder(ngram_dict, rawstr, depth):
    strlist = list(rawstr.encode("ascii", "ignore").decode().lower())
    ngram_tup = list(ngrams(strlist, depth))

    def convert_tup2dict(nrgam_tup, n_dict: dict):
        if len(nrgam_tup) > 0:
            x = nrgam_tup[0]
            n_dict.setdefault(x, {"__count__": 0})
            n_dict[x] = convert_tup2dict(nrgam_tup[1:], n_dict[x])
            n_dict[x]["__count__"] = n_dict[x]["__count__"] + 1
        return n_dict

    def convert_tuplist2dict(nrgam_tup_list, n_dict: dict):
        for ngram in nrgam_tup_list:
            convert_tup2dict(ngram, n_dict)
        return n_dict

    ngram_dict = convert_tuplist2dict(ngram_tup, ngram_dict)

    return ngram_dict


def parse_user_aguments():
    """parse the users aguments from the terminal

    Returns:
        object : user arguments
    """
    parser = argparse.ArgumentParser(description='Add files to ngram json')
    parser.add_argument('--json', dest='ngram_file', type=str,
                        help=("location of json file used to store ngram output."
                              " If the file doesn't exist it will be created"))
    # parser.add_argument('--input', dest='data_dir', type=str,
    #                     help="directory of files to parse")
    parser.add_argument('--depth', dest='depth', type=int, default=3,
                        help="depth of nrgam")
    args = parser.parse_args()
    return args


def default_json_for_ngram():
    """Generate the default json structure for an ngram

    Returns:
        dict: default json ngram structur
    """
    default_json = {
        # "_reading_corpus": [],  # list of references used to generate ngram
        # "_ngrams": {
        #     "_letters": {},  # ngram for letter
        #     "_words": {}  # nrgam for words
        # }
    }
    return default_json


def open_json(filepath, default_data):
    """parse a json file

    Args:
        filepath (str): load location
        default_data (dict): default json data if file is not found

    Returns:
        dict: parsed_json
    """
    try:
        with open(filepath, 'r') as json_file:  # open file in append mode
            parsed_json = json.load(json_file)
    except:
        parsed_json = default_data
        with open(filepath, 'a+')as json_file:  # open file in append mode
            json.dump(parsed_json, json_file, ensure_ascii=False, indent=4)

    return parsed_json


def save_json(filepath, json_data):
    """save json to a json file

    Args:
        filepath (str): save location
        json_data (dict): json data to be saved to file

    Returns:
        dict: parsed_json
    """
    with open(filepath, 'w')as json_file:  # open file in append mode
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)


def main():
    """generate ngram data from text files
     """
    user_args = parse_user_aguments()
    print(user_args)
    ngram_dict = open_json(user_args.ngram_file, default_json_for_ngram())
    #corpus = [nltk.corpus.webtext.raw(), nltk.corpus.brown.raw()]
    save_json(
        user_args.ngram_file,
        ngram_builder(ngram_dict, nltk.corpus.webtext.raw(), user_args.depth)
    )


if __name__ == "__main__":
    main()
