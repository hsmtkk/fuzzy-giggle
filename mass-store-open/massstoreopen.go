package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Problem struct {
	ConstructFee int
	HumanFee     int
	Profit       int
	Month        int
	Amounts      []int
}

func Solve(p Problem) int {
	count := 0
	for _, amount := range p.Amounts {
		profit := amount*p.Profit - p.ConstructFee - p.HumanFee*p.Month
		if profit < 0 {
			count += 1
		}
	}
	return count
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
	p := Problem{}
	ints, err := strings2ints(strings.Split(lines[0], " "))
	if err != nil {
		log.Fatal(err)
	}
	p.Month = ints[1]
	ints, err = strings2ints(strings.Split(lines[1], " "))
	if err != nil {
		log.Fatal(err)
	}
	p.ConstructFee = ints[0]
	p.HumanFee = ints[1]
	p.Profit = ints[2]
	amounts := []int{}
	for _, line := range lines[2:] {
		amount, err := strconv.Atoi(line)
		if err != nil {
			log.Fatal(err)
		}
		amounts = append(amounts, amount)
	}
	p.Amounts = amounts
	fmt.Println(strconv.Itoa(Solve(p)))
}
