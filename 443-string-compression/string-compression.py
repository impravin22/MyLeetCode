class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) <= 1:
            return len(chars)
        current = chars[0]
        count = 0
        result = []
        for element in chars:
            if element == current:
                count += 1
            else:
                result.append(current)
                if count >= 10:
                    elem = list(str(count))
                    for i in elem:
                        result.append(i)
                elif count > 1 and count < 10:
                    result.append(str(count))
                # result.append(str(count))
                count = 1
                current = element
        
        result.append(current)
        if count >= 10:
            elem = list(str(count))
            for i in elem:
                result.append(i)
        elif count > 1:
            result.append(str(count))

        chars[0:len(result)+1] = result

        return len(result)