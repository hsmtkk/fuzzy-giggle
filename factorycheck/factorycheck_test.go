package factorycheck_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/factorycheck"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	expected := []int{1, 2, 1, 2, 3}
	input := []int{2, 1, 3, 2, 1}
	got := factorycheck.Solve(expected, input)
	assert.True(t, got)
}

func Test2(t *testing.T) {
	expected := []int{3, 1, 4}
	input := []int{1, 5, 2}
	got := factorycheck.Solve(expected, input)
	assert.False(t, got)
}
