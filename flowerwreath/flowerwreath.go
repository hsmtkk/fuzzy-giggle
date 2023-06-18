package flowerwreath

type Problem struct {
	First  string
	Second string
}

func Solve(p Problem) bool {
	patterns := Rotate(p.First)
	_, ok := patterns[p.Second]
	return ok
}

func Rotate(s string) map[string]bool {
	patterns := map[string]bool{}
	t := s
	for i := 0; i < len(s); i++ {
		patterns[t] = true
		t = t[1:] + string(t[0])
	}
	return patterns
}
