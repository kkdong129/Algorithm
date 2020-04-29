# -*- coding:utf-8 -*- #
'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백 문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야 합니다.
'''

s = "try hello world"
#return TrY HeLlO WoRlD

def solution(s):
  for i in range(len(s)):
    if i % 2 == 0:
      print(s[i].upper(), end="")
    else:
      print(s[i], end="")
  #print()

solution(s)