package idsort

import (
	"fmt"
	"log"
	"regexp"
	"sort"
	"strconv"
)

func Solve(words []string) []string {
	copied := make([]string, len(words))
	copy(copied, words)
	sort.Sort(BySuffix(copied))
	return copied
}

type BySuffix []string

func (words BySuffix) Len() int {
	return len(words)
}

func (words BySuffix) Less(i, j int) bool {
	numi, err := getSuffix(words[i])
	if err != nil {
		log.Fatal(err)
	}
	numj, err := getSuffix(words[j])
	if err != nil {
		log.Fatal(err)
	}
	return numi < numj
}

func (words BySuffix) Swap(i, j int) {
	words[i], words[j] = words[j], words[i]
}

func getSuffix(s string) (int, error) {
	compiled := regexp.MustCompile(`[a-z]+([0-9]+)`)
	matched := compiled.FindSubmatch([]byte(s))
	if len(matched) != 2 {
		return 0, fmt.Errorf("invalid string: %s", s)
	}
	number, err := strconv.Atoi(string(matched[1]))
	if err != nil {
		return 0, fmt.Errorf("failed to parse %s as int: %w", matched[1], err)
	}
	return number, nil
}
