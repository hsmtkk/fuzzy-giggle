package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	correctOrNots := []CorrectOrNot{
		{true, false},
		{false, true},
		{false, false},
		{true, true},
	}
	want := []int{1, 2, 3}
	got := new().Solve(correctOrNots)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	correctOrNots := []CorrectOrNot{
		{true, true},
	}
	want := []int{}
	got := new().Solve(correctOrNots)
	assert.Equal(t, want, got)
}
