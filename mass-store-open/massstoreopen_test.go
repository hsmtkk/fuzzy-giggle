package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	p := Problem{
		1000,
		1000,
		50,
		3,
		[]int{25, 500, 80},
	}
	want := 1
	got := Solve(p)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	p := Problem{
		2556,
		3424,
		77,
		3,
		[]int{137, 721, 984, 999},
	}
	want := 1
	got := Solve(p)
	assert.Equal(t, want, got)
}
