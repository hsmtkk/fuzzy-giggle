package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Calculator interface {
	Calculate(intervals []int, threshold int) int
}

type calculatorImpl struct {
}

func new() Calculator {
	return &calculatorImpl{}
}

func (c *calculatorImpl) Calculate(intervals []int, threshold int) int {
	sum := 0
	for _, interval := range intervals {
		if interval <= threshold {
			sum += interval
		}
	}
	return sum
}

func readStdIn() ([]string, error) {
	lines := []string{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("failed to read standard input: %w", err)
	}
	return lines, nil
}

func strings2ints(ss []string) ([]int, error) {
	ints := []int{}
	for _, s := range ss {
		i, err := strconv.Atoi(s)
		if err != nil {
			return nil, fmt.Errorf("failed to parse %s as int: %w", s, err)
		}
		ints = append(ints, i)
	}
	return ints, nil
}

func main() {
	lines, err := readStdIn()
	if err != nil {
		log.Fatal(err)
	}
	threshold, err := strconv.Atoi(strings.Split(lines[0], " ")[1])
	if err != nil {
		log.Fatal(err)
	}
	intervals, err := strings2ints(lines[1:])
	if err != nil {
		log.Fatal(err)
	}
	calculator := new()
	sum := calculator.Calculate(intervals, threshold)
	fmt.Println(sum)
}
