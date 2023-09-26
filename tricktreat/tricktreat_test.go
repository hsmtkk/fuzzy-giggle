package tricktreat_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/tricktreat"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	p := tricktreat.Problem{6, 3, 2, []int{2, 4, 5}}
	want := 2
	got := tricktreat.Solve(p)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	p := tricktreat.Problem{10, 4, 3, []int{1, 5, 6, 9}}
	want := 6
	got := tricktreat.Solve(p)
	assert.Equal(t, want, got)
}
