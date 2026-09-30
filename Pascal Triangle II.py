class Solution:
    def getRowFromList(self, input_values: list[int]) -> list[int]:
        return self.getRow(input_values[0])
    def getRow(self, rowIndex: int) -> list[int]:
        result: list[int] = [1]
        current: int = 1
        for col in range(1, rowIndex + 1):
            current = current * (rowIndex - col + 1) // col
            result.append(current)
            return result
def main() -> None:
    rowIndex: int = 5
    sol: Solution = Solution()
    print(sol.getRow(rowIndex))
if __name__ == "__main__":
    main()