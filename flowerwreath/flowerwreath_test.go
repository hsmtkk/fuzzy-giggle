package flowerwreath_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/flowerwreath"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	got := flowerwreath.Solve(flowerwreath.Problem{"baaab", "aabba"})
	assert.True(t, got)
}

func Test2(t *testing.T) {
	got := flowerwreath.Solve(flowerwreath.Problem{"baaab", "abaab"})
	assert.False(t, got)
}

func TestRotate(t *testing.T) {
	got := flowerwreath.Rotate("baaab")
	want := map[string]bool{}
	for _, s := range []string{"baaab", "aaabb", "aabba", "abbaa", "bbaaa"} {
		want[s] = true
	}
	assert.Equal(t, want, got)
}
