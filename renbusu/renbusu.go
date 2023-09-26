package renbusu

import (
	"math/big"
)

func Solve(xs []int64) *big.Rat {
	return calc(xs, 0)
}

func calc(xs []int64, n int) *big.Rat {
	if n == len(xs)-1 {
		return big.NewRat(xs[n], 1)
	} else {
		ans := big.NewRat(0, 1)
		ans.Add(ans, big.NewRat(xs[n], 1))
		anplus1 := calc(xs, n+1)
		ans.Add(ans, anplus1.Inv(anplus1))
		return ans
	}
}
