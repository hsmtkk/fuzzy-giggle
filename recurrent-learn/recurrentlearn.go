package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type CorrectOrNot struct {
	First  bool
	Second bool
}

type Solver interface {
	Solve(correctOrNots []CorrectOrNot) []int
}

type solverImpl struct{}

func new() Solver {
	return &solverImpl{}
}

func (s *solverImpl) Solve(correctOrNots []CorrectOrNot) []int {
	problems := []int{}
	for i, correctOrNot := range correctOrNots {
		if (!correctOrNot.First) || (!correctOrNot.Second) {
			problems = append(problems, i+1)
		}
	}
	return problems
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

func parseLines(lines []string) []CorrectOrNot {
	results := []CorrectOrNot{}
	for _, line := range lines {
		correctOrNot := CorrectOrNot{First: true, Second: true}
		line = strings.TrimSpace(line)
		elems := strings.Split(line, " ")
		if elems[0] == "n" {
			correctOrNot.First = false
		}
		if elems[1] == "n" {
			correctOrNot.Second = false
		}
	}
	return results
}

func main() {
	lines, err := readStdIn()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%v\n", lines)
	correctOrNots := parseLines(lines[1:])
	fmt.Printf("%v\n", correctOrNots)
	problems := new().Solve(correctOrNots)
	if len(problems) == 0 {
		fmt.Println("0")
	} else {
		fmt.Println(strconv.Itoa(len(problems)))
		for _, p := range problems {
			fmt.Println(strconv.Itoa(p))
		}
	}
}
