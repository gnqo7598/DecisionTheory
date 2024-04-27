# 중간과제 2번 선택

# 사용자 정의 함수부
# 세 값의 최댓값 반환 함수
def chooseMax(value1, value2, value3):
    if value1 >= value2:
        if value1 >= value3:
            return value1
        else:
            return value3
    else:
        if value2 >= value3:
            return value2
        else:
            return value3

# 최적의 대안 선정 함수
def printMaxAlt(value1, value2, value3):
    max_value = chooseMax(value1, value2, value3)
    # 중복을 허용해서 최댓값에 해당하는 대안의 알파벳 번호 조합
    res = ''
    if value1 == max_value:
        res += 'A'
    if value2 == max_value:
        if res != '':
            res += ', '
        res += 'B'
    if value3 == max_value:
        if res != '':
            res += ', '
        res += 'C'
    print(f'{res} 대안이 선정되었습니다.')

# 주 프로그램부
# 대안 3개의 각 미래 저수요 및 고수요 입력
print('대안 3개의 미래 수요가 낮을 떄와 높을 떄의 각 수치를 입력받습니다.')
demand1_Low = int(input('A 대안의 미래 저수요 입력:'))
demand1_High = int(input('A 대안의 미래 고수요 입력:'))
demand2_Low = int(input('B 대안의 미래 저수요 입력:'))
demand2_High = int(input('B 대안의 미래 고수요 입력:'))
demand3_Low = int(input('C 대안의 미래 저수요 입력:'))
demand3_High = int(input('C 대안의 미래 고수요 입력:'))

# 의사결정 기준 입력
print('사용할 의사결정 기준을 입력받습니다.')
print('1. 최대최소(maximin) 기준: 최악의 경우 중 가장 나은 대안 선정')
print('2. 최대최대(maximax) 기준: 최선의 경우 중 가장 나은 대안 선정')
print('3. 라플라스(Laplace) 기준: 가중평균 보상이 가장 나은 대안 선정')
print('4. 최소최대 후회(minimax regret) 기준: 최악의 후회가 가장 최소화되는 대안 선정')
criteria = int(input('사용할 의사결정 기준 번호 입력:'))

# 최대최소 기준
if criteria == 1:
    printMaxAlt(demand1_Low, demand2_Low, demand3_Low)
# 최대최대 기준
elif criteria == 2:
    printMaxAlt(demand1_High, demand2_High, demand3_High)
# 라플라스 기준
elif criteria == 3:
    # 가중평균 계산
    average1 = 0.5 * (demand1_Low + demand1_High)
    average2 = 0.5 * (demand2_Low + demand2_High)
    average3 = 0.5 * (demand3_Low + demand3_High)
    printMaxAlt(average1, average2, average3)
# 최소최대 후회 기준
elif criteria == 4:
    # 저/고수요의 최댓값 선정
    demandMax_Low = chooseMax(demand1_Low, demand2_Low, demand3_Low)
    demandMax_High = chooseMax(demand1_High, demand2_High, demand3_High)
    # 각 대안의 최대 후회 선정
    regret1 = chooseMax(demandMax_Low - demand1_Low, demandMax_High - demand1_High, 0)
    regret2 = chooseMax(demandMax_Low - demand2_Low, demandMax_High - demand2_High, 0)
    regret3 = chooseMax(demandMax_Low - demand3_Low, demandMax_High - demand3_High, 0)
    # 가장 낮은 후회가 최적의 대안이므로 음수로 변환
    printMaxAlt(-regret1, -regret2, -regret3)
else:
    print('올바르지 않은 의사결정 기준값입니다.')