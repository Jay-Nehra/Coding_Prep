from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        compress = []
        count = 1
        current = chars[0]

        for char in chars[1:]:
            if char == current:
                count += 1
            else:
                compress.append(current)
                if count > 1:
                    compress.extend(list(str(count)))
                current = char
                count = 1

        compress.append(current)
        if count > 1:
            compress.extend(list(str(count)))

        chars[: len(compress)] = compress
        return len(compress)
