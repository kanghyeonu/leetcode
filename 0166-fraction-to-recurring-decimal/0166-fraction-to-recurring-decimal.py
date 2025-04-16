class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        result = []
      
        # 결과 양수 음수 처리
        is_negative = (numerator > 0) ^ (denominator > 0)
        if is_negative:
            result.append('-')

        numerator_abs = abs(numerator)
        denominator_abs = abs(denominator)

        # 정수 부분
        result.append(str(numerator_abs // denominator_abs))
      
        # 나머지 부분
        remainder = numerator_abs % denominator_abs
        # 나머지 없으면 리턴
        if remainder == 0:
            return ''.join(result)
      
        # 정수부분 처리 완료
        result.append('.')
      
        seen_remainders = {}

        # 나머지가 없거나, 패턴 반복까지 반복
        while remainder != 0:
            if remainder in seen_remainders:
                # 패턴 반복 위치에 () 처리
                idx = seen_remainders[remainder]
                result.insert(idx, '(')
                result.append(')')
                break

            # 나머지 추가, 발생 위치 저장
            seen_remainders[remainder] = len(result)

            # 다음 자릿 수 계산
            remainder *= 10
            result.append(str(remainder // denominator_abs))

            # 나머지 업데이트
            remainder %= denominator_abs

        return ''.join(result)