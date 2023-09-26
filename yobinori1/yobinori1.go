package main

import (
	"fmt"
	"strconv"
)

func main() {
	n := 27000001
	i := 2
	for {
		if n%i == 0 {
			n /= i
			fmt.Println(strconv.Itoa(i))
			if n == 1 {
				break
			}
		} else {
			i += 1
		}
	}
}
