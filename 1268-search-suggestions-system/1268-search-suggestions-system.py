class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        ans = []
        prefix = ""

        for ch in searchWord:
            prefix += ch  # Ek ek letter add karo
            temp = []

            for p in products:
                if p.startswith(prefix):  # Prefix match karo
                    temp.append(p)

                if len(temp) == 3:  # Sirf 3 suggestions
                    break

            ans.append(temp)

        return ans