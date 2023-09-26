package dietrecord_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/dietrecord"
	"github.com/stretchr/testify/assert"
)

func TestDietRecord(t *testing.T) {
	weights := []int{55, 56, 57, 55, 56, 53, 52, 50}
	want := dietrecord.Answer{3, 2}
	got := dietrecord.Solve(weights)
	assert.Equal(t, want, got)
}
