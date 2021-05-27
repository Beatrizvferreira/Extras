{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercício 3.4 - Algobio",
      "provenance": [],
      "authorship_tag": "ABX9TyNc1yKEp96nOSCx51gzjo58",
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
        "<a href=\"https://colab.research.google.com/github/Beatrizvferreira/Extras/blob/master/Exerc%C3%ADcio%203.4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8AVCDfyx52dF",
        "outputId": "24abeffe-4cbb-403c-bf99-917d935dfc23"
      },
      "source": [
        "pip install numpy"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (1.19.5)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IgVRlSXyD-JD",
        "outputId": "bb0205f4-7a65-40a8-84a6-debc7131652e"
      },
      "source": [
        "dados = {}\n",
        "pessoas = []\n",
        "#num = int(input('Quantas pessoas irá cadastrar?'))\n",
        "for i in range(2):\n",
        "  dados['Nome'] = str(input('Qual o nome?'))\n",
        "  dados['Sexo'] = str(input('Qual o sexo? (M/F)'))\n",
        "  dados['Peso'] = float(input('Qual o peso?'))\n",
        "  dados['Altura'] = float(input('Qual é a altura?'))\n",
        "  dados['IMC'] = dados['Peso']/(dados['Altura']*dados['Altura'])\n",
        "  pessoas.append(dados.copy())\n",
        "\n",
        "num = len(pessoas)\n",
        "print(f'Foi/foram cadastrada(s) {num} pessoa(s)')\n",
        "\n",
        "soma_peso = 0\n",
        "soma_altura =0 \n",
        "soma_imc =0\n",
        "for i in pessoas:\n",
        "  for k,v in i.items():\n",
        "    if k == 'Peso':\n",
        "      soma_peso += v\n",
        "    elif k == 'Altura':\n",
        "      soma_altura += v\n",
        "    elif k == 'IMC':\n",
        "      soma_imc += v\n",
        "\n",
        "print(f'O peso médio das pessoas é {soma_peso/num:.2f}\\m')\n",
        "print(f'O peso médio das pessoas é {soma_altura/num:.2f}')\n",
        "print(f'O peso médio das pessoas é {soma_imc/num:.2f}')\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Qual o nome?bia\n",
            "Qual o sexo? (M/F)F\n",
            "Qual o peso?50\n",
            "Qual é a altura?1.8\n",
            "Qual o nome?Rafa\n",
            "Qual o sexo? (M/F)M\n",
            "Qual o peso?40\n",
            "Qual é a altura?2.0\n",
            "O(s) número(s) de pessoa(s) cadastrada(s) é(são) 2\n",
            "O peso médio das pessoas é 45.0\\m\n",
            "O peso médio das pessoas é 1.9\n",
            "O peso médio das pessoas é 12.716049382716049\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UzYI_iqpXx4b"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}