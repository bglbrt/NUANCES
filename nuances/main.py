#!/usr/bin/env
# -*- coding: utf-8 -*-

# this source code is licensed under the MIT license found in the LICENSE file in the root directory of this source tree

# I/O packages
import os
import glob
import argparse
import warnings

# dependencies
from data.preprocessing import Preprocessor
from models.language_model import LanguageModel


# define parser
parser = argparse.ArgumentParser(prog="Nuances",
                                 description="A Tool for Contextual Word Embeddings' Graphical Analysis and Visualisation",
                                 epilog="This source code is licensed under a MIT license.")

# define arguments
parser.add_argument("--corpus", nargs="1", default=None, type=str, help="Path to .txt file or folder of .txt files containing the corpus.")
parser.add_argument("--source_vocabulary", nargs="?", default=None, type=str, help="List of words or .txt file containing the source vocabulary.")
parser.add_argument("--target_vocabulary", nargs="?", default=None, type=str, help="List of words or .txt file containing the target vocabulary.")
parser.add_argument("--expand_source_vocabulary", default=False, type=bool, help="Expand source vocabulary with words from the corpus (see documentation for methodology).")
parser.add_argument("--language_model", nargs=1, default="bert-base", type=str, help="Language model to use for the contextual word embeddings. Options: bert, roberta, ...")
parser.add_argument("--dimensionality_reduction_method", nargs=1, default="pca", type=str, help="Dimensionality reduction method to use for the embeddings. Options: pca, t-sne, umap, ...")
parser.add_argument("--output_plot", nargs=1, default=None, type=str, help="Type of output plot. Options are: ..., ..., ...")
parser.add_argument("--output_dimension", nargs=1, default=2, type=int, help="Number of dimensions in the output plot. Options are: 1, 2, 3.")
parser.add_argument("--output_format", nargs=1, default=".jpg", type=str, help="Format of output. Options are: .jpg, .png, .svg.")
parser.add_argument("--output_path", nargs=1, default=None, type=str, help="Path to output folder.")
#parser.add_argument("-...", nargs=1, default=None, type=str, help="...")

# parse arguments
args = parser.parse_args()

# process corpus argument to obtain a list of files
if args.corpus is not None:
    if args.corpus.endswith(".txt"):
        args.corpus = list(args.corpus)
    elif os.path.isdir(args.corpus):
        files = glob.glob(args.corpus + "/*.txt")
        if len(files) >= 1:
            args.corpus = files
        else:
            raise ValueError("Source vocabulary folder contains no .txt file.")
    else:
        raise ValueError("Corpus must be a .txt file or a folder containing .txt files.")
else:
    raise ValueError("No corpus specified.")

# process source vocabulary argument to obtain a list of words
if args.source_vocabulary is not None:
    if len(args.source_vocabulary) == 1:
        if args.source_vocabulary[0].endswith(".txt"):
            with open(args.source_vocabulary[0]) as f:
                args.source_vocabulary = [word for line in f for word in line.split()]
    elif len(args.source_vocabulary) => 1:
        pass
    else:
        raise ValueError("Source vocabulary must be a .txt file or a folder containing .txt files.")
else:
    raise ValueError("No source vocabulary specified.")

# process target vocabulary argument to obtain a list of words or None
if args.target_vocabulary is not None:
    if len(args.target_vocabulary) == 1:
        if args.target_vocabulary[0].endswith(".txt"):
            with open(args.target_vocabulary[0]) as f:
                args.target_vocabulary = [word for line in f for word in line.split()]
    elif len(args.target_vocabulary) => 1:
        pass
    else:
        raise ValueError("Source vocabulary must be a .txt file or a folder containing .txt files.")   

# process output path argument
if args.output_path is not None:
    if not os.path.isdir(args.output_path):
        raise ValueError("Output path must be an existing folder.")
else:
    warnings.warn("No output type specified. Default output type is set to current working directory.")
    args.output_path = os.getcwd()

# load pre-processing pipeline
preprocessor = Preprocessor(...)

# load language model
embedder = LanguageModel(language_model)

# load dimensionality reduction model
reducer = DimensionalityReducer(dimensionality_reduction_metho, output_dimension)

def main():
    """
    Main function. 
    """

    # step 1: data pre-preprocessing

    # step 2: computation 1 - embeddings

    # step 3: computation 2 - dimensionality reduction

    # step 4: data visualisation

# run main function
if __name__ == "__main__":
    main()