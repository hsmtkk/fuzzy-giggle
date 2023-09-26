package xmassale_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/xmassale"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	prices := []int{500, 300, 400, 200, 100}
	input := xmassale.Input{3, 1, prices}
	want := 1400
	got := xmassale.Solve(input)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	prices := []int{400, 300, 200}
	input := xmassale.Input{5, 5, prices}
	want := 900
	got := xmassale.Solve(input)
	assert.Equal(t, want, got)
}
