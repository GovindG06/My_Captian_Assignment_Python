{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOq26AhvDpL8TaTv4rnlv0G",
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
        "<a href=\"https://colab.research.google.com/github/GovindG06/My_Captian_Assignment_Python/blob/main/Assignment%201.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d7wXWKzKo7RX",
        "outputId": "04cd7ddd-f886-484e-e603-131cf28b459c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input the radius of the circle : 5\n",
            "The area of the circle with radius 5 is: 25\n"
          ]
        }
      ],
      "source": [
        "# write a program which accepts the radius of a circle from the user and computes area \n",
        "r = int(input(\"Input the radius of the circle : \"))\n",
        "area = r*r\n",
        "print('The area of the circle with radius', r,'is:',area)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#write a python program to accept a filename from the user and print the extension of that\n",
        "a=input()\n",
        "n = len(a)\n",
        "if a[n-2:n]==\"py\":\n",
        "  print(\"python\")\n",
        "else:\n",
        "  print(\"invalid\")  "
      ],
      "metadata": {
        "id": "MmO14F5KpieB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "921edf5d-a492-4a82-fb03-a745be59187e"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fdfdf.py\n",
            "python\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Fr85uU5l_xv5"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}