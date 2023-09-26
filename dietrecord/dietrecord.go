package dietrecord

type Answer struct {
	Diet   int
	NoDiet int
}

func Solve(weights []int) Answer {
	up := 0
	down := 0
	diets := []int{}
	noDiets := []int{}
	for i := 0; i < len(weights)-1; i++ {
		this := weights[i]
		next := weights[i+1]
		if this < next {
			up += 1
			diets = append(diets, down)
			down = 0
		} else {
			down += 1
			noDiets = append(noDiets, up)
			up = 0
		}
	}
	diets = append(diets, down)
	noDiets = append(noDiets, up)
	return Answer{max(diets), max(noDiets)}
}

func max(ns []int) int {
	max := ns[0]
	for _, n := range ns {
		if n > max {
			max = n
		}
	}
	return max
}
