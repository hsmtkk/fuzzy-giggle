package uniqueroomnumber_test

import (
	"testing"

	uniqueroomnumber "github.com/hsmtkk/fuzzy-giggle/unique-room-number"
	"github.com/stretchr/testify/assert"
)

func TestRotatedSame(t *testing.T) {
	assert.True(t, uniqueroomnumber.RotatedSame(86098))
	assert.False(t, uniqueroomnumber.RotatedSame(12345))
}

func Test1(t *testing.T) {
	want := 2
	got := uniqueroomnumber.Solve(1, 9)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	want := 32
	got := uniqueroomnumber.Solve(100, 10000)
	assert.Equal(t, want, got)
}
