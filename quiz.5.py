# -*- coding:utf-8 -*- #
'''
수박수박수박수박수?

문제 설명
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.
'''

n = 5
#수박수박수

def solution(n):
  if n >= 0:
      answer = '수'
      for i in range(1,n):
        if answer[-1] == '수':
          answer += '박'
        elif answer[-1] == '박':
          answer += '수'
  else:
    print('n is letter than 0')
    answer = None
  return answer

print(solution(n))