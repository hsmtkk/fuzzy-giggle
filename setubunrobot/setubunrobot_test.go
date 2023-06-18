package setubunrobot_test

import (
	"testing"

	"github.com/hsmtkk/fuzzy-giggle/setubunrobot"
	"github.com/stretchr/testify/assert"
)

func Test1(t *testing.T) {
	p := setubunrobot.Problem{Members: []uint{10, 20, 30, 40, 50}, Turns: []setubunrobot.Turn{{1, 3, 10}, {0, 2, 15}}}
	want := setubunrobot.Answer{[]uint{10, 20, 25, 10, 0}}
	got := setubunrobot.New().Distribute(p)
	assert.Equal(t, want, got)
}

func Test2(t *testing.T) {
	p := setubunrobot.Problem{Members: []uint{3, 1, 4}, Turns: []setubunrobot.Turn{{0, 0, 2}}}
	want := setubunrobot.Answer{[]uint{2, 0, 0}}
	got := setubunrobot.New().Distribute(p)
	assert.Equal(t, want, got)
}
