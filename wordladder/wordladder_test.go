package wordladder_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/wordladder"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	words := wordladder.NewWords([]string{"apPle", "error", "suBway", "Zb"})
	problem := wordladder.NewProblem(words)
	chained, got := wordladder.New().Solve(problem)
	want := wordladder.NewAnswer(wordladder.NewChar("r"), wordladder.NewChar("s"))
	assert.False(t, chained)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	words := wordladder.NewWords([]string{"idIOh", "hiKoQA", "AbijoD", "djgeldi", "kjoial"})
	problem := wordladder.NewProblem(words)
	chained, got := wordladder.New().Solve(problem)
	want := wordladder.NewAnswer(wordladder.NewChar("D"), wordladder.NewChar("d"))
	assert.False(t, chained)
	assert.Equal(t, want, got)
}

func Test3(t *testing.T) {
	words := wordladder.NewWords([]string{"adijA", "Akq", "qZR"})
	problem := wordladder.NewProblem(words)
	chained, _ := wordladder.New().Solve(problem)
	assert.True(t, chained)
}
