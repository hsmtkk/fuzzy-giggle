package xmassale

import "sort"

type Input struct {
	Threshold int
	Free      int
	Prices    []int
}

func Solve(input Input) int {
	if len(input.Prices) < input.Threshold {
		return sum(input.Prices)
	}
	sortedPrices := input.Prices[:]
	sort.Sort(sort.Reverse(sort.IntSlice(input.Prices)))
	nonFreeCounts := len(input.Prices) - input.Free
	return sum(sortedPrices[:nonFreeCounts])
}

func sum(ns []int) int {
	sum := 0
	for _, n := range ns {
		sum += n
	}
	return sum
}
