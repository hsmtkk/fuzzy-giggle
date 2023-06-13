package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type testCase struct {
	intervals []int
	threshold int
	want      int
}

func TestCalculate(t *testing.T) {
	testCases := []testCase{
		{[]int{5, 6, 25, 4}, 10, 15},
		{[]int{30, 10, 40}, 30, 40},
	}
	calculator := new()
	for _, tc := range testCases {
		got := calculator.Calculate(tc.intervals, tc.threshold)
		assert.Equal(t, tc.want, got)
	}
}
