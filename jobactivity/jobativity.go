package jobactivity

import "slices"

type Answer struct {
	Begin int
	End   int
}

func Solve(days []int) Answer {
	begin := 0
	end := 0
	maxSpan := 0
	for _, d := range days {
		span := 1
		for slices.Contains(days, d+span) {
			span += 1
		}
		if span > maxSpan {
			maxSpan = span
			begin = d
			end = d + span - 1
		}
	}
	return Answer{begin, end}
}
