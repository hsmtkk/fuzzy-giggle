package expresshotel_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/expresshotel"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	want := 1100
	p := expresshotel.Problem{
		ExpressFee: 200,
		HotelFee:   300,
		InternshipDays: []expresshotel.Internship{
			{1, 3},
			{4, 6},
			{8, 10},
		},
	}
	got := expresshotel.Solve(p)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	want := 223
	p := expresshotel.Problem{
		ExpressFee: 100,
		HotelFee:   1,
		InternshipDays: []expresshotel.Internship{
			{1, 2},
			{10, 15},
			{30, 50},
		},
	}
	got := expresshotel.Solve(p)
	assert.Equal(t, want, got)
}
