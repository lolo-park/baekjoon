"""
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때,
3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

정확하게 N kg 를 만들 수 없다면 -1 을 출력

전제 - 설탕 N킬로그램 배달, 봉지로 배달 (3kg, 5kg) 두 종류.
조건 - 최대한 적은 봉지를 들고 가고싶음
      18kg 설탕 배달 시 (3kg 6개) 말고 (5kg 3개와 3kg 1개) = return 4
출력 - "설탕"을 "N 킬로그램" 배달 해야 할 때, "봉지" "몇 개" 필요한 지 출력
      18 = [5, 5, 5, 3]  len() = 4 가 출력되어야한다는 건데


N 킬로그램의 N 을 인수로 받고
    N kg % 3 == 0 나머지가 없으면
    N kg % 5 == 0 나머지가 없으면




"""

def solution(N):
