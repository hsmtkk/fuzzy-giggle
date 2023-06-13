package jetlag_test

import (
	"testing"

	jetlag "github.com/hsmtkk/fuzzy-giggle/jet-lag"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	records := []jetlag.Record{
		jetlag.NewRecord(jetlag.NewHour(7), jetlag.NewHour(5), jetlag.NewHour(12)),
		jetlag.NewRecord(jetlag.NewHour(10), jetlag.NewHour(6), jetlag.NewHour(20)),
		jetlag.NewRecord(jetlag.NewHour(12), jetlag.NewHour(3), jetlag.NewHour(8)),
	}
	p := jetlag.NewProblem(records)
	want := jetlag.NewAnswer(jetlag.NewHour(20), jetlag.NewHour(31))
	got := jetlag.Solve(p)
	assert.Equal(t, want, got)
}
