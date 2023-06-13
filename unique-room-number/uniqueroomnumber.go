package uniqueroomnumber

import (
	"log"
	"strconv"
	"strings"
)

func Solve(begin, end int) int {
	count := 0
	for n := begin; n <= end; n++ {
		if containsUnreversableNumber(n) {
			continue
		}
		if RotatedSame(n) {
			count += 1
		}
	}
	return count
}

func containsUnreversableNumber(n int) bool {
	digits := int2Digits(n)
	if contains(digits, 2) {
		return true
	}
	if contains(digits, 3) {
		return true
	}
	if contains(digits, 4) {
		return true
	}
	if contains(digits, 5) {
		return true
	}
	if contains(digits, 7) {
		return true
	}
	return false
}

func RotatedSame(n int) bool {
	digits := int2Digits(n)
	digits = reverse(digits)
	digits = convert(digits)
	m := digits2Int(digits)
	return n == m
}

func reverse(ns []int) []int {
	ms := []int{}
	for _, n := range ns {
		ms = append([]int{n}, ms...)
	}
	return ms
}

func contains(ns []int, m int) bool {
	for _, n := range ns {
		if m == n {
			return true
		}
	}
	return false
}

var convertDict = map[int]int{
	0: 0,
	1: 1,
	6: 9,
	8: 8,
	9: 6,
}

func convert(ns []int) []int {
	ms := []int{}
	for _, n := range ns {
		ms = append(ms, convertDict[n])
	}
	return ms
}

func int2Digits(n int) []int {
	digits := []int{}
	for _, s := range strconv.Itoa(n) {
		d, err := strconv.Atoi(string(s))
		if err != nil {
			log.Fatalf("failed to parse %s as int: %v", string(s), err)
		}
		digits = append(digits, d)

	}
	return digits
}

func digits2Int(digits []int) int {
	ss := []string{}
	for _, d := range digits {
		ss = append(ss, strconv.Itoa(d))
	}
	s := strings.Join(ss, "")
	n, err := strconv.Atoi(s)
	if err != nil {
		log.Fatalf("failed to parse %s as int: %v", s, err)
	}
	return n
}
