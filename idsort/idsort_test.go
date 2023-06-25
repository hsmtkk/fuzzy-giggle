package idsort_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/idsort"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	orig := []string{"paiza1", "kirishima813", "pizza99", "sushi100", "beef1001"}
	want := []string{"paiza1", "pizza99", "sushi100", "kirishima813", "beef1001"}
	got := idsort.Solve(orig)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	orig := []string{"tanaka1192", "tanaka123", "tanaka95"}
	want := []string{"tanaka95", "tanaka123", "tanaka1192"}
	got := idsort.Solve(orig)
	assert.Equal(t, want, got)
}
