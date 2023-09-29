package jobactivity_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/jobactivity"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	days := []int{1, 2, 4, 5, 6, 9, 10, 11, 13}
	want := jobactivity.Answer{4, 6}
	got := jobactivity.Solve(days)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	days := []int{2, 4, 6}
	want := jobactivity.Answer{2, 2}
	got := jobactivity.Solve(days)
	assert.Equal(t, want, got)
}
