# syntax=docker/dockerfile:1

FROM python:3.9
COPY . .
RUN apt-get update && apt-get -y upgrade
RUN pip install pdflatex
RUN apt-get install -y texlive graphviz graphviz-dev python3-pygraphviz
RUN pip install networkx==2.8
RUN pip install pygraphviz
RUN pip install -i https://test.pypi.org/simple/ testpackagefibbfunpicturegen==0.1.6
RUN python3 main.py
RUN pdflatex artifacts/medium_task.tex