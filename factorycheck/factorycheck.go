package factorycheck

func Solve(expected, input []int) bool {
	counter := map[int]int{}
	for _, n := range input {
		count, ok := counter[n]
		if !ok {
			count = 0
		}
		counter[n] = count + 1
	}
	for _, n := range expected {
		count, ok := counter[n]
		if !ok {
			return false
		}
		if count == 0 {
			return false
		}
		counter[n] = count - 1
	}
	return true
}
