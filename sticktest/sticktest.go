package sticktest

type Problem struct {
	Span   int
	Sticks []bool
}

func Solve(p Problem) bool {
	for i := 0; i < len(p.Sticks)-p.Span+1; i++ {
		sticks := p.Sticks[i : i+p.Span]
		if !any(sticks) {
			return false
		}
	}
	return true
}

func any(bs []bool) bool {
	for _, b := range bs {
		if b {
			return true
		}
	}
	return false
}
