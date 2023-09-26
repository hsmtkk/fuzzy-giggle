package tricktreat

import "slices"

type Problem struct {
	N    int
	M    int
	K    int
	Boys []int
}

func Solve(p Problem) int {
	surprised := 0
	treat := 0
	for i := 1; i <= p.N; i++ {
		if slices.Contains(p.Boys, i) {
			surprised += 1
			if surprised >= p.K {
				break
			}
		} else {
			surprised = 0
			treat += 1
		}
	}
	return treat
}
