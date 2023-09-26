package sticktest_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/sticktest"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	prob := sticktest.Problem{3, []bool{true, false, true, true, true}}
	want := true
	got := sticktest.Solve(prob)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	prob := sticktest.Problem{3, []bool{true, false, false, false, false, true}}
	want := false
	got := sticktest.Solve(prob)
	assert.Equal(t, want, got)
}
