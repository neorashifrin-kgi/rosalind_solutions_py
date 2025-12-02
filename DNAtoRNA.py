{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM6XNw8ljDzWbuS87bTWeIB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/neorashifrin-kgi/rosalind_solutions_py/blob/main/DNAtoRNA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "RNA"
      ],
      "metadata": {
        "id": "3iFwC6RkB963"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0aXM9OwzrOl3"
      },
      "outputs": [],
      "source": [
        "#GATGGAACTTGACTACGTAAATT"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The following code intakes a DNA sequence as an input and will return its complementary RNA sequence"
      ],
      "metadata": {
        "id": "1S3kwmz2s5ZP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def DNA_to_RNA(sequence):\n",
        "  RNA_Dictionary = {\"A\":\"A\", \"G\":\"G\", \"C\":\"C\", \"T\":\"U\"}\n",
        "  return \"\".join(RNA_Dictionary[nucleotide] for nucleotide in sequence) #start with an empty string and for every nucleotide in our input sequence match with its value from our RNA dictionary and join that into our empty string"
      ],
      "metadata": {
        "id": "fVxr6v11rW9l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "DNA_to_RNA (\"GATGGAACTTGACTACGTAAATT\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "7Fe7MA2_swiE",
        "outputId": "77b42bc7-7b8c-44ee-ab0c-8a4548fadfbc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'GAUGGAACUUGACUACGUAAAUU'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    }
  ]
}